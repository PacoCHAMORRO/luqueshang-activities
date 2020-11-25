from os import system, name
import sys
import time
# Clase Cola FIFO


class Queue:
    # Lista donde guardamos nuestros elementos
    elements = []

    def __init__(self):
        self.elements = []

    # Regresa el frente de la cola
    def front(self):
        if (not self.is_empty()):
            return self.elements[0]

    # Ingresa un nuevo elemento al final de la cola
    def enque(self, x):
        self.elements.append(x)

    # Remueve un elemento de la primera posición de la cola
    def dequeue(self):
        if (not self.is_empty()):
            self.elements.pop(0)

    # Revisa si la cola está vacía
    def is_empty(self):
        return not self.elements

# Helper que nos ayuda a limpiar pantalla
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Main
# aplicación: reproductor de mp3, queue de canciones
if __name__ == '__main__':

    # Declaramos un nuevo objeto del tipo Queue
    playlist_queue = Queue()
    opcion = None
    # Menú principal
    while opcion != "3":
        clear()
        print("----- Canciones para  pasar el semestre -----")
        # -------------- FRONT ------------------
        if (not playlist_queue.is_empty()):
            print("# Reproduciendo ahora: " + playlist_queue.front())
        else:
            print("# Reproduciendo ahora: No hay canciones en el queue")
        print('---------------------------------------------')
        print("Opciones:\n"
              "1. Agregar una canción\n"
              "2. Siguiente canción\n"
              "3. Salir")

        opcion = input("Escribe tu opcion (1-3): ")

        # -------------- ENQUE --------------------
        if opcion == "1":
            print('---------------------------------------------')
            song = input("Ingrese el título de la canción: ")
            playlist_queue.enque(song)
            print("Canción ingresada exitosamente.")
            print("Volviendo al reproductor ¬u¬ ...")
            time.sleep(3)
        # ----------------- DEQUE -----------------
        elif opcion == "2":
            if (not playlist_queue.is_empty()):
                playlist_queue.dequeue()
            else:
                print("Ya se acabó la música")
                print("Volviendo al reproductor ...")
                time.sleep(3)

        elif opcion == "3":
            print("Saliendo del programa...")
            time.sleep(3)
            sys.exit()

        else:
            print("Error!, ingrese una opción válida")
            time.sleep(3)
