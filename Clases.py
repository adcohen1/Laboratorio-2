import random
from pathlib import Path
import pygame as pg
import constantes as c

p = Path('./sprites')


class Vehiculo(pg.sprite.Sprite):
    def __init__(self, tipo, placa):
        pg.sprite.Sprite.__init__(self)
        self.tipo = tipo
        self.placa = placa
        # posicionamiento en parqueadero
        self.fila = None
        self.columna = None
        self.celda = None
        self.image = self.getSprite(self.celda)
        # ubicacion una la pantalla
        self.x = (self.fila + 0.5) * c.cell_size
        self.y = (self.columna + 0.5) * c.cell_size
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.movilidad_reducida = False

    def setSprite(self, celda):
        celda = 34

        for directorio in p.iterdir():
            if directorio.parts[-1] == self.tipo:
                direcciones = [direccion for direccion in directorio.iterdir()]
                if celda % 3 == 1:
                    return random.choice(list(direcciones[0].glob('**/*.png')))
                elif celda % 3 == 0:
                    return random.choice(list(direcciones[1].glob('**/*.png')))
                else:
                    return

    def setPosicion(self, mousepos):
        self.fila = (mousepos[0] - c.FORM_WIDTH) // c.cell_size
        self.columna = mousepos[1] // c.cell_size
        self.celda = (self.columna * c.PARQ_COLUMNAS) + self.fila


class Auto(Vehiculo):
    pass


# otras funciones
def colocar_auto(mousepos, piso, tipo_vehiculo):
    mouse_fila = (mousepos[0] - c.FORM_WIDTH) // c.cell_size
    mouse_columna = mousepos[1] // c.cell_size
    celda = (mouse_columna * c.PARQ_COLUMNAS) + mouse_fila
    if c.pisos[piso][celda] == tipo_vehiculo:
        pass


class Moto(Vehiculo):
    pass


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
            return True
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

    def existeCelda(self, celda):
        if self.estaVacia():
            return False
        temp = self.head
        if temp.auto.ubicacion == celda:
            return True
        while temp.next != self.head:
            temp = temp.next
            if temp.auto.ubicacion == celda:
                return True
        return False
