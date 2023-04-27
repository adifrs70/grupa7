class Exemplu1:
    counter = 1

    def name(self):
        return "sad"


class Exemplu2(Exemplu1):
    counter = 2
    # def name(self):
    #     return "Leo"


class Exemplu3(Exemplu2):
    pass
    # def name(self):
    #     return "Messi"


obiect1 = Exemplu3()
print(obiect1.name())