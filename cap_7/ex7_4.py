message = ""
while message != 'sair':
    message = input("Digite seu ingrediente ou 'sair': ")

    if message != 'sair':
        print(message.title() + " foi adicionao ao seu pedido.")
