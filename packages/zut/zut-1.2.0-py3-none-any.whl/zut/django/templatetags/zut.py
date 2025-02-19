from __future__ import annotations
import logging
import re
from django import template
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import Form, widgets
from django.forms.boundfield import BoundField
from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.templatetags.static import static
from django.conf import settings
from zut import get_logger
from zut.django.admin import admin_url as _admin_url

_logger = get_logger(__name__)

register = template.Library()
        

#region Script and style libs

@register.simple_tag
def style_lib(package, file, version=None, integrity=None):
    """
    Usage example in Django base template:

        {% load static base %}
        ...
        <head>
        ...
        {% style_lib  'bootstrap' 'dist/css/bootstrap.min.css' '5.2.0' 'sha256-7ZWbZUAi97rkirk4DcEp4GWDPkWpRMcNaEyXGsNXjLg=' %}
        ...
        </head>
    """
    if file and version and re.match(r'^\d+', file):
        # invert
        arg2 = file
        file = version
        version = arg2

    url = _get_lib_url(package, file, version)

    if not version and not url in _missing_version:
        _logger.warning(f"Missing version for style_lib: {url}")
        _missing_version.add(url)
        
    html = f"<link rel=\"stylesheet\" href=\"{url}\""
    
    if integrity:
        html += f" integrity=\"{integrity}\" crossorigin=\"anonymous\""
    elif not url in _missing_integrity:
        _logger.warning(f"Missing integrity hash for style_lib: {url}")
        _missing_integrity.add(url)

    html += f" />"
    return mark_safe(html)


@register.simple_tag
def script_lib(package, file, version=None, integrity=None, defer=False):
    """
    Usage example in Django base template:

        {% load static base %}
        ...
        <head>
        ...
        {% script_lib 'bootstrap' 'dist/js/bootstrap.bundle.min.js' '5.2.0' 'sha256-wMCQIK229gKxbUg3QWa544ypI4OoFlC2qQl8Q8xD8x8=' %}
        ...
        </head>
    """
    if file and version and re.match(r'^\d+', file):
        # invert
        arg2 = file
        file = version
        version = arg2
    
    url = _get_lib_url(package, file, version)
    
    if not version and not url in _missing_version:
        _logger.warning(f"Missing version for script_lib: {url}")
        _missing_version.add(url)

    html = f"<script"
    if defer:
        html=" defer"
    html += f" src=\"{url}\""
    
    if integrity:
        html += f" integrity=\"{integrity}\" crossorigin=\"anonymous\""
    elif not url in _missing_integrity:
        _logger.warning(f"Missing integrity hash for script_lib: {url}")
        _missing_integrity.add(url)

    html += f"></script>"
    return mark_safe(html)

# avoid logging warnings for every request
_missing_version: set[str] = set()
_missing_integrity: set[str] = set()

def _get_lib_url(package, file, version=None, prefix=None):
    LOCAL_STATIC_LIB = getattr(settings, "LOCAL_STATIC_LIB", False)
    if LOCAL_STATIC_LIB:
        return static(f"lib/{package}/{file}")
    else:
        if version:
            return f"https://cdn.jsdelivr.net/npm/{package}@{version}/{file}"
        else:
            return f"https://cdn.jsdelivr.net/npm/{package}/{file}"
        
#endregion


@register.simple_tag
def admin_url(model):
    return _admin_url(model)


@register.filter
def prefix_unless_empty(value: str, prefix: str):
    value = value.strip()
    if not value:
        return value
    else:
        return f"{prefix}{value}"


@register.filter
def suffix_unless_empty(value: str, suffix: str):
    value = value.strip()
    if not value:
        return value
    else:
        return f"{value}{suffix}"


@register.filter
def field_attrs(field: BoundField, attrs: str):
    # See original idea: https://stackoverflow.com/a/69196141
    actual_attrs = dict(field.field.widget.attrs)
    css_classes = actual_attrs['class'].split(' ') if 'class' in actual_attrs else []

    for attr in attrs.split(','):
        if ':' not in attr:
            for css_class in attr.split(' '):
                if css_class not in css_classes:
                    css_classes.append(css_class)
        else:
            key, val = attr.split(':')
            actual_attrs[key] = val
    
    if css_classes:
        actual_attrs['class'] = ' '.join(css_classes)
    return field.as_widget(attrs=actual_attrs)


@register.filter
def field_horizontal(field: BoundField, label_col = 4):    
    widget = field.field.widget
    if isinstance(widget, (widgets.CheckboxInput, widgets.RadioSelect)):
        attrs = 'form-check-input'
    elif isinstance(widget, (widgets.Select, widgets.SelectMultiple)):
        attrs = 'form-select'
    else:
        attrs = 'form-control'

    if field.errors:
        attrs += ' is-invalid'
    
    html = f'''<div class="row mb-{label_col}">
        <label for="{field.auto_id}" class="col-sm-4 col-form-label">{field.label}</label>
        <div class="col-sm-{12 - label_col}">'''
    
    html += field_attrs(field, attrs)

    if field.errors:
        html += '<div class="invalid-feedback">'
        for error in field.errors:
            html += f'<div>{escape(error)}</div>'
        html += '</div>'
    
    html += '''</div>
    </div>'''
    return mark_safe(html)


@register.filter
def form_horizontal(form: Form, label_col = 4):
    html = ''

    if form.errors:
        html += '<div class="alert alert-danger" role="alert">'
        for error in form.non_field_errors():
            html += f'<div>{escape(error)}</div>'
        fields_with_errors = [f"<strong>{name}</strong>" for name in form.errors if name != NON_FIELD_ERRORS]
        if fields_with_errors:
            html += f'<div>Invalid field{"s" if len(fields_with_errors) > 1 else ""}: {", ".join(fields_with_errors)}.</div>'
        html += '</div>'

    for field in form:
        html += field_horizontal(field, label_col=label_col)

    return mark_safe(html)
