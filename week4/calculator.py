class Calculator:

    def __init__(self):
        self.first_op = float(input("Alege primul numar: "))
        self.second_op = float(input("Alege cel de-al doilea numar: "))
        self.op = input("Alege operatorul: ")


    def Adunare(self):
        return(self.first_op + self.second_op)

    def Scadere(self):
        return(self.first_op - self.second_op)

    def Inmultire(self):
        return(self.first_op * self.second_op)

    def Impartire(self):
        if(self.second_op != 0):
            return(self.first_op / self.second_op)
        else:
            return("Nu functioneaza")

    def __str__(self):
        if (self.op == '-'):
           return str(self.Scadere())
        elif (self.op == '+'):
           return str(self.Adunare())
        elif (self.op == '/'):
           return str(self.Impartire())
        else:
           return str(self.Inmultire())


obiect1 = Calculator()
print(obiect1)