# gestion de pasajeros/invitados
#1 crear conjuto inicial
invitados = {"juan", "Roma", "pedro"}
print("1. invitados iniciales:", invitados)
#uso de add agrega nuevos elementos
invitados.add("Lucas")
invitados.add("Roma")
print("\n2. despues de .add():", invitados)
#uso de remove elimina un elemento
invitados.remove("pedro")
print("\n3. Despues de .remove('pedro'):", invitados)
#uso de discard elimina sin riesgo de error
#eliminar a lucas (existe)
invitados.discard("Lucas")
# intenta eliminar a carlos ( no existe)
invitados.discard("carlos")
print("\n4. Despues de .discard():", invitados)
# uso de clear vaciar el conjunto entero
invitados.clear()
print("\n5. Despues de .clear():", invitados)
