# PROYECTO N1 INTEGRADOR PRIMER MODULO
#1. COLECCION DE DATOS (LISTA DE DICCIONARIOS)
inventario = [ 
    {"id": 1, "nombre": "Teclado mecanico", "precio": 45000.0, "stock": 10}, 
    {"id": 2, "nombre": "Mouse gamer", "precio": 25000.0, "stock": 15},
    {"id": 3, "nombre": "Monitor 24", "precio": 180000.0, "stock":5}]
#2. FUNCIONES DE APOYO Y VALIDACION
def obtener_siguiente_id():
    """calcula el id autoincremental para un nuevo producto."""
    if not inventario:
        return 1
    return inventario[-1]["id"] + 1
def ingresar_numero_positivo(mensaje, es_entero=False): 
    """Bucle con try/except para validar que el usuarion ingrese numeros validos."""
    while True:
        try:
            entrada = input(mensaje)
            valor = int(entrada) if es_entero else float (entrada)
            if valor < 0:
                print("⚠️ el numero debe ser mayor o igual a cero.")
                continue
            return valor
        except ValueError:
            print("❌ Entrada invalida. Por favor, ingresa un numero correcto.")
# 3. FUNCIONES PRINCIPALES DEL SISTEMA
def agregar_producto():
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    nombre = input("Nombre del producto: ").strip().capitalize()
    if not nombre:
        print("⚠️ El nomnre no puede estar vacio.")
        return
    precio = ingresar_numero_positivo("Precio del producto: $", es_entero=False)
    stock = ingresar_numero_positivo("Cantidad er stock: ", es_entero=True)

    nuevo_prod = {
        "id": obtener_siguiente_id(), "nombre": nombre, "precio": precio,
        "stock": stock
    }
    inventario.append(nuevo_prod)
    print(f"✅ ¡Producto '{nombre}' agregado exitosamente con ID {nuevo_prod['id']}!")

def listar_productos():
    print("\n--- LISTA DE PRODUCTOS---")
    if not inventario: 
        print("El inventario esta vacio.")
        return
    print(f"{'ID':<5} | {'Nombre':<20} | {'Precio':<12} | {'Stock':<8}")
    print("-" * 52)
    for prod in inventario:
        print(f"{prod['id']:<5} | {prod['nombre']:<20} | ${prod['precio']:<11.2f} | {prod['stock']:<8}")

def buscar_producto():
    print("\n--- BUSCAR PRODUCTO ---")
    criterio = input("Ingresa el nombre o parte del nombre a buscar: ").strip().lower()

    resultados = [p for p  in inventario if criterio in p["nombre"].lower()]

    if resultados: 
        print("\nResultados encontrados:")
        for prod in resultados:
            print(f"-ID: {prod['id']} | {prod['nombre']} | Precio : ${prod['precio']} | Stock: {prod['stock']}")
    else:
        print("❌ No se encontraron productos con ese criterio.")

def realizar_venta():
    print("\n--- REGISTRAR  VENTA ---")
    listar_productos()
    if not inventario:
        return

    id_prod = ingresar_numero_positivo("Ingresa el ID del producto a vender: ", es_entero=True)

    #busqueda por id del producto
    producto_encontrado = None
    for p in inventario:
        if p["id"] == id_prod:
            producto_encontrado = p
            break

    if not producto_encontrado:
        print("❌ No existe ningun producto con ese ID.")
        return
    cantidad = ingresar_numero_positivo(f"Cantidad a vender de '{producto_encontrado['nombre']}': ", es_entero=True) 
#condicionales para verificar stock suficiente
    if cantidad > producto_encontrado["stock"]:
        print(f"❌ Stock insuficiente. Solo quedan {producto_encontrado['stock']} unidades disponibles.")
    else:
        producto_encontrado["stock"] -= cantidad
        total = cantidad * producto_encontrado["precio"]
        print(f"✅ Venta realizada. Total a pagar: ${total:.2f}")
        print(f"Stock restante de '{producto_encontrado['nombre']}': {producto_encontrado['stock']}")

# 4: BUCLE PRINCIPAL Y MENU DE NAVEGACION
def menu_principal():
    while True:
        print("\n============================================")
        print("        SISTEMA DE GESTIÓN Y VENTAS         ")
        print("============================================")
        print("1. Ver lista de productos")
        print("2. Agregar nuevo producto")
        print("3. Buscar producto por nombre")
        print("4. Registrar una venta")
        print("5. Salir")

        opcion= input("\nSeleccioná una opción (1-5): ").strip()

        if opcion == "1":
            listar_productos()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            realizar_venta()
        elif opcion == "5":
            print("\n¡Gracias por usar el sistema! Saliendo...")
            break
        else:
            print("⚠️ Opción no valida. Por favor, elegi un número deñ 1 al 5.")

#Punto de entrada para ejecutarla aplicacion
if __name__ == "__main__":
    menu_principal()