class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3
        self.LIMITE_MAX_SAQUE = 500

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R${valor:.2f}")
            print(f"R${valor:.2f} depositados com sucesso!")
        else:
            print("O valor de depósito tem que ser positivo!")

    def saque(self, valor):
        if self.numero_saques >= self.LIMITE_SAQUES:
            print("Você atingiu o limite de saques diários.")
        elif valor > self.LIMITE_MAX_SAQUE:
            print("O valor de saque excede o limite máximo de R$ 500,00.")
        elif self.saldo < valor:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R${valor:.2f}")
            self.numero_saques += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso!")

    def exibir_extrato(self):
        print("Extrato da conta:")
        for operacao in self.extrato:
            print(operacao)
        print(f"Saldo atual: R${self.saldo:.2f}")





# Instancia a classe ContaBancaria
conta = ContaBancaria()

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True: 
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor para depósito: "))
        conta.depositar(valor)

    elif opcao == "s":
        print("Sacar")
        
    elif opcao == "e":
        conta.exibir_extrato()
        
    elif opcao == "q": 
        print("Saindo...")
        break 
        
    else:
        print("Opção inválida, tente novamente!")   