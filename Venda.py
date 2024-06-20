from Cliente import Cliente
from Veiculo import Veiculo

class Venda:
    def __init__(self, cliente, veiculo, valor_venda):
        self.cliente = cliente
        self.veiculo = veiculo
        self.valor_venda = valor_venda
    
    def fechar_venda(self):
        if self.cliente.verificar_credito(self.valor_venda):
            self.cliente.comprar_veiculo(self.veiculo)
            print(f"Venda realizada para o cliente {self.cliente.nome}")
        else:
            print(f"Cliente {self.cliente.nome} não possui crédito suficiente.")

    def exibir_detalhes_venda(self):
        print("Detalhes da Venda:")
        print(f"Cliente: {self.cliente.nome}")
        print("Veículo:")
        self.veiculo.exibir_dados()
        print(f"Valor da Venda: R${self.valor_venda}")