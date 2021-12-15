#Sidney
#4) Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta. Exemplo:

class Pilha:
     def __init__(self):
         self.items = []

     def estaVazia(self):
         return self.items == []

     def adicionar(self, item):
         self.items.append(item)

     def existe(self, x):
         return x in self.items

     def imprimir(self):
         return print(self.items)
     
     def contar(self, string):
         return self.items.count(string)

     def tamanho(self):
         return len(self.items)

nova = Pilha()

aux = 0
while(aux != '9'):
    aux = input('9 para sair ')
    if(aux != '9'):
        nova.adicionar(aux)    
    nova.imprimir()
    
aberto = nova.contar('(')
fechado = nova.contar(')')

print('( = ', aberto, ', ) =', fechado)
if(aberto != fechado):
    print('ERRO')
else:
    print('OK')
nova.imprimir()
