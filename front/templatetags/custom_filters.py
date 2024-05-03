# custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_list2_value(list2, index):
    return list2[index]