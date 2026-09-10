stock = ["manzana", "banana", "naranja"]
stock.append("pera")
stock.insert(0, "frutilla")
print("paso 3 (insert):", stock)
stock.remove("naranja")
print("paso 3 (remove):", stock)
stock.sort()
print("paso 5 (sort):", stock)
print(stock)
ofertas = [fruta.upper() for fruta in stock]
print("nueva lista (ofertas):", ofertas)
print("lista original (stock):", stock)
vendida = ofertas.pop(1)
print("lista ofertas actualizada:", ofertas)
print("vendido:", vendida)
#esta codigo es para probar las ordenes de lista estructura de datos