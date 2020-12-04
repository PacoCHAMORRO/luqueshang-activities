# Clase Nodo
class Node:
  data = None
  next = None
  # Constructor, recibe dato, inicializa el siguiente 
  # apuntando/refrenciando a null/None
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

  # -------------- Getters --------------
  def get_data(self):
    return self.data

  def get_next(self):
    return self.next

  # -------------- Setters --------------
  def set_data(self, data):
    self.data = data

  def set_next(self, next):
    self.next = next