filename = "guest.txt"

name = input("Qual seu nome?: ")
with open(filename, "a") as file_object:
    file_object.write(name + "\n")
