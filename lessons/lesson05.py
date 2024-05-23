'''
Aula05 - Métodos Get e Set -> ter acesso às variáveis
encapsuladas

'''
class Conta():
    def __init__(self, parametro_nome, parametro_saldo = 0):
        self.var_nome = parametro_nome
        self.__var_saldo = parametro_saldo
    
    def getSaldo(self):
        return self.__var_saldo
    
    def setSaldo(self, parametro_saldo):
        if type(parametro_saldo) is int and parametro_saldo > 0:
            self.__var_saldo = parametro_saldo
        else:
            print("ERRO")    

conta1 = Conta('Hilda', 1000)
conta2 = Conta('Ana Paulo')     
conta3 = Conta('Beth')

conta1.setSaldo(7)

print(conta1.getSaldo())
print(conta2.getSaldo())
print(conta3.getSaldo())

conta1(conta1.setSaldo())        


