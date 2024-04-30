usuarios = ["admin", "paulo", "pedro", "maria", "joão"]

for usuario in usuarios:
    if usuario == "admin":
        print("Olá admin, gostaria de ver um relatório de status?")
    else:
        print("Olá " + usuario.title() + ", obrigado(a) por fazer login novamente.")
