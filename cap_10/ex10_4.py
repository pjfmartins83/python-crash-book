filename = "guest_book.txt"

names = []
while True:
    print("Qual seu nome?")
    user_input = input("Tecle 'n' se você quer parar: ")
    if user_input == 'n':
        break
    names.append(user_input) 

with open(filename, "a") as file_object:
    for name in names:
        file_object.write(name + "\n")
