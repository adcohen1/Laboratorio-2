import pygame as pg

import constantes as c

screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
pg.display.set_caption('El Parqueadero')

piso1 = pg.image.load('piso1.png').convert_alpha()
piso2 = pg.image.load('piso2.png').convert_alpha()
piso3 = pg.image.load('piso3.png').convert_alpha()
panel = pg.image.load('Panel_lateral.png').convert_alpha()

clock = pg.time.Clock()
run = True

while run:

    # clock.tick(c.FPS)
    screen.fill((100, 100, 100))

    screen.blit(piso1, (c.FORM_WIDTH, 0))
    screen.blit(panel, (0, 0))

    for event in pg.event.get():
        # cerrar el juego
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()
