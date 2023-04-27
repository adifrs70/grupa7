# class FirstClass:
#
#     __counter = 0
#
#     def __init__(self, val = 33):
#         self.__first = val
#         FirstClass.__counter += 1
#
# object_1 = FirstClass()
# object_2 = FirstClass()
# object_3 = FirstClass()
# object_4 = FirstClass()
#
# print(object_1.__dict__, object_1._FirstClass__counter)
# print(object_2.__dict__, object_2._FirstClass__counter)
# print(object_3.__dict__, object_3._FirstClass__counter)

class Exemplu:
    def __init__(self, val):
        self.val = val
        self.a, self.b = None, None
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

    def denumire(self):
       return self.val

object = Exemplu(1)
print(object.a)
print(object.b)
print(object.denumire())
print(object.__dict__)
print(Exemplu.__dict__)
# try:
#     print(object.b)
# except AttributeError:
#     pass