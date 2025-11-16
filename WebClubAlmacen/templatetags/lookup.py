from django import template
register = template.Library()

@register.filter
def lookup(obj, key):
    try:
        return getattr(obj, key)
    except:
        return None
