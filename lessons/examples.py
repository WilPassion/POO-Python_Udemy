'''
Aula05 - Métodos Get e Set

class Conta():
    def __init__(self, parametro_numero, parametro_saldo=0):
        self.var_numero = parametro_numero
        self.__var_saldo = parametro_saldo  # __var_saldo -> encapsulada

    def depositar(self, valor):
        if valor > 0:
            self.__var_saldo += valor
            return True
        else:
            return False

    def sacar(self, valor):
        if valor > 0 and valor <= self.__var_saldo:
            self.__var_saldo -= valor
            return True
        else:
            return False

    def conferirSaldo(self):
        return self.__var_saldo

# Testes
conta1 = Conta(123, 5500)

print("Saldo inicial:", conta1.conferirSaldo())

# Depositar
if conta1.depositar(2000):
    print("Depósito realizado com sucesso!")
else:
    print("Valor de depósito inválido.")

print("Saldo após depósito:", conta1.conferirSaldo())

# Sacar
if conta1.sacar(3000):
    print("Saque realizado com sucesso!")
else:
    print("Valor de saque inválido ou saldo insuficiente.")

print("Saldo após saque:", conta1.conferirSaldo())



class Conta():
    def __init__(self, parametro_numero, parametro_saldo=0):
        self.var_numero = parametro_numero
        self.__var_saldo = parametro_saldo  # __var_saldo -> encapsulada

    def depositar(self, valor):
        if valor > 0:
            self.__var_saldo += valor
            return True
        else:
            return False

    def sacar(self, valor):
        if valor > 0 and valor <= self.__var_saldo:
            self.__var_saldo -= valor
            return True
        else:
            return False

    def conferirSaldo(self):
        return self.__var_saldo


class ContaInterface():
    @staticmethod
    def mostrar_menu(conta):
        while True:
            print("\n### Menu ###")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Conferir Saldo")
            print("4. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                valor = float(input("Digite o valor a depositar: "))
                if conta.depositar(valor):
                    print("Depósito realizado com sucesso!")
                else:
                    print("Valor de depósito inválido.")

            elif opcao == "2":
                valor = float(input("Digite o valor a sacar: "))
                if conta.sacar(valor):
                    print("Saque realizado com sucesso!")
                else:
                    print("Valor de saque inválido ou saldo insuficiente.")

            elif opcao == "3":
                print("Saldo:", conta.conferirSaldo())

            elif opcao == "4":
                print("Saindo do menu.")
                break

            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

# Teste
conta1 = Conta(123, 5500)
ContaInterface.mostrar_menu(conta1)
'''


class Conta:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito de", valor, "realizado com sucesso.")
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque de", valor, "realizado com sucesso.")
        else:
            print("Saldo insuficiente para sacar", valor)

    def verificar_saldo(self):
        print("Saldo atual:", self.saldo)


class UsaConta:

    def main():
        minha_conta = Conta()

        while True:
            print("\nMenu de Opções:")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Verificar Saldo")
            print("4. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                valor = float(input("Digite o valor a depositar: "))
                minha_conta.depositar(valor)
            elif opcao == "2":
                valor = float(input("Digite o valor a sacar: "))
                minha_conta.sacar(valor)
            elif opcao == "3":
                minha_conta.verificar_saldo()
            elif opcao == "4":
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    UsaConta.main()

