print("Escolha dois números")
print("Adicione dois zeros para sair")


def add_two():
    try:
        um = int(input())
        dois = int(input())
    except ValueError:
        print("Me desculpe, seus números não foram aceitos")
        return True
    else:
        print(str(um + dois))
        if um == 0 and dois == 0:
            return False
        return True
    

while add_two():
    continue
