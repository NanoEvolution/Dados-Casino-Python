import random
import time

tiradas = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
veces_tiradas = 0

# Función que se introduce desde el menu() para tirar los 2 dados, también suba el incremento de tiradas y
# del numero de dado que ha tocado, se suma 1 como cantidad en el diccionario de tiradas
def tirar_dado():
    global veces_tiradas
    veces_tiradas += 1
    valor_dado_1 = random.randint(1, 6)
    valor_dado_2 = random.randint(1, 6)
    print("Tirando dados...")
    time.sleep(1)
    tiradas[valor_dado_1] += 1
    tiradas[valor_dado_2] += 1
    dibujar_dado(valor_dado_1, valor_dado_2)    

# Función que recibe los valores de la tirada de la función anterior para imprimpir por pantalla el resultado
# y volver a llamar a menu() para que sea mas dinámico

def dibujar_dado(valor_dado_1, valor_dado_2):
    print("")
    print("*****   *****")
    print(f"* {valor_dado_1} * | * {valor_dado_2} *")
    print("*****   *****")
    print(f"Ha salido los números {valor_dado_1} y {valor_dado_2}")
    print("")
    menu()

# Función menú que imprime por pantalla el menú y la interactividad del programa
def menu():
    print("===========[ Bienvenido al Casino de Daniel Cobo ]===========")
    print("(S) Salir - Salir del programa")
    print("(T) Tirar - Tirar los dados")
    print("(M) Media Aritmética - Mostrar media de cantidad de dados")
    print("(E) Estadísticas números - Porcentaje de apariciones de cada numero")
    print("=============================================================")
    print()

# While True para que siempre se repita el programa y funciona mediante condicionales con un else para control
# de errores
    while True:
        opcion = input("¿Qué acción desea realizar?: ").upper()
        
        if opcion == "T":
            tirar_dado()

        elif opcion == "M":
            if veces_tiradas > 0: 
                # Esto calcula la media aritmética de los dados tirados usando un for. Como los dados son
                # del rango del diccionario, permite multiplicar cada número de dado (clave) por su cantidad de
                #  apariciones (valor). La suma total se divide entre el doble de las tiradas, ya
                #  que cada tirada lanza dos dados. El .items selecciona lo que hay dentro del diccionario 
                # directamente
                media = sum(numero * cantidad for numero, cantidad in tiradas.items()) / (2 * veces_tiradas)
                print(f"De las {veces_tiradas} tiradas de dados, la media ha sido: {media:.2f}")
                print("")
                menu()
            else:
                print("No se han realizado tiradas aún.")
                print("")
                menu()

        elif opcion == "S":
            print("Saliendo del Casino...")
            exit()

        elif opcion == "E":
            if veces_tiradas > 0: # Control de errores por si se intenta revisar la media y no se ha tirado ninguna vez
                total_tiradas = 2 * veces_tiradas # Como en realidad lanzamos 2 dados en una tirada, se calcula el total
                print(f"De las {total_tiradas} tiradas de dados:")
                for numero, cantidad in tiradas.items():
                    porcentaje = (cantidad / total_tiradas) * 100
                    
                    print(f"El número {numero} ha salido {cantidad} veces del total. Un {porcentaje:.2f}%")
                print("")
                menu()
            else:
                print("No se han realizado tiradas aún.")
                print("")
                menu()
                
        else:
            print("Opción no válida. Intente nuevamente.")
            print("")
            menu()

menu()
