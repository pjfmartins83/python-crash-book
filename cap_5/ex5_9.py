usuarios = []

if usuarios:
    
    for usuario in usuarios:
        
        if usuario == 'admin':
            print("Olá admin, gostaria de ver um relatório de status?")
        
        else:
            print("Olá " + usuario + ", obrigado(a) por fazer login novamente.")

else:
    print("Precisamos encontrar alguns usuarios!")
