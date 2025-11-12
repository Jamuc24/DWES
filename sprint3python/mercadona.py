#Ejercicio del Banco

#Zona de la funcion encargada de desplegar el menu principal
def mostrar_menu():
    print("Bienvenido al Mercadona (pero si demandan no lo es)")
    print("1. agregar producto a la cesta")
    print("2. eliminar producto de la cesta")
    print("3. ver carrito de productos")
    print("4. vaciar carrito de productos")
    print("5. salir/ir a la caja")

#Zona para declarar el carrito de la compra
carrito_compra = []

#Zona de la funcion encargada de agregar los productos
def agregar_producto():
    producto = input("Producto a agregar: ").lower().strip()
    if producto in carrito_compra:
        print("Ya tienes ese producto en el carrito")
    else:
        carrito_compra.append(producto)
        print(f"'{producto}' añadido al carrito")

#Zona de la funcion encargada de eliminar productos del carrito
def eliminar_producto():
    if not carrito_compra:
        print("el carrito esta vacio")
        return
    
    producto = input("Producto a eliminar: ").lower().strip()
    
    if producto in carrito_compra:
        carrito_compra.remove(producto)
        print(f"'{producto}' eliminado del carrito")
    else:
        print("Este producto no este en tu carrito")

#Zona de la funcion encargada de visualizar el carrito de la compra
def ver_carrito():
    if not carrito_compra:
        print("el carrito esta vacio")
    else:
        print("Tus productos en el carrito hasta el momento son: ")
        carrito_compra.sort()
        for i, producto in enumerate(carrito_compra, 1):
            print(f"{i}. {producto}")

#Zona de la funcion encargada de vaciar el carrito de la compra
def vaciar_carrito():
    if not carrito_compra:
        print("el carrito ya está vacio")
        return
    
    confirmar = input("quieres retirar todos los productos agregados? (s/n): ").lower()
    if confirmar == 's':
        carrito_compra.clear()
        print("carrito vaciado")
    else:
        print("cambie de opinion")

#Zona de fusionar todas las demas funciones para hacer funcionar el carrito de la compra
print("Menu para gestionar tus compras")

while True:
    mostrar_menu()
    opcion = input("Elige una opcion (1-5): ")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        eliminar_producto()
    elif opcion == "3":
        ver_carrito()
    elif opcion == "4":
        vaciar_carrito()
    elif opcion == "5":
        print("Hasta la siguiente compra, apreciado cliente")
        break
    else:
        print("Aun no tenemos esa opcion, elige de 1 a 5")