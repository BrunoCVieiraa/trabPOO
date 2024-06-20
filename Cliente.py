class Cliente:
    def __init__(self, nome, credito):
        self.nome = nome
        self.credito = credito
        self.veiculos_comprados = []

    def verificar_credito(self, valor_compra):
        return self.credito >= valor_compra

    def comprar_veiculo(self, veiculo):
        self.veiculos_comprados.append(veiculo)

    def listar_veiculos_comprados(self):
        print(f"Veículos comprados por {self.nome}:")
        for veiculo in self.veiculos_comprados:
            veiculo.exibir_dados()