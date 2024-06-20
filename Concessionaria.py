class Concessionaria:
    def __init__(self, nome):
        self.nome = nome
        self.estoque = []

    def adicionar_veiculo(self, veiculo):
        self.estoque.append(veiculo)

    def listar_estoque(self):
        print(f"Estoque da concessionária {self.nome}:")
        for veiculo in self.estoque:
            veiculo.exibir_dados()

    def vender_veiculo(self, veiculo, cliente):
        if veiculo in self.estoque:
            self.estoque.remove(veiculo)
            cliente.comprar_veiculo(veiculo)
            print(f"Veículo vendido para o cliente {cliente.nome}")
        else:
            print("Veículo não encontrado no estoque da concessionária.")