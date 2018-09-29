from django import template

register = template.Library()

@register.simple_tag
def get_value_by_key(source, key):
    return source.get(key)
