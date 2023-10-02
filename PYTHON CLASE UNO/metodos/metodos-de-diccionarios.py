#CREAR DICCIONARIO
diccionario = {
    "nombre" : 'Gonzalo',
    "apellido" : 'Garcia',
    "calificaion" : 90    
}

diccionario_dos = {
    "nombre" : 'Andre',
    "apellido" : 'Guerra',
    "calificaion" : 92  
}


diccionario_tres = {
    "nombre" : 'Mauricio',
    "apellido" : 'Tejeda',
    "calificaion" : 87 
}

#METODOS
claves = diccionario.keys() #Devuelve las claves (tambien sirve para iterar)
valores_clave = diccionario.get("nombre") #Devuelve el valor de una clave (si np encuentra nada el programa continua solo da un none)
borrar = diccionario_dos.clear() #Borra todos los elementos
borrar_uno = diccionario_tres.pop("apellido") #Borra un elemento en especifico 
diccionario_iterable = diccionario.items() #iterar 

#IMPRIMIR RESULTADO
print(claves)
print(valores_clave)

print(diccionario_dos)

print(diccionario_tres)

print(diccionario_iterable)