#Zona de definicion de los valores de la cuenta
cuenta = {
    "cliente": "Jorgino",
    "saldo": 1000
}

#Zona de la funcion encargada de desplegar el menu principal
def mostrar_menu():
    print("Banco Antidinero, Bienvenido")
    print("1. Consultar saldo actual")
    print("2. Ingresar dinero a mi cuenta")
    print("3. Retirar dinero de mi cuenta") 
    print("4. Salir/cerrar sesion")

#Zona de la funcion encargada de consultar el saldo
def consultar_saldo():
    print(f"Saldo actual: ${cuenta['saldo']}")

#Zona de la funcion encargada de ingresar el saldo
def ingresar_saldo():
    while True:
        try:
            cantidad = int(input("Cantidad a ingresar: $"))
            if cantidad > 0:
                cuenta['saldo'] += cantidad
                print(f"Dinero insertado: ${cantidad}")
                print(f"Nuevo saldo: ${cuenta['saldo']}")
                break
            else:
                print("No puedes restarte dinero, para eso hay otra opcion")
        except:
            print("Escribe un numero entero, no aceptamos centimos")

#Zona de la funcion encargada de retirar el saldo
def retirar_dinero():
    while True:
        try:
            cantidad = int(input("Cantidad a retirar: $"))
            if cantidad <= 0:
                print("La cantidad debe ser positiva, hay otra opcion para ingresar dinero")
            elif cantidad > cuenta['saldo']:
                print("Saldo insuficiente, POBRETON")
                print(f"Saldo actual: ${cuenta['saldo']}")
            else:
                cuenta['saldo'] -= cantidad
                print(f"Retirado: ${cantidad}")
                print(f"Nuevo saldo: ${cuenta['saldo']}")
                break
        except:
            print("Escribe un número entero")

#Zona de la funcion encargada de ensamblar todas las demas funciones comformando el cajero
print("Banco Antidinero, Bienvenido")

while True:
    mostrar_menu()
    
    opcion = input("Elige una opcion (1-4): ")
    
    if opcion == "1":
        consultar_saldo()
    elif opcion == "2":
        ingresar_saldo()
    elif opcion == "3":
        retirar_dinero()
    elif opcion == "4":
        print("Sesion cerrada correctamente")
        break
    else:
        print("Aun no tenemos esa opcion, elige de 1 a 4")