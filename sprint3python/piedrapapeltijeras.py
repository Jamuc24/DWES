import random

#Zona de la declaracion de las opciones, las almacenamos asi para poder aletorizarlas despues :p
opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]

#Zona donde definimos que es capaz de ganar a que, haciendo un array de array
reglas = {
    "tijera": ["papel", "lagarto"],
    "papel": ["piedra", "spock"],
    "piedra": ["tijera", "lagarto"],
    "lagarto": ["spock", "papel"],
    "spock": ["tijera", "piedra"]
}

#Zona donde determinaremos quien ganara entre la maquinola o el jugador
def quien_gana(jugador, maquinola):
    if jugador == maquinola:
        return 0
    elif maquinola in reglas[jugador]:
        return 1
    else:
        return -1

#Zona donde se lleva a cabo el jugar la partida, la parte principal
def jugar_partida():
#Zona de pedir número de rondas
    while True:
        try:
            n_rondas = int(input("Inserta un numero de rondas (numero impar): "))
            if n_rondas >= 1 and n_rondas % 2 == 1:
                break
            else:
                print("NO insertaste un numero IMPAR")
        except:
            print("Escribe un numero")
    
    victorias_necesarias = n_rondas // 2 + 1
    victorias_jugador = 0
    victorias_maquinola = 0
    
#Zona para determinar los resultados de cada ronda
    while victorias_jugador < victorias_necesarias and victorias_maquinola < victorias_necesarias:
        print(f"\nResultados hasta ahora: Jugador {victorias_jugador} - {victorias_maquinola} Maquinola")
        
        #Zona para la eleccion del jugador
        while True:
            eleccion = input("Elige entre piedra, papel, tijera, lagarto, spock: ").lower()
            if eleccion in opciones:
                break
            else:
                print("Elige entre piedra, papel, tijera, lagarto, spock: ")
        
        #Zona para la eleccion de la maquinola
        eleccion_maquinola = random.choice(opciones)
        print(f"maquinola elige: {eleccion_maquinola}")
        
        #Zona para determinar el resultado de la ronda
        resultado = quien_gana(eleccion, eleccion_maquinola)
        
        if resultado == 0:
            print("Empate")
        elif resultado == 1:
            print("Ganaste esta ronda")
            victorias_jugador += 1
        else:
            print("Gana la maquinola")
            victorias_maquinola += 1
    
#Zona de visualizar el resultado final de la partida
    print(f"Resultados finales: Tu {victorias_jugador} - {victorias_maquinola} maquinola")
    if victorias_jugador > victorias_maquinola:
        print("Absoluto ganador de la partida? tú")
    else:
        print("Vaya, acabas de perder contra la IA, verguenza")

#Zona para jugar o relanzar el juego
print("PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK")

jugar_de_nuevo = True

while jugar_de_nuevo:
    jugar_partida()
    
    while True:
        respuesta = input("te juegas otra partida? (s/n): ").lower()
        if respuesta == 's':
            jugar_de_nuevo = True
            break
        elif respuesta == 'n':
            jugar_de_nuevo = False
            break
        else:
            print("Responde s o n")

print("Fin del ejercicio mas rolloso de todos, y del juego :P")
