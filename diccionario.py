 #DICCIONARIO FICHA DE PASAJEROS
pasajero1 = {"nombre": "Juan", "edad": 25, "ciudad": "Buenos Aires"}
pasajero2 = {"nombre": "Roma", "edad": 23, "ciudad": "Tigre"}
#AGRUPAMOS DICC DENTRO DE UNA LISTA DE EXCURSION = [PASAJERO1,PASAJERO2]
excursion = [pasajero1, pasajero2]
print("--- INFORMACION DEL PRIMER PASAJERO---")
#KEYS PROBAR
print("Claves disponibles:", pasajero1.keys())
#PROBAR VALUES
print("Valores guardado:", pasajero1.values())
#PROBAR ITEMS
print("Pareja de datos:", pasajero1.items())
print("\n--- ACTUALIZACIÓN DE DATOS CON .UPDATE()---")
#ACTUALIZAMOS LA EDAD Y AGREGAMOS UN DATO 
datos_nuevos = {"edad": 26, "hotel": "Bungalow Resort"}
pasajero1.update(datos_nuevos)
print("Ficha actualizada de Juan:", pasajero1)
print("\n--- RECORRIENDO LA LISTA COMPLETA CON UN BUCLE---")
#RECORREMOS LA LISTA PARA MOSTRAR TODOS LOS PASAJEROS A LA EXCURSION
for pasajero in excursion:
    print(f"pasajero: {pasajero['nombre']} | Ciudad: {pasajero['ciudad']}")