#PEDIRLE UN NÚMERO AL USUARIO

numero = input("dame un numero: ")
num_int = int(numero)

#OPERACIONES

num_multi = input("Por cuanto quieres multiplicar tú número: ")
num_multi_int = int(num_multi)
multiplicado = num_multi_int* num_int

#IMPRIMIR RESULTADOS
print (f'tu numero es: {numero} el cual multiplicado por {num_multi} es: {multiplicado}')

