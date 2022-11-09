from django import template
import numpy as np
register = template.Library()

@register.filter(name='noneZero')
def noneZero(valor):
    if valor != None:
        return valor
    else:
        return 0