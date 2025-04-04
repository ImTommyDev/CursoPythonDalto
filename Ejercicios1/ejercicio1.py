#datos iniciales. Duracion de horas de los cursos
duracion_max_otros = 7
duracion_min_otros = 2.5
media_duracion_otros = 4
duracion_dalto = 1.5

#Diferencia de dutración entre el curso de dalto y el más rápido de los otros
diferencia_min = 100 - duracion_dalto * 100 / duracion_min_otros
print("El curso de Dalto dura", diferencia_min, "% menos que el curso más rápido de los otros")

#Diferencia de duración entre el curso de dalto y el más lento de los otros
diferencia_max = 100 - round(duracion_dalto * 100 / duracion_max_otros, 2)
print("El curso de Dalto dura", diferencia_max, "% menos que el curso más lento de los otros")

#Diferencia de duración entre el curso de dalto y la media de los otros
diferencia_media = 100 - duracion_dalto * 100 / media_duracion_otros
print("El curso de Dalto dura", diferencia_media, "% menos que la media de los otros cursos")

#EJERCICIO 2
#Defino las variables de la duración de los cursos sin editar (el crudo de los cursos)
duracion_crudo_otros = 5
duracion_crudo_dalto = 3.5

#Calculo el porcentaje de tiempo vacio
tiempo_vacio_otros = 100 - round(media_duracion_otros * 100 / duracion_crudo_otros, 2)
tiempo_vacio_dalto = 100 - round(duracion_dalto * 100 / duracion_crudo_dalto,2)
print("El curso de Dalto elina un", tiempo_vacio_dalto, "% de tiempo vacío")
print("Otros cursos eliminan un", tiempo_vacio_otros, "% de tiempo vacío")


#EJERCICIO 3
#Ver 10h de este curso a cuando equivale de otros cursos
print(f'Ver 10h de este curso equivale a {round(media_duracion_otros * 100 // duracion_dalto / 10, 2)}h de los otros cursos')
print(f'Ver 10h de otros cursos equivale a {round(duracion_dalto * 100 // media_duracion_otros / 10, 2)}h de el de dalto')