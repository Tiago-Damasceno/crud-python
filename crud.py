class ControleRemoto:
    def __init__(self, cor, altura, largura, profundidade) -> None:
        self.cor = cor
        self.altura = altura
        self.largura = largura
        self.profundidade = profundidade


controleremoto = ControleRemoto('azul', '10cm', '2cm', '2cm')
print(controleremoto.cor)

controle_remoto = ControleRemoto('preto', '3cm', '5cm', '3cm')
print(controle_remoto.cor)

