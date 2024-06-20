from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, marca, ano, preco, cilindradas):
        super().__init__(modelo, marca, ano, preco)
        self.cilindradas = cilindradas

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Tipo: Moto, Cilindradas: {self.cilindradas}")

    def calcular_desconto(self):
        return self.preco * 0.06  # Desconto de 6% para motos