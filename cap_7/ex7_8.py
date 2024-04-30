pedidos = ['peixe', 'frango', 'vegetariano', 'bovino']

for i in range(3):
    pedidos.append('pastrami')
terminados = []
print("Desculpe, estamos sem ingredientes para pastrami")
while 'pastrami' in pedidos:
    pedidos.remove('pastrami')
while pedidos:
    sandwich = pedidos.pop()
    print("Estou fazendo " + sandwich)
    terminados.append(sandwich)
print("Sandiwiches prontos: ")
for sandwich in terminados:
    print(sandwich.title())
