age = 1

if age < 2:
    print("É um bebê!")
if (age == 2) or (age < 4):
    print("É uma criança!")
elif age == 4 or age < 13:
    print("É um(a) garoto(a)")
elif age == 13 or age < 20:
    print("É um(a) adolescente!")
elif age == 20 or age < 65:
    print("É um adulto")
else:
    print("É um idoso!")
