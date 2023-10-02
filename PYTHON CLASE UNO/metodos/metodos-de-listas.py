#DEFINE LA LISTA
lista = list(["manzana","pera","platano"]) #Función para crear lista (es mejor para crearla sin elementos)
mi_lista1 = [1,2,3]
mi_lista_desordenada = [1,7,6,5,8,9,0,2,4,3]
mi_lista2 = [3,2,1,0]
mi_lista_para_eliminar = [1,5,3,2,5,6,4,3]

#METODOS DE LISTAS
mi_lista1.append(4) #Agrega un elemento al final de la lista.
mi_lista1.extend([5,6,2]) #Agrega los elementos de un iterable al final de la lista.
mi_lista1.insert(1, 69) #Inserta un elemento en una posición específica de la lista.
mi_lista1.remove(69) #Elimina la primera ocurrencia de un elemento en la lista.
mi_lista_desordenada.sort() #Ordena la lista en su lugar en orden ascendente.
mi_lista2.reverse() #Invierte la lista en su lugar.
mi_lista_para_eliminar.clear() #elimina todos los elementos de una lista 

indice = mi_lista1.index(3) #Devuelve el índice de la primera aparición de un elemento en la lista.
elemento_uno = mi_lista1.pop(4) #Elimina y devuelve el elemento en la posición especificada (o el último elemento si no se proporciona un índice)
conteo = mi_lista1.count(2) #Devuelve el número de veces que un elemento aparece en la lista.
longitud = len(mi_lista_desordenada) #devuelve el numero de elementos de la lista 

#IMPRIME LA LISTA DESEADA
print(mi_lista1)

print(indice)
print(elemento_uno)
print(conteo)

print(mi_lista_desordenada)
print(mi_lista2)
print(mi_lista_para_eliminar)
print(lista)
print(longitud)

