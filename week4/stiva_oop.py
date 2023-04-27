class Stack:

    def __init__(self, val_stiva = 1, val_stiva2 = 2):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        self.second = 5
        value = self.__stackList[-1]
        del self.__stackList[-1]
        return value
    def __str__(self):
        return f"{self.__stackList} {self.second}"

object_1 = Stack(val_stiva2=1, val_stiva= 2)
object_2 = Stack()
object_1.third = 6
object_1.push(3)
object_1.pop()
# print(object_1)
# object_2.push(object_1.pop())
# print(object_1._Stack__stackList)
print(object_1.__dict__)
print(object_2.__dict__)

# object_1.push(3)
# object_1.push(2)
# object_1.push(1)
# print(object_1.pop())
# print(object_1.pop())
# print(object_1.pop())
# print(len(object_1.stackList))