from django import template

register = template.Library()

@register.filter
def design_id(id):
    return 'SG{:0>4}'.format(id)