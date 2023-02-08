def sum(valor_1, valor_2):
  return valor_1 + valor_2
valor_1 = 10
valor_2 = 20

result = sum(valor_1,valor_2)
lista_valores = []
lista_valores.append(valor_1)
lista_valores.append(valor_2)
lista_valores.append(result)


for valor in lista_valores:
    print(valor)

for i in range(0, len(lista_valores)):
    print('Posicao: '+ str(i) + ' Valor: ' + str(lista_valores[i]))
