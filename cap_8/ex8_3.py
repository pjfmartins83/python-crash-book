def make_shirt(tamanho, mensagem):
    print("Você escolheu uma camiseta " + tamanho.title() +
          " com a seguinte mengsagem: " + mensagem + ".")


make_shirt("m", "camiseta de teste")
make_shirt(mensagem="camiseta de teste", tamanho="M")
