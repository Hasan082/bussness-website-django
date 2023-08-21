from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()

@register.filter
@stringfilter
def truncate_and_ellipsis(value, max_length):
    if len(value) > max_length:
        return value[:max_length-3] + '...'
    return value
