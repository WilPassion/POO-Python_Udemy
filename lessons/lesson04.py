'''
Aula04 - Encapsulamento - Possibilidade de esconder algumas métodos/variáveis do mundo externo,
podendo apenas serem acessados pela Classe

ANOTAÇÕES - IMPRIMIR TITULAR E CONTA CRIANDO METODO -> def informacoesConta(self):
class Conta():
    def __init__(self, parametro_nome_titular, parametro_saldo=0):
        self.var_nome_titular = parametro_nome_titular
        self.__var_saldo = parametro_saldo

    def retornaSaldo(self):
        return self.__var_saldo

    def informacoesConta(self):
        return f"Titular: {self.var_nome_titular}, Saldo: {self.__var_saldo}"

#teste
conta1 = Conta('William', 5500)
print(conta1.informacoesConta())

'''
class Conta():
    def __init__(self, parametro_nome_titular, parametro_saldo = 0):
        self.var_nome_titular = parametro_nome_titular
        self.__var_saldo = parametro_saldo #__var_saldo -> encapsulada

    def retornaSaldo(self):
        return self.__var_saldo

#testes
conta1 = Conta('William', 5500)

print(conta1.retornaSaldo())
#print(conta1.__saldo) --> Não roda/sem acesso ao saldo na classe - Precisa de um método para fazer a chamada

