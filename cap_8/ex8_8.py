def make_album(banda, título, faixas):
    álbum_dicionario = {
        "banda": banda.title(), "título": título.title()
    }
    if faixas:
        álbum_dicionario["número de faixas"] = faixas
    return álbum_dicionario


while True:
    banda = input("Qual o nome da banda?")
    título = input("Qual o nome do disco?")
    faixas = input("Quantas faixas tem o disco?")
