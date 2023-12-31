from numpy import ndarray, asarray, multiply, add, divide, subtract, where
from math import sqrt


class Vector(ndarray):
    def __new__(cls, input_array, info=None):
        obj = asarray(input_array).view(cls)
        return obj

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    @x.setter
    def x(self, value):
        self[0] = value

    @y.setter
    def y(self, value):
        self[1] = value

    def magnitude(self):
        return sqrt(self.x*self.x + self.y*self.y)

    def normalize(self):
        m = self.magnitude()
        if m > 0:
            self.x /= m
            self.y /= m


# Basic vector transformations, they return numpy arrays
def multiply_vec(a, b):
    return multiply(a, b)


def divide_vec(a, b):
    return divide(where(a != 0, a, 1), where(b != 0, b, 1))


def add_vec(a, b):
    return add(a, b)


def subtract_vec(a, b):
    return subtract(a, b)
