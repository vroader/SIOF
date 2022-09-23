from django import template
import numpy as np
register = template.Library()

@register.filter(name="soma")
def soma(values):
    total = 0
    for value in values:
        total += value
    return total
