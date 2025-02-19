"""
General-purpose Django template context processors.
"""
from datetime import date
from django.http import HttpRequest
from django.conf import settings
from django.urls import get_script_prefix

def general(request: HttpRequest):
    """
    Return general-purpose context variables.
    """
    today = date.today()

    return {
        'script_prefix': get_script_prefix(),
        'copyright_years': f"{settings.COPYRIGHT_FIRST_YEAR}{f'-{today.year}' if today.year > settings.COPYRIGHT_FIRST_YEAR else ''}" if settings.COPYRIGHT_FIRST_YEAR else today.year,
        'env_name': settings.ENV_NAME,
        'registration_opened': settings.REGISTRATION_OPENED,
    }
