import pygame as pg

import Clases
import constantes as c

screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
pg.display.set_caption('El Parqueadero')

piso1 = pg.image.load('piso1.png').convert_alpha()
piso2 = pg.image.load('piso2.png').convert_alpha()
piso3 = pg.image.load('piso3.png').convert_alpha()

clock = pg.time.Clock()
run = True

vehiculo = None
sprite = None
piso = piso1

# Grupos
grupoTemporal = pg.sprite.Group()
grupoVehiculos = pg.sprite.Group()


while run:

    # clock.tick(c.FPS)
    screen.fill((100, 100, 100))

    screen.blit(piso, (c.FORM_WIDTH, 0))
    grupoVehiculos.draw(screen)
    if sprite:
        # screen.blit(sprite.image, (sprite.x, sprite.y))
        grupoTemporal.draw(screen)

    for event in pg.event.get():
        # cerrar el juego
        if event.type == pg.QUIT:
            run = False

        # cuando se selecciona un lugar para aparcar se crea la imagen para el nuevo vehículo
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pg.mouse.get_pos()
            if c.FORM_WIDTH < mouse_pos[0] < c.WIDTH and 0 < mouse_pos[1] < c.HEIGHT:
                mouse_fila = mouse_pos[0] // c.cell_size
                mouse_columna = mouse_pos[1] // c.cell_size
                celda = mouse_columna * c.PARQ_COLUMNAS + ((mouse_pos[0] - c.FORM_WIDTH) // c.cell_size)
                if c.pisos["primero"][celda] != 0:
                    imagen = pg.image.load(Clases.seleccionarImagen(mouse_pos[0], 'Autos'))
                    # screen.blit(imagen, (mouse_pos[0], mouse_pos[1]))
                    sprite = Clases.Sprite(imagen, mouse_fila, mouse_columna)
                    grupoTemporal.empty()
                    grupoTemporal.add(sprite)

        if event.type == pg.MOUSEBUTTONDOWN and event.button == pg.BUTTON_RIGHT:
            grupoVehiculos.add(sprite)
            sprite = None
            grupoTemporal.empty()
            print(3)

                # auto = Clases.Auto('Auto', '125-wdf', mouse_pos[0], mouse_pos[1])
                # Clases.colocarAuto(auto, mouse_pos, 'primero', 30)

    pg.display.flip()
