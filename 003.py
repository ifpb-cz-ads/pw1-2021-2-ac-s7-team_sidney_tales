#Sidney
#3) Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
#não ta perfeito já que se a segunda lista for menor que a primeira da erro, mas funciona :)
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
list3 = []
aux = 0
while(aux < len(list1)):
    if(not list1[aux] in list3):
        list3.append(list1[aux])
    if(not list2[aux] in list3):
        list3.append(list2[aux])
    aux=aux+1
print('lista 1: ', list1)
print('Lista 2: ', list2)
print('Lista 3: ', list3)