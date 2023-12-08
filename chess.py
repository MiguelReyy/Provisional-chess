import os

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class Ficha:
    def __init__(self, figura, movimientos_validos):
        self.figura = figura
        self.movimientos_validos = movimientos_validos

    def presentarse(self):
        print(f"Soy la ficha {self.figura} y me puedo mover a {self.movimientos_validos}")

class Torre(Ficha):
    def __init__(self):
        super().__init__("♖", [(i, 0) for i in range(-7, 8)] + [(0, j) for j in range(-7, 8)])

class Peon(Ficha):
    def __init__(self):
        super().__init__("♙", [(1, 0), (2, 0)])

class Caballo(Ficha):
    def __init__(self):
        super().__init__("♘", [(i, j) for i in range(-2, 3) for j in range(-2, 3) if abs(i) + abs(j) == 3])

class Alfil(Ficha):
    def __init__(self):
        super().__init__("♗", [(i, i) for i in range(-7, 8)] + [(i, -i) for i in range(-7, 8)])

class Reina(Ficha):
    def __init__(self):
        super().__init__("♕", [(i, 0) for i in range(-7, 8)] + [(0, j) for j in range(-7, 8)] +
                         [(i, i) for i in range(-7, 8)] + [(i, -i) for i in range(-7, 8)])

class Rey(Ficha):
    def __init__(self):
        super().__init__("♔", [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)])

def imprimir_tablero(tablero):
    for i in range(8):
        for j in range(8):
            casilla = tablero[(i, j)]
            if casilla:
                print(casilla.figura, end=' ')
            else:
                print(' ', end=' ')
        print()

def mover_ficha(tablero, fila_origen, columna_origen, fila_destino, columna_destino):
    ficha = tablero[fila_origen][columna_origen]
    if ficha:
        movimientos_validos = ficha.movimientos_validos
        if (fila_destino - fila_origen, columna_destino - columna_origen) in movimientos_validos:
            tablero[fila_origen][columna_origen] = None
            tablero[fila_destino][columna_destino] = ficha
            print("Ficha movida con éxito")
        else:
            print("La ficha no puede moverse a la posición especificada")
    else:
        print("No hay ficha en la posición de origen")

# Inicializar el tablero con instancias de fichas en un diccionario
tablero = {
    (i, j): None for i in range(8) for j in range(8)
}

tablero[(0, 0)] = Torre()
tablero[(0, 1)] = Caballo()
tablero[(0, 2)] = Alfil()
tablero[(0, 3)] = Rey()
tablero[(0, 4)] = Reina()
tablero[(0, 5)] = Alfil()
tablero[(0, 6)] = Caballo()
tablero[(0, 7)] = Torre()

tablero[(1, 0)] = Peon()
tablero[(1, 1)] = Peon()
tablero[(1, 2)] = Peon()
tablero[(1, 3)] = Peon()
tablero[(1, 4)] = Peon()
tablero[(1, 5)] = Peon()
tablero[(1, 6)] = Peon()
tablero[(1, 7)] = Peon()

imprimir_tablero(tablero)

fila_origen = 7
columna_origen = 0
fila_destino = 6
columna_destino = 0

mover_ficha(tablero, fila_origen, columna_origen, fila_destino, columna_destino)
imprimir_tablero(tablero)
