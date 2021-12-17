#Sidney
#5) Modifique o programa abaixo de forma a realizar a mesma tarefa, mas sem utilizar a variável achou. Dica: observe a condição de saída do while.

L=[15,7,27,39]

x=0
while x<len(L):
    p=int(input("Digite o valor a procurar:"))
    if p in L:
        print("Valor Encontrado")
        x = 100
        break
    x+=1
if x != 100:
    print("Valor Não Encontrado")
    

