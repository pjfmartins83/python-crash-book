filename = "enquete.txt"

reasons = []

print("Para sair da enquete tecle 'n'")
while True:
    user_input = input("Pq você gosta de programar?: ")
    if user_input == 'n':
        break
    reasons.append(user_input)

with open(filename, "a") as file_object:
    for reason in reasons:
        file_object.write(reason + "\n")
