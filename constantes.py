# dimensiones de la ventana
WIDTH = 1980
HEIGHT = 1080

# dimensiones del panel del paqueadero
PARQ_WIDTH = 1380
PARQ_HEIGHT = 1080
PARQ_FILAS = 20
PARQ_COLUMNAS = 25
# dimensiones de la celda
cell_size = 54

# dimensiones del panel formulario de ingreso
FORM_WIDTH = 600
FORM_HEIGHT = 1080

FPS = 60

# pisos np parqueadero = 0, parqueadero auto = 10 (ocupado = 11), parqueadero moto = 20 (ocupado = 21)
# parqueadero movilidad reducida = 30 (ocupado = 31)
pisos = {
    "primero": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 30, 0, 30, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 0,
                0, 0, 0, 30, 0, 30, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 0,
                0, 0, 0, 30, 0, 30, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 0,
                0, 0, 0, 30, 0, 30, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 0,
                0, 0, 0, 30, 0, 30, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                ],
    "segundo": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 30, 0, 30, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 0,
                0, 0, 0, 30, 0, 30, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 0,
                0, 0, 0, 30, 0, 30, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 0,
                0, 0, 0, 30, 0, 30, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 0,
                0, 0, 0, 30, 0, 30, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                ],
    "tercero": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 30, 0, 30, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 0,
                0, 0, 0, 30, 0, 30, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 0,
                0, 0, 0, 30, 0, 30, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 0,
                0, 0, 0, 30, 0, 30, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 0,
                0, 0, 0, 30, 0, 30, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 10, 0, 10, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 20, 0, 20, 10, 0, 10, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                ]
}
