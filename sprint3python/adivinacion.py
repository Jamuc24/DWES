import random

reintentar = True  
while reintentar:  
    
    # Zona de presentar el juego
    print("Bienvenido a adivina el numero, donde... adivinas el numero")
    print("Elige la dificultad:")

    #Zona para elegir dificultad
    while True:
        print("1 - Facil")
        print("2 - Intermedio") 
        print("3 - Dificil")
        
        opcion = input("Elige (1/2/3): ")
        
        if opcion == "1":
            max_numero = 50
            print("Nivel Facil (1 a 50)")
            break
        elif opcion == "2":
            max_numero = 100
            print("Nivel Intermedio (1 a 100)")
            break
        elif opcion == "3":
            max_numero = 500
            print("Nivel Dificil (1 a 500)")
            break
        else:
            print("No elegiste una opcion, elige 1, 2 o 3")

    # Zona de generar numero secreto y los intentos
    numero_secreto = random.randint(1, max_numero)
    intentos = 0

    # Zona del juego principal
    while True:
        try:
            tu_numero = int(input("Introduce un numero: "))
            intentos = intentos + 1

            if tu_numero < numero_secreto:
                print("El numero es mayor que ese")
            elif tu_numero > numero_secreto:
                print("El numero es menor que ese")
            else:
                print(f"Lo clavaste en {intentos} intentos")
                break
                
        except ValueError:
            print("Esto NO es un numero valido")

    # Zona de preguntar si quiere jugar de nuevo (FUERA del bucle de juego)
    print("\n" + "=" * 30)
    while True:
        respuesta = input("¿Quieres jugar otra vez? (s/n): ").lower().strip()
        if respuesta == 's':
            reintentar = True
            break
        elif respuesta == 'n':
            reintentar = False
            break
        else:
            print("Responde 's' para SÍ o 'n' para NO")

print("The end")
