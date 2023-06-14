import carta as c
from ataques import attack as atq

class Jugador():

    def __init__(self, nombre, mazo, magia):
        self.nombre = nombre
        self.mazo = mazo
        self.magia = magia
        self.carta_activa = mazo[0] # Por defecto la primera carta es la carta activa
        self.curaciones = 4
        self.botiquin = c.CartaAmbulancia()

    def escoger_carta(self):
        '''Este metodo permite al usuario seleccionar una carta de su mazo para lanzarla.'''
        index = int(input('Elige tu carta: '))
        while index < 0 or index >= len(self.mazo):
            print('Esa carta no esta disponible ahora')
            index = int(input('Elige tu carta: '))
        
        self.carta_activa = self.mazo[index]

    def lanzar_carta(self):
        '''Se indica la carta con la que vas a jugar ese turno.'''
        return f'{self.nombre} lanza la {self.carta_activa.__str__()} {self.carta_activa.nombre}'

    def retirar_carta(self):
        '''Cuando una carta es derrotada
        el jugador pierde una cantidad de magia'''
        self.magia -= self.carta_activa.costo_perder
        # self.__actualizar_mazo()

    def __actualizar_mazo(self):
        '''Esta funcion actualiza las cartas del mazo,
        retirando las cartas debilitadas'''
        for c in self.mazo:
            if c.ps_actual <= 0:
                self.mazo.remove(c)
                # Devuelve la posicion del elemento.
                # return self.mazo.index(c)

    def curar_carta(self):
        if self.curaciones > 0:
            if  self.carta_activa.ps_actual == self.carta_activa.ps:
                return 'No puedes curar esta carta'
            self.curaciones -= 1
            return self.botiquin.sanar(self.carta_activa)
        else:
            return 'Ya no te quedan curaciones :('

    def jugador_atacar(self, rival):
        # Que pasa conmigo.
        # self.magia = self.carta_activa.atacar(self.magia) ---> Se reducen mis puntos de Magia
        
        self.carta_activa.nuevo_atacar(carta_que_recibe=rival.carta_activa)
        
        if rival.carta_activa.ps_actual <= 0:
            self.retirar_carta()
            rival.carta_activa.ps_actual = 0
