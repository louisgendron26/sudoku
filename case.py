#!/usr/bin/env python3
class Case:
    def __init__(self, value, x, y, fixed = False):
        self.value = value
        self.x = x
        self.y = y
        self.fixed = fixed

    def set_val(self, new_value):
        if not self.fixed AND new_value in range(0,10):
            self.value = new_value
            return self

    def set_x(self, new_x):
        if new_x in range(0, 9):
            self.x = new_x
        else:
            print("Error : x value out of range")

    def set_y(self, new_y):
        if new_y in range(0, 9):
            self.y = new_y
        else:
            print("Error : y value out of range")

    def fix(self):
        self.fixed = True

    def unfix(self):
        self.fixed = False

    def get_val(self):
        return self.value

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def is_fixed(self):
        if self.fixed:
            return True
        else:
            return False
