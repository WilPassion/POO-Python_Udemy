'''
Aula01 - Classes, Objetos e Atributos

* Classe - esqueleto que serve para moldar um Objeto
* Objeto - uma instância da classe que possui cada um suas especificidades
* Atributos - variáveis atributos do Objeto

'''
class Vetor():
    x = 2
    y = 0

#teste
vetor1 = Vetor()
vetor2 = Vetor()

print(vetor1.x)
print (vetor1.y)

print(vetor2.x)
print(vetor2.y)

#trabalhando com as variáveis diretamente no objeto - não altera o atributo da classe
vetor1.x = 10000
print(vetor1.x) 

vetor2.x = 50000
print(vetor2.x) 