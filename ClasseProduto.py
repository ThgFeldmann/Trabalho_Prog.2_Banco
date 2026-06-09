class Produto:
    def __init__(self, nome, tipo, valor, estoque):
        self.nome = nome
        self.tipo = tipo
        self.valor = valor
        self.estoque = estoque

    @classmethod
    def ConstrutorViaTeclado(cls):
        nome = input("Qual nome do produto?")
        tipo = input("Qual tipo do produto?")
        valor = float(input("Qual valor do produto?"))
        estoque = int(input("Qual estoque do produto?"))

        return cls(nome,tipo,valor,estoque)

    @classmethod
    def construtorViaCSV(cls, dadosDeProduto):
        nome = dadosDeProduto[0]
        tipo = dadosDeProduto[1]
        valor = float(dadosDeProduto[2])
        estoque = int(dadosDeProduto[3].replace("\n", ""))
        return cls(nome, tipo, valor, estoque)

    def info(self):
        print("Informações de produto")
        print(f"{self.tipo} - {self.nome}")
        print(f"R${self.valor}")
        print(f"Estoque: {self.estoque}")


if __name__ == '__main__':
    prod1 = Produto("Coca-cola","Refrigerante", 9.98, 3000)
    prod1.info()
    prod2 = Produto.ConstrutorViaTeclado()



