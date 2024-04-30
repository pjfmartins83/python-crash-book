convidados = ["João", "Maria", "Antônio"]

print("Encontrei uma mesa maior, portanto a lista de convidados será \
      modificada!")
convidados.insert(0, "Bernardo")
convidados.insert(2, "Valentina")
convidados.append("Morsa")

message0 = convidados[0] + ", gostaria de jantar comigo?"
message1 = convidados[1] + ", gostaria de jantar comigo?"
message2 = convidados[2] + ", gostaria de jantar comigo?"
message3 = convidados[3] + ", gostaria de jantar comigo?"
message4 = convidados[4] + ", gostaria de jantar comigo?"
message5 = convidados[5] + ", gostaria de jantar comigo?"

print(message0, "\n" + message1, "\n" + message2, "\n" + message3, "\n" +
      message4, "\n" + message5)
