"""
Django middleware.
"""
from types import FunctionType

from django.conf import settings
from django.contrib.auth.backends import RemoteUserBackend as BaseRemoteUserBackend
from django.contrib.auth.middleware import PersistentRemoteUserMiddleware as BasePersistentRemoteUserMiddleware
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import AbstractUser, AnonymousUser
from django.contrib.auth.views import LoginView, LogoutView, redirect_to_login
from django.http import HttpRequest, JsonResponse
from django.views.generic import RedirectView

from zut import get_logger

try:
    from asgiref.local import Local
except ImportError:
    from threading import local as Local

try:
    from rest_framework.permissions import AllowAny as APIAllowAny
    from rest_framework.views import APIView
    _with_rest_framework = True
except ImportError:
    _with_rest_framework = False

_logger = get_logger(__name__)


#region Thread

class ThreadLocalMiddleware:
    """
    Register request object as a local context/thread variable.
    
    This make it available to parts of Django that do not have direct access to the request,
    such as models (e.g. allows historization of the authenticated user making a change).
    """
    _local = Local()

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        self.__class__._local.request = request
        response = self.get_response(request)
        del self.__class__._local.request
        return response

    @classmethod
    def get_request(cls) -> HttpRequest:
        try:
            return cls._local.request
        except:
            return None

    @classmethod
    def get_user(cls) -> AbstractUser:
        request = cls.get_request()
        if request is None:
            return AnonymousUser()        
        return request.user

#endregion


#region Authentication

class RemoteUserBackend(BaseRemoteUserBackend):
    """
    Usage example in `settings.py`:

    ```
    REMOTE_USER_STRIP_SUFFIXES = ['@mydomain.lan']
    REMOTE_USER_STRIP_PREFIXES = ['adm_', 'adm_t0_', 'adm_t1_', 'adm_t2_']
    REMOTE_USER_APPEND_DOMAIN = '@mydomain.com'

    AUTHENTICATION_BACKENDS = [
        'zut.django.middleware.RemoteUserBackend',
    ]
    ```
    
    """
    _strip_prefixes: list[str]
    _strip_suffixes: list[str]
    _append_domain: str
    _append_domain_is_mail: bool

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._strip_suffixes = settings.REMOTE_USER_STRIP_SUFFIXES
        if self._strip_suffixes:
            if isinstance(self._strip_suffixes, str):
                self._strip_suffixes = [self._strip_suffixes]
            self._strip_suffixes.sort(key=lambda suffix: -len(suffix))

        self._strip_prefixes = settings.REMOTE_USER_STRIP_PREFIXES
        if self._strip_prefixes:
            if isinstance(self._strip_prefixes, str):
                self._strip_prefixes = [self._strip_prefixes]
            self._strip_prefixes.sort(key=lambda suffix: -len(suffix))

        self._append_domain = settings.REMOTE_USER_APPEND_DOMAIN
        self._append_domain_is_mail = False
        if self._append_domain:
            if self._append_domain.startswith('@'):
                self._append_domain_is_mail = True
            elif not self._append_domain.endswith('\\'):
                raise ValueError("REMOTE_USER_APPEND_DOMAIN must start with '@' or end with '\\'")

    def clean_username(self, username: str):
        _logger.debug("Raw remote user: %s", username)

        username = username.lower()

        if self._strip_suffixes:        
            for suffix in self._strip_suffixes:
                if username.endswith(suffix):
                    username = username[0:-len(suffix)]

        if self._strip_prefixes:        
            for prefix in self._strip_prefixes:
                if username.startswith(prefix):
                    username = username[len(prefix):]

        if self._append_domain:
            if self._append_domain_is_mail:
                if not '@' in username:
                    username = f'{username}{self._append_domain}'
            else:
                if not '\\' in username:
                    username = f'{self._append_domain}{username}'

        return username


class PersistentRemoteUserMiddleware(BasePersistentRemoteUserMiddleware):
    """
    Usage example in `settings.py`:

    ```    
    DEBUG_REMOTE_USER = 'dev@mydomain.fr'

    MIDDLEWARE = [
        ...
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'zut.django.middleware.PersistentRemoteUserMiddleware',
        'zut.django.middleware.SuperUserDefaultAuthorizationMiddleware',
        'zut.django.middleware.ThreadLocalMiddleware',
        ...
    ]
    ```
    """
    def process_request(self, request):
        if settings.DEBUG and settings.DEBUG_REMOTE_USER and not 'REMOTE_USER' in request.META:
            request.META['REMOTE_USER'] = settings.DEBUG_REMOTE_USER
        super().process_request(request)

#endregion


#region Authorization

class SuperUserDefaultAuthorizationMiddleware:
    """
    Restrict non-protected views to superuser.

    Views may be protected using an AccessMixin (standard class-based views)
    or with `permission_classes` attribute (Django Rest Framework API views).
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)
        return response

    def process_view(self, request: HttpRequest, view_func, view_args, view_kwargs):        
        if settings.DEBUG and settings.MEDIA_URL != '/' and request.path.startswith(settings.MEDIA_URL):
            return
         
        try:
            view_class = view_func.view_class
            # Class-based view
            return self.process_view_class(request, view_class)
        except AttributeError:
            try:
                view_class = view_func.cls
                # API viewset (Django Rest Framework)
                return self.process_view_class(request, view_class)
            except AttributeError:
                # function-based view
                return self.process_view_func(request, view_func)
    
    def process_view_func(self, request: HttpRequest, view_func: FunctionType):
        """
        Process a function-based view.
        """
        if view_func.__module__ in {'django.views.static', 'import_export.admin'} or view_func.__module__.startswith(("django.contrib.", "")):
            return # ignore: use default visibility
        
        _logger.warning("Unexpected function-based view %s (%s)", f"{view_func.__module__}.{view_func.__name__}", request.path)
        if not self.is_authorized(request.user):
            return redirect_to_login(next=request.get_full_path())
        
    def process_view_class(self, request: HttpRequest, view_class: type):
        if request.path == '/':
            return # ignore
        
        elif issubclass(view_class, (LoginView, LogoutView, RedirectView)):
            return # ignore

        elif _with_rest_framework and issubclass(view_class, APIView):
            # API view (Django Rest Framework)
            if not view_class.permission_classes or (view_class.permission_classes == [APIAllowAny] and not 'permission_classes' in view_class.__dict__):
                _logger.warning("API view class %s (%s) has no direct permission_classes", f"{view_class.__module__}.{view_class.__qualname__}", request.path)
                if not self.is_authorized(request.user):
                    return JsonResponse({"detail": "API permissions not properly configured."}, status=403)

        else:
            # Standard class-based view
            if not issubclass(view_class, AccessMixin):
                _logger.warning("View class %s (%s) has no AccessMixin", f"{view_class.__module__}.{view_class.__qualname__}", request.path)
                if not self.is_authorized(request.user):
                    return redirect_to_login(next=request.get_full_path())

    def is_authorized(self, user: AbstractUser):
        return user.is_superuser

#endregion
