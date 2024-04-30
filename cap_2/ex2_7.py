"""
Removendo caracteres em branco de nomes: Armazene o nome de uma pessoa e
inclua alguns caracteres em branco no início e no final do nome. Lembre-se
de usar cada combinação de caracteres, "\t" e "\n", pelo menos uma vez.
Exiba o nome uma vez, de modo que os espaços em branco em torno do nome
sejam mostrados. Em seguida, exiba o nome usando cada uma das três funções
de remoção de espaços: lstrip(), rstrip() e strip().
"""

name = "                  Paulo  "
name_right = name.rstrip()
name_left = name.lstrip()
name_clean = name.strip()
print(name)
print(name_right)
print(name_left)
print(name_clean)
