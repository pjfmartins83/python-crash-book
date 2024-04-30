convidados = ["João", "Maria", "Antônio"]
convidados.insert(0, "Bernardo")
convidados.insert(2, "Valentina")
convidados.append("Morsa")

print("Pessoal, por problemas particulares vou poder convidar apenas duas pessoas no total")

bernardo = convidados.pop(0)
print(convidados)
maria = convidados.pop(2)
print(convidados)
joao = convidados.pop(0)

#print("Me desculpe, " + convidados.pop(0) + " ,você está sendo desconvidado.")
#print("Me desculpe, " + convidados.pop(1) + " ,você está sendo desconvidado.")
#print("Me desculpe, " + convidados.pop(3) + " ,você está sendo desconvidado.")
#print("Me desculpe, " + convidados.pop() + " ,você está sendo desconvidado.")
