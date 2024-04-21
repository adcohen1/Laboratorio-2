import random
from pathlib import Path
import pygame as pg
import constantes as c

# Ruta donde se van a buscar las imagenes
p = Path('./sprites')


class Sprite(pg.sprite.Sprite):
    def __init__(self, sprite, fila, columna):
        pg.sprite.Sprite.__init__(self)
        # posicionamiento en parqueadero
        self.fila = fila
        self.columna = columna
        # ubicacion en la pantalla
        self.image = sprite
        self.x = (self.fila + 0.5) * c.cell_size
        self.y = (self.columna + 0.5) * c.cell_size
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


def colocarAuto(sprite, mousepos, piso, tipo_vehiculo):
    mouse_fila = (mousepos[0] - c.FORM_WIDTH) // c.cell_size
    mouse_columna = mousepos[1] // c.cell_size
    celda = (mouse_columna * c.PARQ_COLUMNAS) + mouse_fila
    if c.pisos[piso][celda] == tipo_vehiculo:
        # Verificar que el lugar esté desocupado
        celda_esta_libre = True
        for v in grupoVehiculos:
            if (mouse_fila, mouse_columna) == (v.fila, v.columna):
                celda_esta_libre = False
            if celda_esta_libre:
                pass


def seleccionarImagen(mouse_x, tipo):
    direc = ((mouse_x - c.FORM_WIDTH) // c.cell_size % 3) // 2
    for directorio in p.iterdir():
        if directorio.parts[-1] == tipo:
            direcciones = [direccion for direccion in directorio.iterdir()]
            return random.choice(list(direcciones[direc].glob('**/*.png')))


class Vehiculo:
    def __init__(self, placa, entrada, salida, sprite):
        self.placa = placa
        self.hora_entrada = entrada
        self.hora_salida = salida
        self.sprite = sprite


class Auto(Vehiculo):
    def __init__(self, sprite, tipo, placa, fila, movilidad_reducida=False):
        super().__init__(sprite, tipo, placa, fila)
        self.movilidad_reducida = movilidad_reducida


class Moto(Vehiculo):
    # ubicacion una la pantalla
    def __init__(self, tipo, placa, fila):
        super().__init__(tipo, placa, fila)
        pass


# Lista de autos estacionados
class Nodo:
    def __init__(self, vehiculo, sprite):
        self.sprite = sprite
        self.dato = vehiculo
        self.next = None


class ListaAutos:
    def __init__(self):
        self.head = None

    def agregarAuto(self, auto, sprite):
        if self.estaVacia():
            head = Nodo(auto, sprite)
            head.next = head
            return True
        if self.existeAuto(auto.placa):
            return False
        head = self.head
        if head.next is head:
            head.next = Nodo(auto, sprite)
            head.next.next = head
        else:
            temp = head.next
            while temp.next != head:
                temp = temp.next
            temp.next = Nodo(auto, sprite)
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
