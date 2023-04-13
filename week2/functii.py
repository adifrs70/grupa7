# print("String")
# var1 = 1
# print("String {}".format(var1))
# input("Adauga o cifra")
# def functie_adunare(param1):
#     print('print')
#     return param1, '-'
#
# functie_adunare(1)

# def get_sum(a: int = 1 , b: int = 3, c: int =2, *args) -> (int, int):
#     suma = a + b + c
#     diferenta = a - b - c
#     for i in args:
#         suma += i
#         diferenta -= i
#     return suma, diferenta


def get_sum(a: int = 1 , b: int = 3, c: int =2, *args, **kwargs) -> (int, int):
    """

    :param a:
    :param b:
    :param c:
    :param args:
    :param kwargs:
    :return:
    """
    suma = a + b + c
    diferenta = a - b - c
    print(args)
    print(kwargs, type(kwargs))
    for i in kwargs.values():
        suma += i
        diferenta -= i
    return suma, diferenta

var1, var2 = get_sum(1,-3, -4, 4, d = 3, e = 6, f=5)
print(var1, var2)