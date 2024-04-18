import pygame as pg


class Auto(pg.sprite.Sprite):
    def __init__(self, placa, ubicacion):
        pg.sprite.Sprite.__init__(self)
        self.placa = placa
        self.imagen = None
        # ubicacion del auto
        self.ubicacion = ubicacion

    '''def getSprite(self):
        s = 0'''


# Lista de autos estacionados
class Nodo:
    def __init__(self, auto):
        self.dato = auto
        self.next = None


class ListaAutos:
    def __init__(self):
        self.head = None

    def agregarAuto(self, auto):
        if self.estaVacia():
            head = Nodo(auto)
            head.next = head
        if self.existeAuto(auto.placa):
            return False
        head = self.head
        if head.next is head:
            head.next = Nodo(auto)
            head.next.next = head
        else:
            temp = head.next
            while temp.next != head:
                temp = temp.next
            temp.next = Nodo(auto)
            temp.next.next = head
        return True

    def eliminarAuto(self, placa):
        if not self.existeAuto(placa):
            return False
        temp = self.head
        while temp.next.auto.placa != placa:
            temp = temp.next
        temp.next = temp.next.next
        return True

    def estaVacia(self):
        return self.head is None

    def existeAuto(self, placa):
        if self.estaVacia():
            return False
        temp = self.head
        if temp.auto.placa == placa:
            return True
        while temp.next != self.head:
            temp = temp.next
            if temp.auto.placa == placa:
                return True
        return False
