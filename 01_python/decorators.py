from datetime import datetime


def measure_time(param1):
    from datetime import datetime
    print(param1)

    def inner(function):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = function(*args, **kwargs)
            print(datetime.now() - start)
            return result

        wrapper.__doc__ = function.__doc__
        wrapper.__name__ = function.__name__

        return wrapper
    return inner


# Don't Repeat Yourself
@measure_time('GEN1')
def gen1(n):
    """
    Генератор списков 1
    :return: List
    """
    lst = []
    # start = datetime.now()
    for i in range(n):
        if i % 2 == 0:
            lst.append(i)
    # print(datetime.now() - start)
    return lst


@measure_time('GEN2')
@measure_time('TEST')
def gen2(n):
    """
    Генератор списков 2
    :return: List
    """
    # start = datetime.now()
    lst = [i for i in range(n) if i % 2 == 0]
    # print(datetime.now() - start)
    return lst


# print('Name:', gen.__name__)
# print('Doc:', gen.__doc__)

f = gen1
print(f)
# print(f())
#
# mt = measure_time(gen1)
# print(mt)
# print(mt())

print(gen1(20))       #  gen1 ==> wrapper()
print(gen2(20))       #  gen2 ==> wrapper()

print('Doc:', gen1.__doc__, '\nName:', gen1.__name__)
print('Doc:', gen2.__doc__, '\nName:', gen2.__name__)
