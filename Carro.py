from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, marca, ano, preco, num_portas):
        super().__init__(modelo, marca, ano, preco)
        self.numero_portas = num_portas

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Tipo: Carro, Número de Portas: {self.numero_portas}")

    def calcular_desconto(self):
        return self.preco * 0.08  # Desconto de 8% para carros