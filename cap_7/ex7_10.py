active = True
férias = {}
while active:
    nome = input("Qual seu nome?: ")
    destino = input("Para onde você quer viajar?: ")
    férias[nome] = destino
    state = input("Você quer continuar?: sim ou não ")
    if state == 'não':
        active = False
for nome, destino in férias.items():
    print(nome + " quer viajar para " + destino)
