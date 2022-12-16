# x = print()
q = 9
g = 5


def func1(a, b, c=0):
    print(a+2, b*3, c)


def func2():
    print(q, g)


def func3(*args):
    print(type(args), args)


def func4(**kwargs):
    print(type(kwargs), kwargs)


func1(q+g, g/2)
func2()
func1(3, 6, 8)
func3(3, 6, 'r', True, 0.8)
func4(f=6, c='fdgdfg', u=True, e=4.6)
