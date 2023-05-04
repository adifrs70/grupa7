tasks = []

def add_task():
    task = input("Introdu task-ul: ")
    date = input("Introdu data pana la care sa fie realizat task-ul (dd.mm.yyyy): ")
    person = input("Introdu persoana responsabila pentru task-ul mentionat: ")
    category = input("Introdu categoria din care face parte task-ul: ")
    tasks.append((task, date, person, category))


def write_to_file():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(','.join(task) + "\n")
        print("Task-urile au fost adaugate cu succes.")


def read_from_file():
    with open("tasks.txt", "r") as f:
        lines = f.readlines()
        tasks_sorted = sorted(lines, key = lambda line: line.split(",")[-1].strip())
        for line in tasks_sorted:
            print(line.strip())

while True:
    print("1. Introdu un task")
    print("2. Vizualizeaza task-urile")
    choice = input("Alege actiunea dorita (1, 2): ")
    if choice == '1':
        add_task()
    elif choice == '2':
        read_from_file()
        write_to_file()
        break
    else:
        print("Optiunea introdusa nu este valida")