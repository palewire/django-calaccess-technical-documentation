from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def format_page_anchor(value):
    return value.lower().replace('_', '-')