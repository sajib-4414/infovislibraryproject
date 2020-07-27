from django import template
import re

register = template.Library()

@register.filter(name='range')
def filter_range(start, end):
  return range(start, end)

@register.filter
def to_and(value):
    return value.replace("/books/","")

@register.filter
def replace_space_with_plus(value):
    return value.replace(" ","+")

@register.filter
def remove_special_characters(value):
    plain_value = re.sub("[!@#$&/.']", '', value)
    return plain_value