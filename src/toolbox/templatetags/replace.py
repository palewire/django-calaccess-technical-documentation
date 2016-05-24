from django import template

register = template.Library()

@register.filter
def replace(value, old_str, new_str):
    return value.replace(old_str, new_str)