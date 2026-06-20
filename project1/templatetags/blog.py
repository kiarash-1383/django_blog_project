from django import template
from ..models import *
register = template.Library()

@register.filter()
def upper_case(value):
    return value.upper()

@register.simple_tag()
def somthing(value):
    return value * 2

