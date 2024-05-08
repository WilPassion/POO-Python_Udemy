'''
Aula03 - Método Construtor e Parâmetros 

class Pessoa(): #pessoa1 = Pessoa(pessoa1, 'Joao')
    def __init__(self, nome_parametro):
        self.nome = nome_parametro
    
    def saudacao(self):
        return "Olá, meu nome é " + self.nome
    
#teste
pessoa1 = Pessoa('Moiraine Aes Sedai')

print(pessoa1.saudacao())

'''
#PARAMETRO OPCIONAL
class Pessoa():
    def __init__(self, parametro_nome, opc1 = 0): #apos o primeiro parâmetro opcional, todos próximos deverão ser também
        self.variavel_nome = parametro_nome
        self.variavel_opc1 = opc1
        
    def saudacao(self):
        return "Opa! Meu nome é " + self.variavel_nome
    
pessoa1 = Pessoa('Michael Jackson')
pessoa2 = Pessoa('Harry Potter', 10)

#pessoa1.variavel_opc1 = pessoa1.saudacao()
#pessoa2.variavel_opc1 = pessoa2.saudacao()

print(pessoa1.variavel_opc1)
print(pessoa2.variavel_opc1)