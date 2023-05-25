import abc

# Clase abstracta para cualquier ataque.
class Ataque(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def obtener_puntos_ataque(self):
        '''Nos retorna el valor de daño del ataque lanzado'''
        pass
    
    @abc.abstractmethod
    def __str__(self):
        '''Nos retorna el nombre ataque lanzado'''
        pass

class Derribo(Ataque):
    '''Abstraccion de un ataque Derribo'''
    def obtener_puntos_ataque(self):
        return 3

    def __str__(self):
        return 'Derribo'

class FuerzaPsiquica(Ataque):

    def obtener_puntos_ataque(self):
        return 5

    def __str__(self):
        return 'Fuerza Psiquica'    # Retorna el nombre del ataque.

class CartaDelJuicio(Ataque):

    def obtener_puntos_ataque(self):
        return 8

    def __str__(self):
        return 'Carta del juicio'    # Retorna el nombre del ataque.
