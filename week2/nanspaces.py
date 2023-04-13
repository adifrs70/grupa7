from functii2 import functie2


variabila_1 = 2
b = 2
a = 3
msg = 3


def functie_1(a, b):
    variabila_1 = a + b
    # global msg
    # msg = 'Hello'
    return variabila_1



print(msg, 'rand 14')
print(variabila_1, 'rand 13')
suma = functie_1(1, 2)
print(suma)

functie2(4, 5)