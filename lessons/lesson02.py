'''
Aula02 - Métodos e Self

'''
class Pessoa():
    nome = ''
    
    #definindo método Saudação dentro da classe
    def saudacao(self): 
        return "Olá, meu nome é " + self.nome #self(objeto)
    
pessoa1 = Pessoa()
pessoa2 = Pessoa()

pessoa1.nome = 'Lord Voldemort'
pessoa2.nome = 'Draco Malfoy'

print(pessoa1.saudacao())
print(pessoa2.saudacao())

