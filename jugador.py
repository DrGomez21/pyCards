from carta import Carta
import ataques.ataque
from os import system

class Jugador():

    def __init__(self, nombre, mazo, magia):
        self.nombre = nombre
        self.mazo = mazo
        self.magia = magia
        self.carta_activa = mazo[0] # ¨Por defecto la primera carta es la carta activa

    # Mostrar el mazo del jugador.
    def mostrar_mazo(self):
        print(f'Mazo de {self.nombre}\tMagia: {self.magia}')
        i = 0
        for c in self.mazo:
            print(f'{i})', end=' ')
            i += 1
            if c.ps_actual > 0:
                c.ver_informacion()

    # Al escoger una carta, el jugador lanza esa misma al tablero.
    def escoger_carta(self):
        index = int(input('Elige tu carta: '))
        # validamos la entrada.
        while index < 0 or index >= len(self.mazo):
            index = int(input('Elige tu carta: '))
        self.carta_activa = self.mazo[index]
        system('cls')   # Limpiar la pantalla del terminal.
        self.carta_activa.lanzar()

    def jugador_atacar(self, rival, tablero):
        # Que pasa conmigo.
        magia = self.carta_activa.atacar(self.magia)
        # Que pasa con el Rival
        rival.carta_activa.ps_actual -= self.carta_activa.ataque.obtenerPuntoAtaque() + tablero.potenciar()
        
        if rival.carta_activa.ps_actual < 0:
            rival.carta_activa.ps_actual = 0

    def ver_datos_jugador(self):
        print('==================================')
        print(f'======NOMBRE: {self.nombre}======')
        print(f'======MAGIA: {self.magia}======')
        print(f'======CARTA: {self.carta_activa.nombre}======')
        print('==================================')
        
