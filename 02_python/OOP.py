"""
class ClassName:
    pass


class ChildClassName(Parent1, Parent2, ....):
    pass
"""


class Point:
    x = 0

    def __add__(self, other):
        tmp = Point()
        tmp.x = self.x + other.x
        # return self.x + other.x     # Point(self.x + other.x)
        return tmp


pt = Point()        # __new__(), __init__()
# pt()              # __call__()
# del pt            # __del__()
pt.x = 9

pt1 = Point()
pt1.x = 5
pt2 = Point()
pt2.x = 7

a = pt1 + pt2       # +=
print(a.x)
# b = pt1 - pt2
# s = pt1 > pt2
