def make_album(banda, título, faixas):
    álbum_dicionario = {
        "banda": banda.title(), "título": título.title()
    }
    if faixas:
        álbum_dicionario["número de faixas"] = faixas
    return álbum_dicionario


album = make_album("pink floyd", "animals", "5")
print(album)

album = make_album("jethro tull", "aqualung", "13")
print(album)

album = make_album("iron maiden", "the number of the beast", "8")
print(album)
