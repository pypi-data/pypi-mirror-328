import re

from django.contrib.admin import display, register
from django.db.models import Field, Model
from django.forms import ModelForm
from django.http import HttpRequest
from django.urls import reverse

try:
    from import_export.admin import ImportExportModelAdmin as _BaseModelAdmin
except ImportError:
    from django.contrib.admin import ModelAdmin as _BaseModelAdmin

    
class BaseModelAdmin(_BaseModelAdmin):
    """
    A replacement ModelAdmin that transform blank values to null values for fields having `null` parameter set to True.
    """
    def _empty_to_null(self, obj: Model):
        field: Field
        for field in obj._meta.fields:
            if field.null:
                value = getattr(obj, field.attname, None)
                if value == '':
                    setattr(obj, field.attname, None)
    
    def save_model(self, request: HttpRequest, obj: Model, form: ModelForm, change: bool):
        self._empty_to_null(obj)
        super().save_model(request, obj, form, change)


# (ensure these attributes are marked as used)
__shortcuts__ = (display, register)


def admin_url(model: type[Model]|str|Model):
    """
    Get admin URL of the given model.
    
    Reference: https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#reversing-admin-urls
    """
    pk = None
    if isinstance(model, (type,Model)):
        app_label = model._meta.app_label
        model_name = model._meta.model_name
        if isinstance(model, Model):
            pk = model.pk
    else:
        m = re.match(r'^([a-z0-9_]+)[\._]([a-z0-9_]+)$', model, re.IGNORECASE)
        if m:
            app_label = m[1]
            model_name = m[2]
        else:
            raise ValueError(f"Invalid model type string: {model}")

    prefix = 'admin:%s_%s' % (app_label, model_name)
    if pk is None:
        return reverse(f'{prefix}_changelist')
    else:
        return reverse(f'{prefix}_change', args=[pk])
