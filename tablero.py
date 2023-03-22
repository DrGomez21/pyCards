import abc
import random

class Tablero(metaclass=abc.ABCMeta):
    def __init__(self, habilidad):
        self.habilidad = habilidad  # Nombre de la habilidad del tablero.
    
    @abc.abstractmethod
    def potenciar(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        return '{} por {}'.format(self.habilidad, self.potenciador)

class TableroBasico(Tablero):
    def __init__(self, habilidad):
        super().__init__(habilidad)
    
    def potenciar(self):
        ''' Valor por el que se suma la fuerza de un ataque como efecto del tablero'''
        return 0    # No potencia ningun ataque

    def __str__(self):
        return '{} por {}'.format(self.habilidad, self.potenciar())

class TableroEspecial(Tablero):
    def __init__(self, habilidad):
        super().__init__(habilidad)
    
    def potenciar(self):
        ''' Valor por el que se suma la fuerza de un ataque como efecto del tablero'''
        if self.lanzar_moneda() % 2 == 0:
            return 3
        else:
            return 1

    def lanzar_moneda(self):
        return random.randint(0, 10)

    def __str__(self):
        return '{} por {}'.format(self.habilidad, self.potenciar())