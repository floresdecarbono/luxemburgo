#entradas
n1 = int(input('número 1: '))
n2 = int(input('número 2: '))
n3 = int(input('número 3: '))

#processamento
if(n1 > n2 and n1 > n3):
    maior = n1
    if(n2 > n3):
        segundo = n2
    else:
        segundo = n3
elif(n2 > n1 and n2 > n3):
    maior = n2
    if(n1 > n3):
        segundo = n1
    else:
        segundo = n3
else:
    maior = n3
    if(n1 > n2):
        segundo = n1
    else:
        segundo = n2

#saida
print(f'o maior número é {maior}')
print(f'o segundo maior número é {segundo}')
