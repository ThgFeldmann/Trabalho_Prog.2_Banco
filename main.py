# Proposta de organizaçao do arquivo
# 'Pessoa: {pessoa}'
# 'Banco: {banco}'
# 'Conta: {conta}'
#TODO Futuramente, adicionar encapsulamento
#TODO Adicionar requisitos do projeto

class Banco:
    def __init__(self, nome, cnpj, numero):
        self.nome = nome
        self.cnpj = cnpj
        self.numero = numero
        
        # Lista de contas bancárias
        self.contas = []
    
    def Info_Banco(self):
        print("-"*15)
        print("Banco")
        print(f"Nome: {self.nome}")
        print(f"CNPJ: {self.cnpj}")
        print(f"Número: {self.numero}")
    
    def Info_Contas(self):
        print("-"*30)
        for conta in self.contas:
            conta.Info_Conta()
    
    def Fechar_Conta(self, numero_conta):
        print("-"*30)
        for conta in self.contas:
            if conta.numero == numero_conta:
                self.contas.remove(conta)

class Pessoa:
    def __init__(self, nome, sobrenome, idade, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf
        
        # Lista de contas bancárias
        self.contas = []
        
    def Info_Pessoa(self):
        print("-"*30)
        print("Pessoa")
        print(f"Nome: {self.nome}")
        print(f"Sobrenome: {self.sobrenome}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")
    
    def Info_Contas(self):
        for conta in self.contas:
            conta.Info_Conta()

class Conta_Bancaria:
    def __init__(self, titular: Pessoa, banco: Banco, numero, saldo, senha):
        self.titular = Pessoa(titular)
        self.banco = Banco(banco)
        self.numero = numero
        self.saldo = saldo
        self.senha = senha
    
    def Info(self):
        print(f"Titular: {self.titular.nome}")
        print(f"Banco: {self.banco.nome}")
        print(f"Número: {self.numero}")
        print(f"Saldo: {self.saldo:.2f}")
        print(f"Senha: {self.senha}")
    
    def Saque(self, other: float):
        self.saldo -= other
        print(f"Saque: R$ {other:.2f}")
        print(f"Saldo: {self.saldo}")
    
    def Deposito(self, other: float):
        self.saldo += other
        print(f"Depósito: ${other:.2f}")
        print(f"Saldo: {self.saldo}")
    
    def Verifica_Senha(self, other: str):
        if self.senha == other:
            return True
        else:
            return False

class Conta_Corrente(Conta_Bancaria):
    def __init__(self, titular, banco, numero, saldo, senha, taxa):
        super().__init__(titular, banco, numero, saldo, senha)
        self.taxa = taxa
    
    def Info_Conta(self):
        print("-"*15)
        print("Conta Corrente")
        super().Info()
        print(f"Taxa Mensal: R$ {self.taxa:.2f}")
    
    def Novo_Mes(self):
        self.saldo -= self.taxa
        print(f"Taxa Mensal: R$ {self.taxa:.2f}")
        print(f"Saldo: R$ {self.saldo:.2f}")

class Conta_Poupança(Conta_Bancaria):
    def __init__(self, titular, banco, numero, saldo, senha, rendimento, total_saques=3):
        super().__init__(titular, banco, numero, saldo, senha)
        self.rendimento = rendimento
        self.total_saques = total_saques
    
    def Info_Conta(self):
        print("-"*15)
        print("Conta Poupança")
        super().Info()
        print(f"Rendimento: {self.rendimento}%")
        print(f"Total de saques: {self.total_saques}")
    
    def Novo_Mes(self):
        self.saldo += (self.rendimento * self.saldo)
        print(f"Rendimento: {self.rendimento}%")
        print(f"Saldo: R$ {self.saldo:.2f}")
    
    def Saque(self, other):
        if self.total_saques <= 3 and self.total_saques > 0:
            super().Saque(other)
            self.total_saques -= 1
        
        else:
            print("-"*30)
            print("Não foi possível efetuar este saque.")
            print("Não há mais saques disponíveis.")


if __name__ == '__main__':