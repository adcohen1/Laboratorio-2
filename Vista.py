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

while run:

    # clock.tick(c.FPS)
    screen.fill((100, 100, 100))

    screen.blit(piso1, (c.FORM_WIDTH, 0))

    for event in pg.event.get():
        # cerrar el juego
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pg.mouse.get_pos()
            if c.FORM_WIDTH < mouse_pos[0] < c.PARQ_WIDTH and 0 < mouse_pos[1] < c.PARQ_HEIGHT:
                # primero se deben capturar los datos tipo de vehiculo y piso del parqueadero
                # otra opcion es que el usuario elija el lugar y se capturan los datos de ese punto
                Clases.colocar_auto(mouse_pos, 'primero', 30)

    pg.display.flip()
