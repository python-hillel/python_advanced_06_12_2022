from django import template

register = template.Library()


# tag
def expression(value, *args):
    for idx, arg in enumerate(args, 1):
        value = value.replace(f'%{idx}', str(arg))
    return eval(value)

# {% expression '(%1 - 1) * 100 // %2' 23 56 as progress_level %}


"""
    '(%1 - 1) * 100 // %2' % (34, 56)  ===>   '(34 - 1) * 100 // 56'
    args = (23, 56)
    1 23
    2 56
    '(23 - 1) * 100 // 56'
"""

register.simple_tag(func=expression, name='expression')
