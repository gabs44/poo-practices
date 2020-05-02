class Pessoa:

    def __init__ (self, nome, etnia, altura, peso, idade, cor_dos_olhos,
     genero, cpf):
     self.nome = nome
     self.etnia = etnia
     self.altura = altura
     self.peso = peso
     self.idade = idade
     self.cor_dos_olhos = cor_dos_olhos
     self.genero = genero
     self.cpf = cpf

    def __str__(self):
        return f"Nome: {self.nome} \n" \
            f"etnia: {self.etnia} \n" \
            f"altura: {self.altura} \n" \
            f"peso: {self.peso} \n" \
            f"idade: {self.idade} \n" \
            f"cor dos olhos: {self.cor_dos_olhos} \n" \
            f"genero: {self.genero} \n" \
            f"cpf: {self.cpf} \n" 


ricart = Pessoa("Antônio Ricart Jacinto de Oliveira Medeiros" , "branco", 1.79, 90, 20, "castanhos", "masculino", "705.207.724-82")
print(ricart)
  