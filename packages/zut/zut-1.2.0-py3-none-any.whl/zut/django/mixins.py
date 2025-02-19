"""
Mixins. NOTE: these cannot be in main `zut.django` module as they require the app registry to be loaded.
"""
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied


#region Authorization mixins

class UserPassesTestOrRedirectMixin(UserPassesTestMixin):
    def handle_no_permission(self):
        """
        Redirect to login page, even if the user is already authenticated: displays "You are logged in as xxx, but you are not authorized to access this page. Do you want to log in as another user?".
        (Default AccessMixin's handle_no_permission() method simply displays a 403 error in this situation).
        """
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect_to_login(self.request.get_full_path())


class AllowAnonymousMixin(UserPassesTestMixin):
    def test_func(self):
        return True


class IsAuthenticatedMixin(UserPassesTestOrRedirectMixin):
    def test_func(self):
        return self.request.user.is_authenticated


class IsSuperUserMixin(UserPassesTestOrRedirectMixin):
    def test_func(self):
        return self.request.user.is_superuser

#endregion
