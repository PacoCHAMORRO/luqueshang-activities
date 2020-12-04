# importamos clase Node
from node import Node

# Lista simplemente ligada
class LinkedList:
    anchor = None
    last = None
    number_of_elements = 0
    # Constructor
    def __init__(self):
        # Inicializa el ancla con un Nodo vació
        self.anchor = Node(None)
        # Inicializa el último valor con el valor del ancla
        self.last = self.anchor

    # Obtener numero de elementos
    def get_num_elements(self):
        return self.number_of_elements

    # Insertar en una posición dada
    def insert(self, element, position):
        # Excepción por posición fuera de rango
        if position < 0 or position > self.number_of_elements:
            raise Exception('posicion fuera de rango.')
        
        # Nodo auxiliar, incializado en el primer elemento
        current = self.anchor
        # Nodo auxiliar, referenciando el elemento que queremos agregar
        new_node = Node(element)

        # Si se quiere insertar en la primera posción
        if position == 0:
            # El nuevo elemento, toma como siguiente la posición del ancla
            new_node.next = self.anchor
            # El ancla toma el valor del nuevo nodo ahora
            self.anchor = new_node

        # Si no queremos ingresar al principio
        else:
            # Traversamos la lista hasta llegar a la posición que queremos
            # y le restamos uno, para insertar nuestro elemento          
            i = 0
            while i < position - 1:
                current = current.next
                i += 1
            # Teniendo la posición que queremos en current
            # Nodo Auxiliar toma el valor de siguiente del valor actual
            aux = current.next
            # El siguiente del valor actual ahora referecia al nuevo nodo
            current.next = new_node
            # el nuevo nodo toma el valor de auxiliar
            new_node.next = aux

            # En caso de que la posicón haya sido la última, actualizamos su valor
            if position == self.number_of_elements:
                self.last = new_node

    # Buscar por elemento, regresa su posición
    def get_position(self, element):
        aux = self.anchor
        i = 0
        # Mientras que sea verdadero
        while 1:
            # Cuando encuentre el dato regresa i, o sea, su posición
            if aux.data is element:
                return i
            # Si no está el elemento, regresa falso
            if aux.next is None:
                return -1

            i += 1
            aux = aux.next

    # Elimina un elemento de la lista por su valor
    def delete(self, element):
        # Encuentra la posición del elemento
        position = self.get_position(element)

        # Si la lista está vacía, nada sucede
        if position == -1:
            return None

        # Si eliminamos la primera posición, el ancha referencía
        # a su siguiente nodo
        if position == 0:
            self.anchor = self.anchor.next

        # Eliminar en cualquier lado
        # encontramos primero la posición
        else:
            current = self.anchor

            i = 0
            while i < position - 1:
                current = current.next
                i += 1
            # Simplemente dejamos de referenciar el valor
            # Que queremos eliminar y el recolector de basura e Python pasa
            current.next = current.next.next

            # Actualizamos el último en caso de que se haya elimnado 
            if position == self.number_of_elements - 1:
                self.last = current
        # Actualizamos el número de elementos
        self.number_of_elements -= 1

    # Insertar al final
    def append_element(self, element):
        new_node = Node(element)
        # Si es la primera inserción
        if self.anchor.data == None:
            new_node.next = self.anchor
            self.anchor = new_node
        # después de la primera vez
        self.last.next = new_node
        self.last = new_node
        self.number_of_elements += 1

    # Imprimir lista
    # recorremos la lista, e imprimimos su posición y su valor
    def print_list(self):
        current = self.anchor
        x = 0
        while current is not None:
            print(str(x) + " " + current.data)
            current = current.next
            x+=1

if __name__ == '__main__':
    # Creación de lista
    todo_list = LinkedList()
    print("Agregar elementos al final de la lista")
    # Agregar unos elementos al final de la lista
    todo_list.append_element("Ir al supermercado")
    todo_list.append_element("Ir al gym")
    todo_list.append_element("Descongelar el pollo")
    todo_list.append_element("Comprar agua")
    todo_list.append_element("Leer 45 minutos")
    todo_list.append_element("Hacer tarea")

    todo_list.print_list()

    print("-------------")
    print("Agrgar elementos al principio de la lista")
    todo_list.insert("Ir al banco", 0)

    todo_list.print_list()

    print("-------------")
    print("Agrgar elementos en cualquier de la lista")
    todo_list.insert("Tocar la guitarra", 3)

    todo_list.print_list()

    print("-------------")
    print("Eliminar elemento al principio de la lista")
    todo_list.delete("Ir al banco")

    todo_list.print_list()

    print("-------------")
    print("Eliminar elemento al final de la lista")
    todo_list.delete("Hacer tarea")
  
    todo_list.print_list()

    print("-------------")
    print("Eliminar elemento en cualuqier posición de la lista")
    todo_list.delete("Comprar agua")
  
    todo_list.print_list()
