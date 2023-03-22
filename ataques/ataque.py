import abc

# Clase abstracta para cualquier ataque.
class Ataque(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def obtenerPuntoAtaque(self):
        pass
    
    @abc.abstractmethod
    def __str__(self):
        pass

class Derribo(Ataque):

    def obtenerPuntoAtaque(self):
        return 3

    def __str__(self):
        return 'Derribo'    # Retorna el nombre del ataque.

class FuerzaPsiquica(Ataque):

    def obtenerPuntoAtaque(self):
        return 5

    def __str__(self):
        return 'Fuerza Psiquica'    # Retorna el nombre del ataque.

class CartaDelJuicio(Ataque):

    def obtenerPuntoAtaque(self):
        return 8

    def __str__(self):
        return 'Carta del juicio'    # Retorna el nombre del ataque.

class MagicoDerribo(Ataque):

    def obtenerPuntoAtaque(self):
        return 4

    def __str__(self):
        return 'Magico Derribo'    # Retorna el nombre del ataque.

class FuerzaMagica(Ataque):

    def obtenerPuntoAtaque(self):
        return 5

    def __str__(self):
        return 'Magico Derribo'    # Retorna el nombre del ataque.

