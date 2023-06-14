from jugador import Jugador
import carta as c
from ataques import attack as atq
from os import system

class Juego():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turno = 0   # Gestión de turnos en el juego

    def interaccion(self, atacante, receptor):
        '''Se gestiona la lucha entre dos cartas.'''
        atacante.jugador_atacar(receptor)

        return f'La carta {atacante.carta_activa.nombre} ataca a {receptor.carta_activa.nombre} con {atacante.carta_activa.ataque.__str__()}'

    def player1_ataca(self):
        '''Ataque del primer jugador.'''
        return self.interaccion(self.player1, self.player2)

    def player2_ataca(self):
        '''Ataque del segundo jugador.'''
        return self.interaccion(self.player2, self.player1)
