
#DEFINIR CADENAS

cadena_uno = "Hola, mundo"
cadena_dos = "Gonzalo Hernán"
cadena_tres = "manzana dura"
cadena_cuatro = " h o l a "
cadena_cinco = "1rkf"
separador = " o "
frutas = ["manzanas","peras","Uvas","mandarinAs"]


#METODOS 

longitud = len(cadena_uno) #Devuelve el número de caracteres en la cadena.(ESTE NO ES UN METODO)
mayusculas = cadena_uno.upper() #Decuelve todos los caracteres como mayusculas
minusculas = cadena_dos.lower() #Decuelve todos los caracteres como minusculas
first_capital = cadena_tres.capitalize() #La primera letra de una cadena es mayuscula y las demas minusculas 
first_of_all_cap = cadena_tres.title() #Convierte la primera letra de cada palabra en una cadena a mayúscula.
without_spaces_end_and_first = cadena_cuatro.strip() #Elimina espacios en blanco y caracteres de nueva línea al principio y al final de una cadena.
without_spaces_first = cadena_cuatro.lstrip() #Elimina espacios en blanco y caracteres de nueva línea al principio de una cadena.
without_spaces_end = cadena_cuatro.rstrip() #Elimina espacios en blanco y caracteres de nueva línea al final de una cadena.
replace = cadena_tres.replace("manzana", "pera") #Reemplaza todas las ocurrencias de old con new en una cadena.
separate = cadena_dos.split(" ") #Divide una cadena en una lista de subcadenas utilizando el separator especificado.
join = separador.join(frutas) #Une una lista de cadenas (o cualquier iterable) en una sola cadena utilizando la cadena actual como separador.
start_with = cadena_tres.startswith("m3n") #Verifica si una cadena comienza con el prefijo especificado. TRUE OR FALSE
end_with = cadena_tres.endswith("dura") #Verifica si una cadena termina con el sufijo especificado. TRUE OR FALSE
letters = cadena_tres.isalpha()  #Verifica si todos los caracteres en una cadena son letras. (ESPACIOS NO SON LETRAS) TRUE OR FALSE
numbers = cadena_cuatro.isdigit()  #Verifica si todos los caracteres en una cadena son dígitos. TRUE OR FALSE
alphanum = cadena_cinco.isalnum() #Verifica si todos los caracteres en una cadena son alfanuméricos. TRUE OR FALSE
are_upper = cadena_cinco.isupper()  #Verifica si todos los caracteres en una cadena están en mayúsculas. TRUE OR FALSE
are_lower = cadena_cinco.islower()  #Verifica si todos los caracteres en una cadena están en minusculas. TRUE OR FALSE

#METODOS BUSCAR SUBSTRING

frase = "Hola, ¿cómo estás?"
posicion = frase.find("cómo") #Esto imprimirá 7, que es la posición de inicio de "cómo" en la cadena.
posicion_dos = frase.rfind("cómo") #Esto imprimirá 7, que es la posición de inicio de la última "cómo" en la cadena.

frase_dos = "Hola, ¿cómo estás? ¿cómo te llamas?"
cantidad = frase_dos.count("cómo") # Esto imprimirá 2, ya que "cómo" aparece dos veces en la cadena.

#METODO COMPLEJO 
#str.index(substring): Similar a str.find(), este método busca la primera aparición de la subcadena substring dentro de la cadena str.
# Sin embargo, en lugar de devolver -1 si no se encuentra la subcadena, este método genera una excepción ValueError. Esto significa que
# si la subcadena no se encuentra en la cadena, tu programa se detendrá y mostrará un error.

oracion = "Hola, ¿cómo estás?"
try:
    num_posicion = oracion.index("cómo")
    print(num_posicion)
except ValueError:
    print("La subcadena no se encuentra en la cadena")


#IMPRIMIR
print(cantidad)  #IMPRIMIR RESULTADO 