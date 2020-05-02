class Cliente:

    def __init__(self, nome, saldo, divida):
        self.nome = nome
        self.saldo = saldo
        self.divida = divida
    

joao = Cliente("joão", 10.00, 150.00)
maria = Cliente("maria", 1000.00, 0.00)
pedro = Cliente("pedro", 0.00, 200000.00)

# exemplo de insegurança por acesso direto de atributo
joao.saldo = 1000
joao.divida = 0
print(joao.saldo, joao.divida)

maria.saldo = 0
maria.divida = 100000
print(maria.saldo, maria.divida)




