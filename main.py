from Veiculo import Veiculo
from Carro import Carro
from Moto import Moto
from Cliente import Cliente
from Venda import Venda

cliente1 = Cliente("Maria", 50000)  #crédito de R$ 50.000
cliente2 = Cliente("João", 30000)   #crédito de R$ 30.000, insuficiente

veiculo1 = Veiculo("Fiesta", "Ford", 2020, 50000)
carro1 = Carro("Corolla", "Toyota", 2022, 90000, 4)   #adicionando veículos
moto1 = Moto("CG 125", "Honda", 2021, 15000, 125)     #moto

venda1 = Venda(cliente1, veiculo1, 45000)  # Venda abaixo do valor do veículo
venda2 = Venda(cliente2, carro1, 80000)    # Venda acima do valor do veículo
venda3 = Venda(cliente1, moto1, 12000)     # Venda de moto

venda1.exibir_detalhes_venda()
venda2.exibir_detalhes_venda()
venda3.exibir_detalhes_venda()

venda1.fechar_venda()
venda2.fechar_venda()
venda3.fechar_venda()

cliente1.listar_veiculos_comprados()
cliente2.listar_veiculos_comprados()