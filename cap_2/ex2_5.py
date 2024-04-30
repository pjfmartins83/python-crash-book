"""
Citação famosa: Encontre uma citação de uma pessoa famosa que você admire.
Exiba a citação e o nome do autor. Sua saída devera ter a aparência a seguir,
incluindo as aspas: Albert Einstein uma vez disse: "Uma pessoa que nunca
cometeu um erro jamais tentou nada novo."
"""

first_name = "david"
last_name = "gilmour"
full_name = first_name + " " + last_name

quote = "Wish you were here."

print(full_name.title() + " uma vez disse: " + "\"" + quote + "\"")

print(f'{full_name.title()} uma vez disse: "{quote}"')
