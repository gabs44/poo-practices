class Pessoa:

    def __init__(self, nome, etnia, cpf, altura, genero, cor_dos_olhos):
        self.__nome = nome
        self.__etnia = etnia
        self.__cpf = cpf
        self.__altura
        self.__genero
        self.__cor_dos_olhos

    # getters: são métodos responsáveis por consultar os valores dos atributos
    def get_nome(self):
        return self.__nome
    
    def get_etnia(self):
        return self.__etnia
    
    def get_cpf(self):
        return self.__cpf
    
    def get_altura(self):
        return self.__altura
    
    def get_genero(self):
        return self.__genero
    
    def get_cor_dos_olhos(self):
        return self.__cor_dos_olhos

    # Setters são métodos das classes responsáveis por alterar valores de atributos
    # geralmente só são feitos setters para atributos que podem sofrer mudanças
    def set_nome(self,nome):
        self.__nome= nome

    def set_altura(self,altura):
        if altura <= 0:
            return False
        self.altura = altura

    def set_genero(self,genero):
        self.__genero = genero

ricart = Pessoa("Antônio Ricart Jacinto de Oliveira Medeiros", "branco", 705.207.724.82, 1.79, "masculino", "castanho")
ricart.set_altura(1.80)
print(ricart.get_nome())