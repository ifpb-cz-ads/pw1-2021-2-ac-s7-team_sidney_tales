#Sidney
#2) Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.

listOne = []
listTwo = []
listThree = []
aux = 0
length = int(input('quantos itens deseja inserir nas lista? '))
while(aux < length):
    listOne.append(input("Na primeira lista insira o item %d  " % (aux+1)))
    listThree.append(listOne[aux])
    listTwo.append(input("Na Segunda lista insira o item %d  " % (aux+1)))
    listThree.append(listTwo[aux])
    aux = aux +1
print(listOne)
print(listTwo)
print(listThree)

