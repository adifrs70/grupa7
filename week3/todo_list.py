def introducere_categorii():
    categorii = input("Introduceți categoriile de taskuri separate prin virgulă: ")
    categorii = [cat.strip() for cat in categorii.split(",")]
    with open("categorii.txt", "r") as file:
        categorii_existent = file.read().splitlines()
    for cat in categorii:
        if cat in categorii_existent:
            print(f"Categoria '{cat}' există deja. Nu se permite adăugarea acelorasi categorii.")
            return
    try:
        with open("categorii.txt", "a") as file:
            for cat in categorii:
                file.write(cat + "\n")
        print("Categorii adăugate cu succes!")
    except:
        print("Eroare la adăugarea categoriilor.")


def afisare_categorii():
    try:
        with open("categorii.txt", "r") as file:
            categorii = file.read().splitlines()
            if categorii:
                print("Categoriile de task-uri disponibile sunt:")
                for cat in categorii:
                    print(cat)
            else:
                print("Nu există categorii de task-uri disponibile.")
    except FileNotFoundError:
        print("Nu există categorii de task-uri disponibile.")

def afisare_taskuri():
    try:
        with open("taskuri.txt", "r") as file:
            taskuri = file.read().splitlines()
            if taskuri:
                print("Task-urile disponibile sunt:")
                tasks_string = "\n".join(taskuri)
                print(tasks_string)
            else:
                print("Nu există task-uri disponibileca.")
            return taskuri
    except FileNotFoundError:
        print("Nu există task-uri disponibile.")
        return []
def adaugare_task():
    task = input("Introduceți un task: ")
    deadline = input("Introduceți data limită (format: DD.MM.YYYY HH:MM): ")
    responsabil = input("Introduceți persoana responsabilă: ")
    categoria = input("Introduceți categoria: ")

    with open("categorii.txt", "r") as file:
        categorii_disponibile = file.read().splitlines()
        while categoria not in categorii_disponibile:
            print("Categoria menționată nu există. Categoriile disponibile sunt:")
            for cat in categorii_disponibile:
                print(cat)
            categoria = input("Introduceți categoria: ")
        else:
            with open("taskuri.txt", "r") as file:
                taskuri_existent = file.read().splitlines()
            if f"{task} - {deadline} - {responsabil} - {categoria}" in taskuri_existent:
                print("Task-ul există deja. Nu se permite adăugarea acelorasi taskuri.")
                return
            try:
                with open("taskuri.txt", "a") as file:
                    file.write(f"{task} - {deadline} - {responsabil} - {categoria}\n")
                print("Task adăugat cu succes!")
            except:
                print("Eroare la salvarea task-ului.")

def sortare_taskuri():
    try:
        with open("taskuri.txt", "r") as file:
            taskuri = file.read().splitlines()
            if taskuri:
                taskuri_sorted = sorted(taskuri)
                print("Task-urile sortate sunt:")
                for task in taskuri_sorted:
                    print(task)
            else:
                print("Nu există task-uri salvate încă.")
    except FileNotFoundError:
        print("Nu există task-uri salvate încă.")
    return taskuri
def editare_task(numar_task):
    taskuri = afisare_taskuri()
    if taskuri:
        if numar_task >= 1 and numar_task <= len(taskuri):
            task_ales = taskuri[numar_task - 1]
            print(f"Task-ul selectat este: {task_ales}")
            detalii = task_ales.split(" - ")
            task = detalii[0]
            deadline = detalii[1]
            responsabil = detalii[2]
            categoria = detalii[3]

            print("Introduceți noile detalii pentru task (lăsați necompletat pentru a păstra valoarea curentă):")
            task_nou = input(f"Task [{task}]: ") or task
            deadline_nou = input(f"Deadline [{deadline}]: ") or deadline
            responsabil_nou = input(f"Responsabil [{responsabil}]: ") or responsabil
            categoria_noua = input(f"Categorie [{categoria}]: ") or categoria

            taskuri[numar_task - 1] = f"{task_nou} - {deadline_nou} - {responsabil_nou} - {categoria_noua}"

            with open("taskuri.txt", "w") as file:
                file.write("\n".join(taskuri))
            print("Task actualizat cu succes!")
        else:
            print("Numărul de task introdus nu este valid.")
    else:
        print("Nu există task-uri salvate încă.")

def stergere_task():
    try:
        with open("taskuri.txt", "r") as file:
            taskuri = file.readlines()
            if taskuri:
                print("Selectați task-ul pe care doriți să-l ștergeți:")
                for i, task in enumerate(taskuri):
                    print(f"{i+1}. {task.strip()}")
                selectie = input("Introduceți numărul task-ului: ")
                try:
                    selectie = int(selectie)
                    if selectie < 1 or selectie > len(taskuri):
                        raise ValueError
                except:
                    print("Opțiune invalidă. Încercați din nou.")
                    return
                task_selectat = taskuri[selectie-1]
                confirmare = input(f"Sigur doriți să ștergeți task-ul '{task_selectat.strip()}'? (da/nu) ")
                if confirmare.lower() == "da":
                    with open("taskuri.txt", "w") as file:
                        for task in taskuri:
                            if task != task_selectat:
                                file.write(task)
                    print("Task șters cu succes!")
                else:
                    print("Operație anulată.")
            else:
                print("Nu există task-uri salvate încă.")
    except FileNotFoundError:
        print("Nu există task-uri salvate încă.")
while True:
    print("\nMeniu principal:")
    print("1. Adăugare task")
    print("2. Adaugare categorie")
    print("3. Afișare task-uri")
    print("4. Afisare categorii")
    print("5. Sortare taskuri")
    print("6. Editare task")
    print("7. Sterge task")
    print("8. Iesire")
    optiune = input("Selectați o opțiune: ")
    if optiune == "1":
         adaugare_task()
    elif optiune == "2":
         introducere_categorii()
    elif optiune == "3":
         afisare_taskuri()
    elif optiune == "4":
         afisare_categorii()
    elif optiune == "5":
         sortare_taskuri()
    elif optiune == "6":
        taskuri = afisare_taskuri()
        if taskuri:
            print("Pentru a edita un task, introduceți numărul corespunzător taskului în meniul principal:")
            numar_task_editare = int(input("Introduceți numărul taskului pe care doriți să-l editați: "))
            editare_task(numar_task_editare)
        else:
            print("Nu există task-uri salvate încă.")
    elif optiune == "7":
        stergere_task()
    elif optiune == "8":
        break
    else:
        print("Opțiune invalidă. Încercați din nou.")