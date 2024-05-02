def make_album(banda, título):
    álbum_dicionario = {
        "banda": banda.title(), "título": título.title()
    }
    return álbum_dicionario


album = make_album("pink floyd", "animals")
print(album)

album = make_album("jethro tull", "aqualung")
print(album)

album = make_album("iron maiden", "the number of the beast")
print(album)
