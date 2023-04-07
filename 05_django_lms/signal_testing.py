from django.dispatch import Signal

signal1 = Signal()
signal2 = Signal()


def func1(*args, **kwargs):
    print(f'FUNC 1: {args} - {kwargs}')


def func2(*args, **kwargs):
    print(f'FUNC 2: {args} - {kwargs}')


def func3(*args, **kwargs):
    print(f'FUNC 3: {args} - {kwargs}')


def func4(*args, **kwargs):
    print(f'FUNC 4: {args} - {kwargs}')


signal1.connect(func1)
signal1.connect(func3)

signal2.connect(func2)
signal2.connect(func4)

signal1.send(sender='Test 1 signal 1', val1=23, val2='Hello')
signal2.send(sender='Test 1 signal 2', val1=True, val2=34.5)

signal1.disconnect(func1)
print('-' * 140)

signal1.send(sender='Test 2 signal 1', val1=23, val2='Hello')
signal2.send(sender='Test 2 signal 2', val1=True, val2=34.5)