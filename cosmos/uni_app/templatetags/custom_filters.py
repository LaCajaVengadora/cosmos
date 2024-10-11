from django import template

register = template.Library()

@register.filter
def to_int(value):
    try: return int(value)
    except (ValueError, TypeError): return None

@register.filter
def get_by_cat(carreras, cat):
    return [c for c in carreras if c.cat.id == cat][:5]