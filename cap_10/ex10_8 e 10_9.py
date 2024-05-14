def read_files(f):
    try:
        with open(f) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        print(f, "não encontrado")
    else:
        for lin in lines:
            print(lin.strip())


files = ["dog.txt", "cat.txt"]

for f in files:
    read_files(f)
