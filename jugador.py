from carta import Carta
import ataques.ataque
from os import system

class Jugador():

    def __init__(self, nombre, mazo, magia):
        self.nombre = nombre
        self.mazo = mazo
        self.magia = magia
        self.carta_activa = mazo[0] # Por defecto la primera carta es la carta activa

    # Mostrar el mazo del jugador.
    def mostrar_mazo(self):
        '''Esta función imprimie en pantalla las cartas del jugador'''
        print('----------')
        print(f'Mazo de {self.nombre} | Magia: {self.magia}')
        i = 0   # Contador de numero de carta.
        for c in self.mazo:
            print(f'{i})')
            i += 1
            if c.ps_actual > 0:
                c.ver_informacion()
        print('----------')

    # Al escoger una carta, el jugador lanza esa misma al tablero.
    def escoger_carta(self):
        '''Este metodo permite al usuario seleccionar una carta
        de su mazo para lanzarla, valida la elección y limpia la terminal'''
        index = int(input('Elige tu carta: '))
        # validamos la entrada.
        while index < 0 or index >= len(self.mazo):
            index = int(input('Elige tu carta: '))
        
        # TODO: Eliminar del array de mazo las cartas que ya no tienen PS
        self.carta_activa = self.mazo[index]
        system('cls')   # Limpiar la pantalla del terminal.
        self.carta_activa.lanzar()

    def jugador_atacar(self, rival, tablero):
        # Que pasa conmigo.
        self.magia = self.carta_activa.atacar(self.magia)   # Se reducen mis puntos de Magia
        # Que pasa con el Rival
        rival.carta_activa.ps_actual -= self.carta_activa.ataque.obtener_puntos_ataque() + tablero.potenciar()
        
        if rival.carta_activa.ps_actual <= 0:
            rival.magia = rival.carta_activa.retirar(rival.magia)
            rival.carta_activa.ps_actual = 0

    def ver_datos_jugador(self):
        print('==================================')
        print(f'======NOMBRE: {self.nombre} ======')
        print(f'======MAGIA: {self.magia} ======')
        print(f'======CARTA: {self.carta_activa.nombre} ======')
        print('==================================')
        
