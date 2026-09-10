mi_tupla = (1,2,3,2,4,2)
          # 0 1 2 3 4 5
print("=== PRACTICANDO METODOS DE TUPLAS ===")
#PROBANDO EL TAMAÑO REAL
total= len(mi_tupla)
print(f"1. tamaño total de la tupla (len): {total} elementos")
#PROBANDO COUNT (REPETICIONES)
cantidad_de_dos = mi_tupla.count(2)
cantidad_de_tres = mi_tupla.count(3)
cantidad_de_nueve = mi_tupla.count(9)
print(f"2. EL numero 2 aparece (count): {cantidad_de_dos} veces")
print(f" El numero 3 aparece(count): {cantidad_de_tres} veces")
print(f" El numero 9 aparece (count): {cantidad_de_nueve} veces")
#PROBANDO INDEX BUSQUEDA DE POSICIONES
#BUSQUEDA SIMPLE
pos_primer_dos = mi_tupla.index(2)
print(f"3. Primer '2' en toda la tupla (index): posicion {pos_primer_dos}" )
#BUSQUEDA DE INICIO (SALTA LA 1 PARTE)
pos_segundo_dos = mi_tupla.index(2, 2)
print(f" Primer '2' buscado desde incide 2 (index): posicion {pos_segundo_dos}")
#BUSQUEDA CON INICIO Y FIN 
pos_rango = mi_tupla.index(2, 2, 4)
print(f" Primer '2' buscando solo entre indice 2 y 4 (index): posicion {pos_rango}")