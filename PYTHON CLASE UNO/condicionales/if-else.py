
#CONDICIONALES IF Y ELSE

#VARIABLES  INICIO DE SESION
usuario_base_de_datos = 'manuelito23'
contraseña_base_de_datos = 'Mojon123'
usuario_ingresado = 'manuelito23'
contraseña_ingresada = 'Mojon123'

#VARIABLES DE SALARIO
ingreso_mensual = 100

#CICLO DE INICIO DE SESION

if usuario_base_de_datos == usuario_ingresado and contraseña_base_de_datos == contraseña_ingresada:
    print("Inicio de sesion exitoso")
else: 
    print("Contraseña o Usuario incorrecto")


#CICLO DE SALARIO

if ingreso_mensual >= 600 :
    print ("Estas bien en USA")

elif ingreso_mensual >= 400 :
    print ("Estas bien en México")

elif ingreso_mensual >= 300 :
    print ("Estas bien en Perú")

elif ingreso_mensual >= 200 :
    print ("estas muy bien en Venezuela")

else :
    print ("Eres de clase muy baja en todos los países")