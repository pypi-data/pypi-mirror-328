from __future__ import annotations

from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import get_user_model, login, views as auth_views, forms as auth_forms
from django.db.models.base import Model as Model
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import get_script_prefix, reverse_lazy
from django.utils.safestring import mark_safe
from django.views import generic
from django import forms
from zut.django.mixins import AllowAnonymousMixin, IsAuthenticatedMixin


class IndexView(AllowAnonymousMixin, generic.TemplateView):
    template_name = 'zut/index.html'


class LangView(AllowAnonymousMixin, generic.View):
    def get(self, request: HttpRequest, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args, **kwargs):
        redirect_to = get_script_prefix() + self.request.POST.get('next', self.request.GET.get('next', '')).lstrip('/')

        if not settings.USE_I18N:
            messages.error(request, mark_safe(f"Translations are not enabled."))
            return HttpResponseRedirect(redirect_to)
            
        lang = self.request.POST.get('lang', self.request.GET.get('lang', None))
        if not lang:
            messages.error(request, mark_safe(f"No `lang` parameter provided."))
            return HttpResponseRedirect(redirect_to)
        
        lang_name = None
        for a_lang, a_name in settings.LANGUAGES:
            if a_lang == lang:
                lang_name = a_name
                break 
        
        if lang_name is None:
            messages.error(request, mark_safe(f"Unknown or unsupported language <strong>{lang}</strong>."))
            return HttpResponseRedirect(redirect_to)

        response = HttpResponseRedirect(redirect_to)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
        messages.success(request, mark_safe(f"Language changed to <strong>{lang}</strong> ({lang_name})."))
        return response


class RegisterView(AllowAnonymousMixin, SuccessMessageMixin, generic.CreateView):
    model = get_user_model()
    template_name = 'zut/register.html'

    class Form(auth_forms.UserCreationForm):
        email = forms.EmailField()

        class Meta:
            model = get_user_model()
            fields = ['username', 'email']

    def form_valid(self, form: Form):
        response = super().form_valid(form)
        login(self.request, form.instance) # ROADMAP: move me to the email confirmation callback.
        return response

    form_class = Form
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)
    success_message = 'User created successfully.' #ROADMAP: <br/>Please <strong>click on the link sent to your mailbox</strong> to validate your email address.


class LoginView(AllowAnonymousMixin, auth_views.LoginView):
    template_name = 'zut/login.html'


class LogoutView(AllowAnonymousMixin, auth_views.LogoutView):
    template_name = 'zut/logged_out.html'


class ProfileView(IsAuthenticatedMixin, generic.DetailView):
    template_name = 'zut/profile.html'

    def get_object(self):
        return self.request.user
