from os import system, name 
import sys
import time


class Stack:
    elements = []

    def __init__(self):
        self.elements = []

    def push(self, x):
        self.elements.append(x)

    def pop(self):
        return self.elements.pop()

    def peek(self):
        return self.elements[-1]

    def is_empty(self):
        return not self.elements

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

if __name__ == '__main__':

    homework_stack = Stack()
    opcion = None

while opcion != "3":
    clear()
    print("--------- PARA DE PROCRASTINAR 3000 ---------")
    if (not homework_stack.is_empty()):
        print("# Ultima tarea apilada: " + homework_stack.peek())
    else:
        print("# Ultima tarea apilada: Nada, no hay, no existe")
    print('---------------------------------------------')
    print("Opciones:\n"
          "1. Apilar una tarea\n"
          "2. Hacer una tarea\n"
          "3. Salir")

    opcion = input("Escribe tu opcion (1-3): ")

    if opcion == "1":
        print('---------------------------------------------')
        homework = input("Ingrese el título de la tarea: ")
        homework_stack.push(homework)
        print("Tarea ingresada exitosamente.")
        print("Volviendo al menu...")
        time.sleep(3)

    elif opcion == "2":
        if (not homework_stack.is_empty()):
            homework_stack.pop()
            print("Haciendo tarea", end='', flush=True)
            for i in range(25):
                time.sleep(.2)
                print('.', end='', flush=True)
            print(" ")
            print("Tarea hecha, campeón@!")
            print("Volviendo al menu...")
            time.sleep(3)
        else:
            print("No tienes tareas pendientes")
            print("Volviendo al menu...")
            time.sleep(3)

    elif opcion == "3":
        print("Saliendo del programa...")
        time.sleep(3)
        sys.exit()

    else:
        print("Error!, ingrese una opción válida")
        time.sleep(3)
