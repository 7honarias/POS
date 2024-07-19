from django import template
from sells.utils import format_currency
register = template.Library()

@register.filter
def currency(value):
    
    return format_currency(value)