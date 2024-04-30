prompt = ("Digite sua idade para continuar ou 'sair' para sair.")
idade = int(input(prompt))

while True:
    if idade == 'sair':
        break

    if idade < 3:
        print("Ingresso Gratuito!")
        break

    elif idade < 12:
        print("O valor do seu ingresso é de 10 dólares.")
        break
              
    else:
        print("O valor do seu ingresso é de 15 dólares.")
        break
