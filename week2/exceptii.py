a = input("Alegeti o valoare: ")
try:
    print(int(a))
    print(variabila_nedefinita)
except ValueError:
    print("S-a intalnit o eroare")
    a = input('Alegeti o valoare: ')
except NameError as e:
    variabila_nedefinita = None
    print('Name error', e)
except Exception as e:
    print(e)
else:
    print("S-a excetut cu succes")
finally:
    print("Se executa oricum")
print("A trecut de blocul de try-except", variabila_nedefinita)