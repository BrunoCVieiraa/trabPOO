class Veiculo:
    def __init__(self, modelo, marca, ano, preco):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.preco = preco

    def exibir_dados(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Preço: R${self.preco}")

    def calcular_desconto(self):
        return self.preco * 0.05  # Desconto padrão de 5%