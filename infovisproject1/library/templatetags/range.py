from django import template
import re
import random

register = template.Library()

@register.filter(name='range')
def filter_range(start, end):
  return range(start, end)

@register.filter
def to_and(value):
    return value.replace("/books/","")

@register.filter
def works_to_id(value):
    return value.replace("/works/","")

@register.filter
def replace_space_with_plus(value):
    return value.replace(" ","+")

@register.filter
def remove_special_characters(value):
    plain_value = re.sub("[!@#$&/.'()]", '', value)
    return plain_value

@register.simple_tag
def random_int(a, b=None):
    if b is None:
        a, b = 0, a
    return random.randint(a, b)

@register.simple_tag
def random_float(a, b=None):
    if b is None:
        a, b = 0, a
    return round(random.uniform(a,b), 1)