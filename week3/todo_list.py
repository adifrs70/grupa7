categorii = input("Introduceți categoriile de taskuri separate prin virgulă: ")
categorii = [cat.strip() for cat in categorii.split(",")]

with open("categorii.txt", "w") as file:
    for cat in categorii:
        file.write(cat + "\n")


def afisare_categorii():
    try:
        with open("categorii.txt", "r") as file:
            categorii = file.read().splitlines()
            print("Categoriile de task-uri disponibile sunt:")
            for cat in categorii:
                print(cat)
    except FileNotFoundError:
        print("Nu există categorii de task-uri disponibile.")

def afisare_taskuri():
    try:
        with open("taskuri.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Nu există task-uri salvate încă.")


def adaugare_task():
    task = input("Introduceți un task: ")
    deadline = input("Introduceți data limită (format: DD.MM.YYYY HH:MM): ")
    responsabil = input("Introduceți persoana responsabilă: ")
    categoria = input("Introduceți categoria: ")

    try:
        with open("taskuri.txt", "a") as file:
            file.write(f"{task} - {deadline} - {responsabil} - {categoria}\n")
        print("Task adăugat cu succes!")
    except:
        print("Eroare la salvarea task-ului.")



while True:
    print("\nMeniu principal:")
    print("1. Adăugare task")
    print("2. Afișare task-uri")
    print("3. Afisare categorii")
    print("4. Ieșire")
    optiune = input("Selectați o opțiune: ")
    if optiune == "1":
         adaugare_task()
    elif optiune == "2":
         afisare_taskuri()
    elif optiune == "3":
         afisare_categorii()
    elif optiune == "4":
        break
    else:
        print("Opțiune invalidă. Încercați din nou.")