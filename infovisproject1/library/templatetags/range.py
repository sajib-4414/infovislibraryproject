from django import template

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