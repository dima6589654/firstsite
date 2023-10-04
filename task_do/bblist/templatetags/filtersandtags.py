from django import template

register = template.Library()


@register.filter(name='truncate_text')
def truncate_text(value, length):
    if len(value) > length:
        return value[:length] + '...'
    else:
        return value


@register.filter(name='to_uppercase')
def to_uppercase(value):
    return value.upper()
