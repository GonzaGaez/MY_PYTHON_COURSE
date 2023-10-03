

#DEFINIR HORAS DE CONTENIDO NECESARIO EN CURSOS 

curso_dalto = 1.5
curso_alt_rapido = 2.5
curso_alt_promedio = 4
curso_alt_lento = 7

#DEFINIR HORAS DE MATERIAL INSERVIBLE

crudo_dalto = 3.5 #Y se convirtio a 1.5 post edicion
crudo_alt = 5 #Y se convirtio a 4 post edicion

#SACAR PORCENTAJES DIFERENCIAS
print("- - - - - - - - - - - - - - - ")
diferencia_lento = 100-((1.5 * 100 )/7)
diferencia_prom = 100-((1.5 * 100 )/4)
diferencia_rapido = 100-((1.5 * 100 )/2.5)
diferencia_lento_float = float(diferencia_lento)
diferencia_prom_float = float(diferencia_prom)
diferencia_rapido_float = float(diferencia_rapido)
print(f"""La diferencia en porcentaje con la duración de los cursos es:
      - Con el mas lento de los otros cursos = {diferencia_lento_float} %.
      - Con el promedio de los otros cursos = {diferencia_prom_float} %
      - Con el mas rapido de los otros cursos = {diferencia_rapido_float} %""")
print("- - - - - - - - - - - - - - - ")

#SACAR PORCENTAJES DE CRUDO

porcentaje_crudo_dalto = 100-((1.5*100)/3.5)
porcentaje_crudo_otros = 100-((4*100)/5)
porcentaje_crudo_dalto_float = float(porcentaje_crudo_dalto)
porcentaje_crudo_otros_float = float(porcentaje_crudo_otros)
print(f"""El porcentaje de ahorro en tiempo es:
      - Los otros cursos ahorran = {porcentaje_crudo_otros_float} %.
      - El curso de dalto ahorra = {porcentaje_crudo_dalto_float} %""")
print("- - - - - - - - - - - - - - - ")

#EQUIVALENCIA DE VISUALIZACION 

equivalencia_largo = (curso_alt_lento/curso_dalto*10)
equivalencia_prom = (curso_alt_promedio/curso_dalto*10)
equivalencia_corto = (curso_alt_rapido/curso_dalto*10)
equivalencia_largo_float = float(equivalencia_largo)
equivalencia_prom_float = float(equivalencia_prom)
equivalencia_corto_float = float(equivalencia_corto)
print(f"""La equivalencia en horas de ver este curso en comparacion de los otros cursos es:
      - Ver 10 horas de este curso equivale a {equivalencia_largo_float} horas del curso mas lento.
      - Ver 10 horas de este curso equivale a = {equivalencia_prom_float} horas del curso promedio.
      - Ver 10 horas de este curso equivale a = {equivalencia_corto_float} horas del curso mas rapido.
      - ver 10 horas de otros cursos equivale a = {curso_dalto*100//curso_alt_promedio/10} horas de este curso""")
print("- - - - - - - - - - - - - - - ")