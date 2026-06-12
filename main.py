# Proposta de organizaçao do arquivo .csv
# 'Pessoa,{pessoa}'
# 'Banco,{banco}'
# 'Conta Corrente,{conta}'
# 'Conta Poupança,{conta}'
#TODO Criar funções para saques e depósitos
#TODO Criar os métodos alternativos

#* Classes

class Banco:
    def __init__(self, nome, cnpj, numero):
        self._nome = nome
        self._cnpj = cnpj
        self._numero = numero
        
        # Lista de contas bancárias
        self._contas = []
    
    # Getters
    @property
    def nome(self):
        return self._nome
    
    @property
    def cnpj(self):
        return self._cnpj

    @property
    def numero(self):
        return self._numero

    @property
    def contas(self):
        return self._contas
    
    # Setters
    @nome.setter
    def nome(self, other):
        if other:
            self._nome = other
    
    @cnpj.setter
    def cnpj(self, other):
        if other:
            self._cnpj = other
    
    @numero.setter
    def numero(self, other):
        if other:
            self._numero = other
    
    @contas.setter
    def contas(self, other):
        if other:
            self._contas = other
    
    # Métodos
    @classmethod
    def Construtor_Banco_Teclado(cls):
        print("Digite o nome do Banco")
        nome = Entrada_De_Dado("")
        print("Digite o CNPJ do Banco")
        cnpj = Entrada_De_Dado("")
        print("Digite o número do Banco")
        numero = Entrada_De_Dado(0)
        
        nome = nome.title()
        
        return cls(nome, cnpj, numero)
    
    def Info_Banco(self):
        print("-"*15)
        print("Banco")
        print(f"Nome: {self._nome}")
        print(f"CNPJ: {self._cnpj}")
        print(f"Número: {self._numero}")
    
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
        self._idade = idade
        self._cpf = cpf
        
        # Lista de contas bancárias
        self._contas = []
    
    # Getters
    @property
    def idade(self):
        return self._idade
    
    @property
    def cpf(self):
        return self._cpf

    @property
    def contas(self):
        return self._contas
    
    # Setters
    @idade.setter
    def idade(self, other):
        if other:
            self._idade = other
    
    @cpf.setter
    def cpf(self, other):
        if other:
            self._cpf = other
    
    @contas.setter
    def contas(self, other):
        if other:
            self._contas = other
    
    # Métodos
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
        
        if cpf.isdigit:
            nome = nome.title()
            sobrenome = sobrenome.title
            return cls(nome, sobrenome, idade, cpf)
        else:
            print("-"*30)
            print("CPF não pode conter letras, tente novamente.")
            print("Por segurança, este cadastro foi cancelado.")
            Continuar()
    
    def Info_Pessoa(self):
        print("-"*30)
        print("Pessoa")
        print(f"Nome: {self.nome}")
        print(f"Sobrenome: {self.sobrenome}")
        print(f"Idade: {self._idade}")
        print(f"CPF: {self._cpf}")
    
    def Info_Contas(self):
        for conta in self.contas:
            conta.Info_Conta()
    
    def Adicionar_Conta(self, nova_conta):
        self.contas.append(nova_conta)

