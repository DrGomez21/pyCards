import carta as c
import ataques.ataque as atq
import tablero
from jugador import Jugador
from os import system

class Juego():

    def __init__(self, tab, player1, player2):
        self.tab = tab
        self.player1 = player1
        self.player2 = player2

    def __validar_estado(self, jugador):
        if jugador.magia == 0:
            return True
        for card in jugador.mazo:
            if card.ps_actual > 0:
                return False
        return True

    def jugar(self, player1, player2):
        while True:
            # Vemos nuestra mano de cartas.
            self.player1.mostrar_mazo()
            # Elegimos la carta con que comenzar.
            self.player1.escoger_carta()

            # El rival ve sus cartas.
            self.player2.mostrar_mazo()
            # El rival escoge.
            self.player2.escoger_carta()

            # Lanzamos un ataque.
            self.player1.jugador_atacar(self.player2, self.tab)
            # El rival ataca.
            if self.player2.carta_activa.ps_actual > 0:
                self.player2.jugador_atacar(self.player1, self.tab)
            # Imprimimos un divisor
            print('======================')

            # Mostramos ps de las cartas activas.
            print('=====\nMarcador\n=====')
            print(f'{self.player1.nombre} tu carta tiene: {self.player1.carta_activa.ps_actual} PS')
            print('----------')
            print(f'{self.player2.nombre} tu carta tiene: {self.player2.carta_activa.ps_actual} PS')
            print('----------')

            if self.__validar_estado(self.player1):
                self.ganador = self.player2
                break
            elif self.__validar_estado(player2):
                self.ganador = self.player1
                break
    
    def ver_ganador(self):
        print('El ganador es: ')
        self.ganador.ver_datos_jugador()

