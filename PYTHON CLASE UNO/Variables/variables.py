#DECLARANDO Y DEFINIENDO VARIABLES
a=2
b=3
c=a+b
nombre="Gonzalo"
apellido = " García"
nombreEntero = nombre + apellido  #usando camelCse

#CONCATENAR CON +
bienvenida = "hola " + nombreEntero + " ¿Cómo estas?" 

#CONCATENAR CON F STRING
bienvenida_Dos = f"Hola {nombreEntero}"  #usando snake_case

#BORRAR DATOS DE UNA VARIABLE (DELETE)
del bienvenida 

#PRINTS
print(bienvenida_Dos)
print(c)

#OPERADORES DE PERTENENCIA IN & NOT IN
print ("zalo" in nombre) #DA TRUE PORQUE ESTA DENTRO DE LA VARIABLE
print ("zalo" not in nombre) #DA FALSE PORQUE ESTA DENTRO DE LA VARIABLE