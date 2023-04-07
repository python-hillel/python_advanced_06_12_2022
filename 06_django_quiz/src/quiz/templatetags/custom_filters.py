from django import template

register = template.Library()


# filter
def negative(value):        # -5
    return -value


# filter
def multi(value, arg):
    return value * arg


# filter
def dived(value, arg):
    return value // arg


register.filter('negative', negative)
register.filter('multi', multi)
register.filter('dived', dived)
