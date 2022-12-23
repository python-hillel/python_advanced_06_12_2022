class Base1:
    pass


class Base2:
    pass


class Child(Base1, Base2):
    pass


ch = Child()
# ch.test()
print(Child.mro())  # Method Resolution Order
print(Child.__mro__)


class I:
    pass


class K:
    pass


class L:
    pass


class A(I, K):
    pass


class B(K, L):
    pass


class X(A, B, L):
    pass


print(X.mro())
