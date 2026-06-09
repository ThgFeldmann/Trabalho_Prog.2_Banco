# Proposta de organizaçao do arquivo
# 'Pessoa: {pessoa}'
# 'Banco: {banco}'
# 'Conta: {conta}'
#TODO Futuramente, adicionar encapsulamento
#TODO Métodos construtores com input

#* Classes

class Banco:
    def __init__(self, nome, cnpj, numero):
        self.nome = nome
        self.cnpj = cnpj
        self.numero = numero
        
        # Lista de contas bancárias
        self.contas = []
    
    @classmethod
    def Construtor_Banco_Teclado(cls):
        print("Digite o nome do Banco")
        nome = Entrada_De_Dado("")
        print("Digite o CNPJ do Banco")
        cnpj = Entrada_De_Dado("")
        print("Digite o número do Banco")
        numero = Entrada_De_Dado(0)
        
        return cls(nome, cnpj, numero)
    
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
    
    def Adicionar_Conta(self, nova_conta):
        self.contas.append(nova_conta)
    
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
    
    @classmethod
    def Construtor_Pessoa_Teclado(cls):
        print("Digite o primeiro nome da Pessoa")
        nome = Entrada_De_Dado("")
        print("Digite o sobrenome da Pessoa")
        sobrenome = Entrada_De_Dado("")
        print("Digite a idade da Pessoa")
        idade = Entrada_De_Dado(0)
        print("Digite o CPF da Pessoa")
        cpf = Entrada_De_Dado("")

        return cls(nome, sobrenome, idade, cpf)
    
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
    
    def Adicionar_Conta(self, nova_conta):
        self.contas.append(nova_conta)

class Conta_Bancaria:
    def __init__(self, titular: Pessoa, banco: Banco, numero, saldo, senha):
        self.titular = Pessoa(titular)
        self.banco = Banco(banco)
        self.numero = numero
        self.saldo = saldo
        self.senha = senha
    
    #TODO Em desenvolvimento
    @classmethod
    def Construtor_Conta_Bancaria_Teclado(cls):
        print("Digite o nome do Titular")
        nome_titular = Entrada_De_Dado("")
        print("Digite o número do Banco")
        numero_banco = Entrada_De_Dado(0)
        print("Digite o número da Conta")
        numero_conta = Entrada_De_Dado(0)
        print("Digite o saldo da Conta")
        saldo = Entrada_De_Dado(0.00)
        print("Digite a senha da Conta")
        senha = Entrada_De_Dado("")
        
        #TODO Criar verificações / extrair o titular e o banco
        
        return cls(titular, banco, numero_conta, saldo, senha)
    
    def Info(self):
        print(f"Titular: {self.titular.nome}")
        print(f"Banco: {self.numero_banco.nome}")
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

#* Funções

# Função para a entrada de um dado
# recebe um tipo | retorna um dado equivalente ao tipo inserido
def Entrada_De_Dado(tipo):
    running = True

    while running:
        entrada = input(": ")
        
        if entrada == "" or entrada == None or entrada == " " or len(entrada) <= 0:
            print("-"*30)
            print("A entrada não pode ser vazia.")
            print("Insira algum valor e tente novamente.")
            Continuar()
            continue
        
        elif type(tipo) == str: #* Se o tipo da entrada for de 'string'
            try:
                entrada = str(entrada.strip())
                
                running = False
                return entrada
            except ValueError:
                print("-"*30)
                print("A entrada não pôde ser alterada para texto.")
                Continuar()
                continue
            except Exception as error:
                print("-"*30)
                print("Ocorreu um erro inesperado, tente novamente.")
                Continuar()
                continue
        
        elif type(tipo) == float: #* Se o tipo da entrada for de 'float'
            try:
                entrada = float(entrada.replace(",", ".").strip())
                
                if entrada <= 0:
                    print("-"*30)
                    print("A entrada não pode ser menor ou igual à zero(0).")
                    print("Tente novamente.")
                    Continuar()
                    continue
                else:
                    running = False
                    return entrada

            except ValueError:
                print("-"*30)
                print("A entrada deve conter apenas números")
                Continuar()
                continue
            except Exception as error:
                print("-"*30)
                print("Ocorreu um erro inesperado, tente novamente.")
                Continuar()
                continue
        
        elif type(tipo) == int: #* Se o tipo da entrada for de 'int'
            try:
                entrada = int(entrada.strip())
                
                if entrada <= 0:
                    print("-"*30)
                    print("A entrada não pode ser menor ou igual à zero(0).")
                    print("Tente novamente.")
                    Continuar()
                    continue
                else:
                    running = False
                    return entrada
            
            except ValueError:
                print("-"*30)
                print("A entrada deve conter apenas números")
                Continuar()
                continue
            except Exception as error:
                print("-"*30)
                print("Ocorreu um erro inesperado, tente novamente.")
                Continuar()
                continue
        else:
            running = False

