"""
r -> citim, nu adaugam read-only, daca fisierul nu exista apare eroare
w -> scriem, daca fiesierul nu exista, il adauga, daca exista deja ceva scris in fisier, il rescrie
a -> scriem, daca exista ceva scris in fisier, il adauga pe urm rand, nu rescrie, nu apare eroare daca fisierul nu exista
r+ -> scriere, citire, daca fisierul nu exista, apare eroare
"""

# file = open('data2.txt', "r+")
# file.write('Hello2')
# file.close()

# file = open('data1.txt', 'r+')
# try:
#     file.write("hello")
# finally:
#     file.close()

# with open('data.txt', 'w') as file:
    # file.writelines(['hello', 'hello1', 'hello2'])
#     file.write('hello\n')
#     file.write('hello1\n')
#     file.write('hello2\n')

# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print(line)

# with open('data.txt', 'r') as file:
#     print(list(file))
#     for line in list(file):
#         print(line)

# with open('data.txt', 'r') as file:
    # while True:
        # line = file.readline()
        # if not line:
            # break
        # print(line)