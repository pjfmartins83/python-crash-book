#Dúvida: argumentos posicionais e argumentos nomeados

def make_shirt(tamanho="L", mensagem="Eu amo Python"):
    print("Você escolheu uma camiseta " + tamanho.title() +
          " com a seguinte mengsagem: " + mensagem + ".")


make_shirt("m", "camiseta de teste")