# Classe abstrata para as contas correntes e poupanças
class Conta_Bancaria:
    def __init__(self, titular: Pessoa, banco: Banco, numero, saldo, senha):
        self.__titular = titular
        self.__banco = banco
        self.__numero = numero
        self.__saldo = saldo
        self.__senha = senha

    # Getters

    @property
    def titular(self):
        return self.__titular
    
    @property
    def banco(self):
        return self.__banco
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def senha(self):
        return self.__senha
    
    # Setters
    
    @titular.setter
    def titular(self, other):
        if other:
            self.__titular = other
    
    @banco.setter
    def banco(self, other):
        if other:
            self.__banco = other
    
    @numero.setter
    def numero(self, other):
        if other:
            self.__numero = other
    
    @saldo.setter
    def saldo(self, other):
        if other:
            self.__saldo = other
    
    @senha.setter
    def senha(self, other):
        if other:
            self.__senha = other
    
    # Métodos
    
    def Info(self):
        print(f"Titular: {self.titular.nome}")
        print(f"Banco: {self.banco._numero}")
        print(f"Número: {self.numero}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print(f"Senha: {self.senha}")
    
    def Saque(self, other: float):
        resultado = self.saldo - other
        self.saldo = resultado
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
        self._taxa = taxa

    @property
    def taxa(self):
        return self._taxa
    
    @taxa.setter
    def taxa(self, other):
        if other:
            self._taxa = other

    @classmethod
    def Construtor_Conta_Corrente_Teclado(cls, sistema):
        # Flags para quando um valor correto for encontrado
        titular_ok = False
        banco_ok = False
        
        recebendo_valores = True

        while recebendo_valores:
            print("Digite o nome do Titular")
            nome_titular = Entrada_De_Dado("")
            try:
                for pessoa in sistema.pessoas:
                    if pessoa.nome == nome_titular:
                        titular = pessoa
                        titular_ok = True
                        recebendo_valores = False
                
                if not titular_ok:
                    print("-"*30)
                    print("Não foi encontrada nenhuma pessoa com este nome.")
                    print("Tente novamente.")
                    Continuar()
                    continue
            except Exception as error:
                print("-"*30)
                print("Não foi possível encontrar o titular.")
                print(f"Mensagem de erro: {error}")
                Continuar()
        
        recebendo_valores = True
        
        while recebendo_valores:
            print("Digite o número do Banco")
            numero_banco = Entrada_De_Dado(0)
            try:
                for banco in sistema.bancos:
                    if banco._numero == numero_banco:
                        banco_encontrado = banco
                        banco_ok = True
                        recebendo_valores = False
                
                if not banco_ok:
                    print("-"*30)
                    print("Não foi encontrado nenhum banco com esse número.")
                    print("Tente novamente.")
                    Continuar()
                    continue
            except Exception as error:
                print("-"*30)
                print("Não foi possível encontrar o banco.")
                print(f"Mensagem de erro: {error}")
                Continuar()
        
        print("Digite o número da Conta")
        numero_conta = Entrada_De_Dado(0)
        print("Digite o saldo da Conta")
        saldo = Entrada_De_Dado(0.00)
        print("Digite a senha da Conta")
        senha = Entrada_De_Dado("")
        print("Digite a taxa mensal da Conta")
        taxa = Entrada_De_Dado(0.00)
        
        if titular_ok and banco_ok:
            
            conta_existe = sistema.Verificar_Conta_Corrente_Existe(numero_conta)
            
            if not conta_existe:
                print("Cadastrando a conta...")
                return cls(titular, banco_encontrado, numero_conta, saldo, senha, taxa)
            else:
                print("-"*30)
                print("Não foi possível continuar com o cadastro.")
                print("Esta conta já existe no sistema.")
                Continuar()
        else:
            print("-"*30)
            print("Não foi possível continuar com o cadastro, faltaram valores.")
            Continuar()
    
    def Info_Conta(self):
        print("-"*15)
        print("Conta Corrente\n")
        super().Info()
        print(f"Taxa Mensal: R$ {self._taxa:.2f}")
    
    def Novo_Mes(self):
        self.saldo -= self.taxa
        print(f"Taxa Mensal: R$ {self._taxa:.2f}")
        print(f"Saldo: R$ {self.saldo:.2f}")

class Conta_Poupanca(Conta_Bancaria):
    def __init__(self, titular, banco, numero, saldo, senha, rendimento, total_saques=3):
        super().__init__(titular, banco, numero, saldo, senha)
        self._rendimento = rendimento
        self._total_saques = total_saques

    # Getters
    @property
    def rendimento(self):
        return self._rendimento
    
    @property
    def total_saques(self):
        return self._total_saques

    # Setters
    @rendimento.setter
    def rendimento(self, other):
        if other:
            self._rendimento = other
    
    @total_saques.setter
    def total_saques(self, other):
        if other:
            self._total_saques = other

    @classmethod
    def Construtor_Conta_Poupanca_Teclado(cls, sistema):
        # Flags para quando um valor correto for encontrado
        titular_ok = False
        banco_ok = False
        
        recebendo_valores = True

        while recebendo_valores:
            print("Digite o nome do Titular")
            nome_titular = Entrada_De_Dado("")
            try:
                for pessoa in sistema.pessoas:
                    if pessoa.nome == nome_titular:
                        titular = pessoa
                        titular_ok = True
                        recebendo_valores = False
                
                if not titular_ok:
                    print("-"*30)
                    print("Não foi encontrada nenhuma pessoa com este nome.")
                    print("Tente novamente.")
                    Continuar()
                    continue
            except Exception as error:
                print("-"*30)
                print("Não foi possível encontrar o titular.")
                print(f"Mensagem de erro: {error}")
                Continuar()
        
        recebendo_valores = True
        
        while recebendo_valores:
            print("Digite o número do Banco")
            numero_banco = Entrada_De_Dado(0)
            try:
                for banco in sistema.bancos:
                    if banco._numero == numero_banco:
                        banco_encontrado = banco
                        banco_ok = True
                        recebendo_valores = False
                
                if not banco_ok:
                    print("-"*30)
                    print("Não foi encontrado nenhum banco com esse número.")
                    print("Tente novamente.")
                    Continuar()
                    continue
            except Exception as error:
                print("-"*30)
                print("Não foi possível encontrar o banco.")
                print(f"Mensagem de erro: {error}")
                Continuar()
        
        print("Digite o número da Conta")
        numero_conta = Entrada_De_Dado(0)
        print("Digite o saldo da Conta")
        saldo = Entrada_De_Dado(0.00)
        print("Digite a senha da Conta")
        senha = Entrada_De_Dado("")
        print("Digite o rendimento da Conta")
        rendimento = Entrada_De_Dado(0.00)
        
        if titular_ok and banco_ok:
            
            conta_existe = sistema.Verificar_Conta_Poupanca_Existe(numero_conta)
            
            if not conta_existe:
                print("Cadastrando a conta...")
                return cls(titular, banco_encontrado, numero_conta, saldo, senha, rendimento)
            else:
                print("-"*30)
                print("Não foi possível continuar com o cadastro.")
                print("Esta conta já existe no sistema.")
        
        else:
            print("-"*30)
            print("Não foi possível continuar com o cadastro, faltaram valores.")
            Continuar()
    
    def Info_Conta(self):
        print("-"*15)
        print("Conta Poupança\n")
        super().Info()
        print(f"Rendimento: {self._rendimento}%")
        print(f"Total de saques: {self._total_saques}")
    
    def Novo_Mes(self):
        self._saldo += (self._rendimento * self._saldo)
        self.total_saques = 3
        print(f"Rendimento: {self._rendimento}%")
        print(f"Saldo: R$ {self._saldo:.2f}")
        print(f"Total de saques: {self.total_saques}")
    
    def Saque(self, other):
        if self.total_saques <= 3 and self.total_saques > 0:
            super().Saque(other)
            self.total_saques -= 1
        
        else:
            print("-"*30)
            print("Não foi possível efetuar este saque.")
            print("Não há mais saques disponíveis.")

# Classe para armazenamento e gerenciamento de dados em geral
class Sistema:
    def __init__(self):
        self.bancos = []
        self.pessoas = []
        self.contas_correntes = []
        self.contas_poupancas = []
    
    # Métodos de adição de dados
    
    def Adicionar_Banco(self, novo_banco: Banco):
        self.bancos.append(novo_banco)
    
    def Adicionar_Pessoa(self, nova_pessoa: Pessoa):
        self.pessoas.append(nova_pessoa)
    
    def Adicionar_Conta_Corrente(self, nova_conta: Conta_Corrente):
        self.contas_correntes.append(nova_conta)
    
    def Adicionar_Conta_Poupanca(self, nova_conta: Conta_Poupanca):
        self.contas_poupancas.append(nova_conta)
    
    # Métodos de busca de dados
    
    def Busca_Banco_Por_Nome(self, nome_inserido):
        for banco in self.bancos:
            if banco._nome == nome_inserido:
                return banco
    
    def Busca_Pessoa_Por_Nome(self, nome_inserido):
        for pessoa in self.pessoas:
            if pessoa.nome == nome_inserido:
                return pessoa
                
    def Busca_Conta_Corrente_Por_Numero(self, numero_inserido):
        for conta_corrente in self.contas_correntes:
            if conta_corrente.numero == numero_inserido:
                return conta_corrente
    
    # Método para verificar se uma conta poupança já existe no sistema
    # retorna um 'booleano'
    def Busca_Conta_Poupanca_Por_Numero(self, numero_inserido):
        for conta_poupanca in self.contas_poupancas:
            if conta_poupanca.numero == numero_inserido:
                return conta_poupanca

    # Método para verificar se uma conta corrente já existe no sistema
    # retorna um 'booleano'
    def Verificar_Conta_Corrente_Existe(self, numero_inserido):
        for conta in self.contas_correntes:
            if conta.numero == numero_inserido:
                return True
    
    # Método para verificar se uma conta poupança já existe no sistema
    # retorna um 'booleano'
    def Verificar_Conta_Poupanca_Existe(self, numero_inserido):
        for conta in self.contas_poupancas:
            if conta.numero == numero_inserido:
                return True

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
                entrada = float(entrada.replace(",", "."))
                
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

def Cadastro_Conta(sistema):
    if len(sistema.pessoas) <= 0:
        print("-"*30)
        print("Não existem pessoas salvas no sistema.")
        print("Saindo...")
        Continuar()
        return False
    elif len(sistema.bancos) <= 0:
        print("-"*30)
        print("Não existem bancos salvos no sistema.")
        print("Saindo...")
        Continuar()
        return False
    else:
        running = True

        while running:
            print("Qual tipo deseja cadastrar?")
            print("1 - Corrente")
            print("2 - Poupança")
            print("0 - Sair")
            
            try:
                escolha = int(input(": "))
                
                if escolha < 0:
                    raise ValueError
                elif escolha == 1:
                    print("-"*30)
                    conta = Conta_Corrente.Construtor_Conta_Corrente_Teclado(sistema)
                    
                    try:
                        sistema.Adicionar_Conta_Corrente(conta)
                        running = False
                        return True
                    except Exception as error:
                        print("-"*30)
                        print("Ocorreu um erro inesperado durante o cadastro, tente novamente.")
                        Continuar()
                        continue
                    
                elif escolha == 2:
                    print("-"*30)
                    print("-"*30)
                    conta = Conta_Poupanca.Construtor_Conta_Poupanca_Teclado(sistema)
                    
                    try:
                        sistema.Adicionar_Conta_Poupanca(conta)
                        running = False
                        return True
                    except Exception as error:
                        print("-"*30)
                        print("Ocorreu um erro inesperado durante o cadastro, tente novamente.")
                        Continuar()
                        continue

                elif escolha == 0:
                    print("-"*30)
                    print("Encerrando a execução...")
                    Continuar()
                    running = False
                    return False
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

def Sacar(sistema, conta):
    running = True

    while running:
        print(f"Saldo: {conta.saldo}")
        
        print("\nDigite o valor do saque")
        valor = Entrada_De_Dado(0.00)
        
        if valor <= 0:
            print("-"*30)
            print("O valor do saque deve ser positivo.")
            Continuar()
            continue
        else:
            print("Sacando...\n")
            conta.Saque(valor)

# Função que verifica se uma conta existe, e pede a senha, se válida, realiza a função de saque
def Verifica_Senha(sistema):
    running = True

    while running:
        print("-"*30)
        print("Saque de uma conta poupança\n")
        
        try:
            print("Digite o número da conta")
            numero_conta = Entrada_De_Dado(0)
            
            conta = sistema.Busca_Conta_Poupanca_Por_Numero(numero_conta)
            
            if not conta:
                print("-"*30)
                print("Não existe uma conta com este número no sistema, tente novamente.")
                Continuar()
                continue
            else:
                verificando_senha = True
                
                while verificando_senha:
                    print("\nDigite a senha da conta")
                    senha_inserida = Entrada_De_Dado("")
                    
                    senha_valida = conta.Verifica_Senha(senha_inserida)
                    
                    if not senha_valida:
                        print("-"*30)
                        print("Senha inválida, tente novamente.")
                        Continuar()
                        continue
                    else:
                        print("-"*30)
                        print("Senha correta, continuando com o saque...\n")
                        Sacar(sistema, conta)
                        verificando_senha = False
                        running = False
        except ValueError:
            print("-"*30)
            print("O número da conta deve conter apenas números positivos")
            Continuar()
            continue
        except Exception as error:
            print("-"*30)
            print("Ocorreu um erro inesperado, tente novamente.")
            print(f"Mensagem de erro: {error}")
            Continuar()
            continue

def Escolher_Tipo_Conta(sistema):
    running = True
    
    while running:
        print("-"*30)
        print("Informe o tipo da conta")
        print("1 - Corrente")
        print("2 - Poupança")
        
        try:
            print()
            escolha = Entrada_De_Dado(0)
            
            if escolha <= 0:
                raise ValueError
            elif escolha == 1:
                running = False
                return "corrente"
            elif escolha == 2:
                running = False
                return "poupanca"
            else:
                print("-"*30)
                print("Opção inválida, tente novamente.")
                Continuar()
                continue
            
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

# Função para o menu de cadastros
def Menu_Cadastro(sistema):
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

                try:
                    sistema.Adicionar_Banco(banco)
                    print("Banco cadastrado com sucesso.")
                    Continuar()
                    running = False
                except Exception as error:
                    print("-"*30)
                    print("Ocorreu um erro inesperado, tente novamente.")
                    print(f"Mensagem de erro: {error}")
                    Continuar()
                    continue
            elif escolha == 2:
                print("-"*30)
                pessoa = Pessoa.Construtor_Pessoa_Teclado()

                try:
                    sistema.Adicionar_Pessoa(pessoa)
                    print("Pessoa cadastrada com sucesso.")
                    Continuar()
                    running = False
                except Exception as error:
                    print("-"*30)
                    print("Ocorreu um erro inesperado, tente novamente.")
                    print(f"Mensagem de erro: {error}")
                    Continuar()
                    continue
            elif escolha == 3:
                print("-"*30)
                sucesso = Cadastro_Conta(sistema)
                if sucesso:
                    print("-"*30)
                    print("Conta cadastrada com sucesso.")
                    Continuar()
                    running = False
                else:
                    print("-"*30)
                    print("O cadastro foi cancelado.")
                    Continuar()
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
def Menu_Info(sistema):
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
            
            if escolha < 0: # Entrada inválida
                raise ValueError
            elif escolha == 1: # Banco
                print("-"*30)
                try:
                    print("Digite o nome do banco")
                    nome_banco = Entrada_De_Dado("")
                    banco = sistema.Busca_Banco_Por_Nome(nome_banco)
                    
                    if not banco:
                        print("-"*30)
                        print("Este banco não existe no sistema.")
                        print("Cancelando a busca...")
                        Continuar()
                    else: 
                        banco.Info_Banco()
                        quantidade_contas = len(banco.contas)
                        
                        if quantidade_contas <= 0:
                            print("Este banco não possui contas cadastradas.")
                        elif quantidade_contas == 1:
                            print(f"Este banco possui: {quantidade_contas} conta")
                        else:
                            print(f"Este banco possui: {quantidade_contas} contas.")

                        Continuar()
                        running = False
                except Exception as error:
                    print("-"*30)
                    print("Ocorreu um erro inesperado, tente novamente.")
                    print(f"Mensagem de erro: {error}")
                    Continuar()
                    continue
            elif escolha == 2: # Pessoa
                print("-"*30)
                try:
                    print("Digite o nome da pessoa")
                    nome_pessoa = Entrada_De_Dado("")
                    pessoa = sistema.Busca_Pessoa_Por_Nome(nome_pessoa)
                    
                    if not pessoa:
                        print("-"*30)
                        print("Esta pessoa não existe no sistema.")
                        print("Cancelando a busca...")
                        Continuar()
                    else: 
                        pessoa.Info_Pessoa()
                        quantidade_contas = len(pessoa.contas)
                        
                        if quantidade_contas <= 0:
                            print("Esta pessoa não possui contas cadastradas.")
                        elif quantidade_contas == 1:
                            print(f"Esta pessoa possui: {quantidade_contas} conta")
                        else:
                            print(f"Esta pessoa possui: {quantidade_contas} contas.")

                        Continuar()
                        running = False
                except Exception as error:
                    print("-"*30)
                    print("Ocorreu um erro inesperado, tente novamente.")
                    print(f"Mensagem de erro: {error}")
                    Continuar()
                    continue
            elif escolha == 3: # Conta
                tipo = Escolher_Tipo_Conta(sistema)
                
                print("-"*30)
                try:
                    print("Digite o número da conta")
                    numero_conta = Entrada_De_Dado(0)
                    
                    if tipo == "corrente":
                        conta = sistema.Busca_Conta_Corrente_Por_Numero(numero_conta)
                    elif tipo == "poupanca":
                        conta = sistema.Busca_Conta_Poupanca_Por_Numero(numero_conta)
                    
                    if not conta:
                        print("-"*30)
                        print("Esta conta não existe no sistema.")
                        print("Cancelando a busca...")
                        Continuar()
                    else: 
                        conta.Info_Conta()
                        Continuar()
                        running = False
                except Exception as error:
                    print("-"*30)
                    print("Ocorreu um erro inesperado, tente novamente.")
                    print(f"Mensagem de erro: {error}")
                    Continuar()
                    continue
            elif escolha == 0: # Sair
                print("-"*30)
                print("Encerrando a execução...")
                Continuar()
                running = False
            else: # Opção inválida
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

# Função de teste | Será removida
def test(sistema):
    
    banco = Banco("banco", "123456", 123)
    pessoa = Pessoa("fulano", "Fulano", 23, "0123456")
    conta_corrente = Conta_Corrente(pessoa, banco, 456, 700, "456", 50)
    conta_poupanca = Conta_Poupanca(pessoa, banco, 789, 500, "789", 25)
    
    sistema.Adicionar_Banco(banco)
    sistema.Adicionar_Pessoa(pessoa)
    sistema.Adicionar_Conta_Corrente(conta_corrente)
    sistema.Adicionar_Conta_Poupanca(conta_poupanca)
    
    print()
    # conta_corrente.Info_Conta()
    # conta_poupanca.Info_Conta()
    
    # print()
    # conta_poupanca.Saque(100)

#* Interface

if __name__ == '__main__':
    # objeto para o armazenamento e gerenciamento dos dados
    sistema = Sistema()
    
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
        print("5 - Cobrar taxa de uma conta")
        print("0 - Sair")

        try:
            escolha = int(input("\n: "))
            
            if escolha == 10: # Função de teste
                test(sistema)
                Continuar()
            
            elif escolha < 0:
                raise ValueError
            elif escolha == 1:
                Menu_Cadastro(sistema)
            elif escolha == 2:
                Menu_Info(sistema)
            elif escolha == 3:
                Verifica_Senha(sistema)
            
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