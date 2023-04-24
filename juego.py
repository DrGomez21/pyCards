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
        '''Corrobora si existe algun jugador derrotado'''
        if jugador.magia <= 0:  # Si la magia del jugador es cero, entonces pierde.
            return True
        for card in jugador.mazo:   # Si alguna carta aún tiene PS, no pierde el combate.
            if card.ps_actual > 0:
                return False
        return True

    def __mostrar_marcador(self, p1, p2):
        '''Despliega en pantalla los PS de las cartas activas'''
        # Mostramos ps de las cartas activas.
        print('\n=====\nMarcador\n=====')
        print(f'{p1.nombre} tu carta {p1.carta_activa.nombre} tiene: {p1.carta_activa.ps_actual}/{p1.carta_activa.ps} PS')
        print('----------')
        print(f'{p2.nombre} tu carta {p2.carta_activa.nombre} tiene: {p2.carta_activa.ps_actual}/{p2.carta_activa.ps} PS')
        print('=====')

        # Agregamos un intro para continuar.
        input('Presiona una tecla para seguir...')
        system('cls')   # Limpiamos la pantalla para seguir jugando.

    def jugar(self, player1, player2):
        '''Metodo que contiene la logica del juego'''
        system('cls')
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

            # Mostramos ps de las cartas activas.
            self.__mostrar_marcador(self.player1, self.player2)

            if self.__validar_estado(self.player1):
                self.ganador = self.player2
                break
            elif self.__validar_estado(self.player2):
                self.ganador = self.player1
                break
    
    def ver_ganador(self):
        '''Metodo para mostrar el ganador de la partida'''
        print('El ganador es: ')
        self.ganador.ver_datos_jugador()

