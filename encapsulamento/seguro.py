# Em Python não é possível encapsular atributos de classe, então é usada uma convenção para protege-los
# encapsulamento: esconder detalhes internos da classe (propriedades e metódos),
# restringindo o acesso a partir de outras partes do código

# 1 anderline antes significa que o autor não quer que o atributo seja alterado
# 2 anderlines antes significam que não se deve, de jeito nenhum, alterar o método.
# "caso contrário você será execrado da comunidade python" - GUEDES, Gabriela

class Cliente:

    def __init__(self, nome, saldo, divida):
        self.__nome = nome
        self.__saldo = saldo
        self.__divida = divida

joao = Cliente("joão", 10.00, 150.00)
maria = Cliente("maria", 1000.00, 0.00)
pedro = Cliente("pedro", 0.00, 200000.00)

joao.saldo = 1000
joao.divida = 0
print(joao.saldo, joao.divida)

maria.saldo = 0
maria.divida = 100000
print(maria.saldo, maria.divida)

# Erro, pois não existe atributo __saldo
#print(joao._saldo)

# Acessando atributo privada
print(joao._Cliente_saldo)

# burlando encapsulamento
joao._Cliente_saldo =1000
print(joao._Cliente_saldo)