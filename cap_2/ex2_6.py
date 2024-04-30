"""
Citação famosa 2: Repita o exercício 2.5, porém, desta vez, armazene o nome
da pessoa famosa em uma variável chamada famous_person. Em seguida, componha
sua mensagem e armazene-a em uma nova variável chamada message. Exiba sua
mensagem.
"""

first_name = "david"
last_name = "gilmour"
famous_person = first_name + " " + last_name

quote = "Wish you were here."

message = (famous_person.title() + " uma vez disse: " + "\"" + quote + "\"")

print(message)
