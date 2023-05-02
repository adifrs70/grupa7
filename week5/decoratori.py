# def decorator_simplu(parametru):
#     print(f"Apelam functia {parametru.__name__}")
#     return parametru
#
# @decorator_simplu
# def functie_simpla():
#     return "Buna seara"
#
# print(functie_simpla())

def decorator_depozit(functia_noastra):
    def ambalaj_metoda(carti):
        return f"Ambalam produse din {functia_noastra.__name__} care contine cartea {carti}"
    return ambalaj_metoda

@decorator_depozit
def impachetare_carti(nume):
    return nume


print(impachetare_carti("Baltagul"))
print(impachetare_carti("Ion"))