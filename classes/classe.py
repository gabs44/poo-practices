class Casa:

    def __init__(self, endereco="desconhecido"):
        self.endereco = endereco

    def __str__(self):
        return "O endereço dessa casa é: {}" .format(self.endereco)


bbb = Casa()
print(bbb.endereco)

mansao_foster = Casa("Cartoon Network")
print(mansao_foster)