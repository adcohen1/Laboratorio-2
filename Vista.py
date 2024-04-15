import pygame as pg
import constantes as c

screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
pg.display.set_caption('El Parqueadero')

park = pg.image.load('park.png').convert_alpha()

clock = pg.time.Clock()
run = True

while run:

    clock.tick(c.FPS)
    screen.fill((100, 100, 100))

    screen.blit(park, (c.FORM_WIDTH, 0))

    for event in pg.event.get():
        # cerrar el juego
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()