# Função para o menu de cadastros
def Menu_Cadastro():
    running = True

    while running:
        print("-"*30)
        print("Menu de Cadastro")
        print("\nDigite a opção desejada")
        print("1 - Cadastro de Banco")
        print("2 - Cadastro de Pessoa")
        print("3 - Cadastro de Conta")
        print("0 - Sair")
        
        try:
            escolha = int(input("\n: "))
            
            if escolha < 0:
                raise ValueError
            elif escolha == 1:
                print("-"*30)
                banco = Banco.Construtor_Banco_Teclado()
                #Cadastro_Banco()
                running = False
            elif escolha == 2:
                print("-"*30)
                #Cadastro_Pessoa()
                running = False
            elif escolha == 3:
                print("-"*30)
                #Cadastro_Conta()
                running = False
            elif escolha == 0:
                print("-"*30)
                print("Encerrando a execução...")
                Continuar()
                running = False
            else:
                print("-"*30)
                print("Opção inválida, tente novamente.")
                Continuar()

        except ValueError:
            print("-"*30)
            print("A entrada deve conter apenas números positivos")
            Continuar()
            continue
        except Exception as error:
            print("-"*30)
            print("Ocorreu um erro inesperado, tente novamente.")
            print(f"Mensagem de erro: {error}")
            Continuar()
            continue

# Função para o menu de informações
def Menu_Info():
    running = True

    while running:
        print("-"*30)
        print("Menu de Informações")
        print("\nDigite a opção desejada")
        print("1 - Informações de Banco")
        print("2 - Informações de Pessoa")
        print("3 - Informações de Conta")
        print("0 - Sair")
        
        try:
            escolha = int(input("\n: "))
            
            if escolha < 0:
                raise ValueError
            elif escolha == 1:
                print("-"*30)
                Info_Banco()
                running = False
            elif escolha == 2:
                print("-"*30)
                Info_Pessoa()
                running = False
            elif escolha == 3:
                print("-"*30)
                Info_Conta()
                running = False
            elif escolha == 0:
                print("-"*30)
                print("Encerrando a execução...")
                Continuar()
                running = False
            else:
                print("-"*30)
                print("Opção inválida, tente novamente.")
                Continuar()

        except ValueError:
            print("-"*30)
            print("A entrada deve conter apenas números positivos")
            Continuar()
            continue
        except Exception as error:
            print("-"*30)
            print("Ocorreu um erro inesperado, tente novamente.")
            print(f"Mensagem de erro: {error}")
            Continuar()
            continue

def Continuar():
    print("-"*30)
    input("Continuar...")
    print()

#* Interface

if __name__ == '__main__':
    #TODO Criar uma lista que irá conter todas as informações do sistema
    #? Ou uma Classe?
    
    running = True

    while running:
        print("-"*30)
        print("\tSistema Bancário")
        print("-"*30)
        print("\nDigite a opção desejada:")
        print("1 - Cadastro")
        print("2 - Informações")
        print("3 - Sacar de uma conta")
        print("4 - Depositar em uma conta")
        print("5 - Novo mês")
        print("0 - Sair")

        try:
            escolha = int(input("\n: "))
            
            if escolha < 0:
                raise ValueError
            elif escolha == 1:
                Menu_Cadastro()
            elif escolha == 2:
                Menu_Info()
            elif escolha == 0:
                print("-"*30)
                print("Encerrando a execução...")
                Continuar()
                running = False
            else:
                print("-"*30)
                print("Opção inválida, tente novamente.")
                Continuar()

        except ValueError:
            print("-"*30)
            print("A entrada deve conter apenas números positivos")
            Continuar()
            continue
        except Exception as error:
            print("-"*30)
            print("Ocorreu um erro inesperado, tente novamente.")
            print(f"Mensagem de erro: {error}")
            Continuar()
            continue