bicycles = ["trek", "cannondale", "redline", "specialized"]


print(bicycles)     #mostrar itens da lista

print(bicycles[0])     #mostrar 1º item da lista

print(bicycles[0].title())     #mostrar 1º item da lista com a 1ª letra maiúsucla

print(bicycles[1]), print(bicycles[3])     #mostrar itens 2 e 4

print(bicycles[-1])     #mostrar último item da lista

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
