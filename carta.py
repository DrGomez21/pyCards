import abc
from ataques import attack as atq

class Carta(metaclass=abc.ABCMeta):
    '''Abstraccion de una carta en el juego'''

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    @abc.abstractmethod
    def __str__(self):
        '''Se indica cual carta fue utilizada.'''
        pass

    @abc.abstractmethod
    def recibir_danho(self, atacante):
        pass

class CartaBasica(Carta):
    '''Abstraccion del elemento Carta Basica en el juego'''
    
    def __init__(self, nombre, descripcion, ps, costo_perder, ataque, img, img_hover):
        super().__init__(nombre, descripcion)
        self.ps = ps
        self.costo_perder = costo_perder
        self.ps_actual = ps
        self.ataque = ataque
        self.img = img
        self.img_hover = img_hover

    def obtener_pts_ataque(self):
        '''Obtenemos el valor del ataque de la carta'''
        return self.ataque.obtener_puntos_ataque()
    
    def recibir_danho(self, atacante):
        '''Sobre la salud de nuestra carta, 
        le quitamos el ataque de la carta atacante'''
        self.ps_actual -= atacante.obtener_pts_ataque()
        if self.ps_actual < 0:
            self.ps_actual = 0

    def nuevo_atacar(self, carta_que_recibe):
        carta_que_recibe.recibir_danho(self)

    def __str__(self):
        return 'Carta Basica'      

class CartaMagica(Carta):
    '''Abstraccion del elemento Carta Magica en el juego.
    Implementacion a futuro'''
    
    def __init__(self, nombre, descripcion, ps, costo_perder, ataque, reserva_magica):
        super().__init__(nombre, descripcion)
        self.ps = ps
        self.costo_perder = costo_perder
        self.ps_actual = ps
        self.ataque = ataque
        self.reserva_magica = reserva_magica

    def obtener_pts_ataque(self):
        '''Obtenemos el valor del ataque de la carta'''
        return self.ataque.obtener_puntos_ataque()

    def recibir_danho(self, atacante):
        '''Sobre la salud de nuestra carta, 
        le quitamos el valor de ataque de la carta atacante'''
        self.ps_actual -= atacante.obtener_pts_ataque()
        if self.ps_actual < 0:
            self.ps_actual = 0
    
    def nuevo_atacar(self, carta_que_recibe):
        '''Efecto de ataque en las cartas'''
        carta_que_recibe.recibir_danho(self)

    def __jugar_atq_especial(self):
        '''Se indica el uso de la resera de magia con la que cuenta la carta.
        Implementacion a futuro'''
        pass

    def __str__(self):
        return 'Carta Magica'

class CartaAmbulancia(Carta):
    '''Abstraccion del elemento de carta ambulancia
    Esta carta cura la salud de una carta'''

    def __init__(self):
        super().__init__('Ambulancia', 'Permite curar una carta del mazo')
        self.salud_recuperable = 5

    def sanar(self, segunda_carta):
        segunda_carta.ps_actual += self.salud_recuperable
        if segunda_carta.ps_actual >= segunda_carta.ps:
            segunda_carta.ps_actual = segunda_carta.ps  
        return f'Carta curada con {self.salud_recuperable}PS'

    def recibir_danho(self, atacante):
        '''Implementacion futura'''
        pass

    def __str__(self):
        return 'Carta Ambulancia'
