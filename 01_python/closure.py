a = 1
b = a
print(a, b)
print(id(a), id(b))

a = 2
print(a, b)
print(id(a), id(b))

x = [1, 2, 3]
y = x
print(x, y)
print(id(x), id(y))
x.append(4)
print(x, y)
print(id(x), id(y))


d = 45


def func1():
    # global d
    d = 9
    print(d)


func1()
print(d)
# print(d)


def func():
    h = [3, 6]

    def inner():
        print(h)
        print(h)
    return inner


f = func()
print(f)
f()
