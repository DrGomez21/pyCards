import abc
import ataques.ataque as atq

class Carta(metaclass=abc.ABCMeta):
    '''Abstraccion de una carta en el juego'''

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    @abc.abstractmethod
    def lanzar(self):
        pass

    @abc.abstractmethod
    def retirar(self):
        pass

    @abc.abstractmethod
    def ver_informacion(self):
        pass

class CartaBasica(Carta):
    '''Abstraccion del elemento Carta Basica en el juego'''
    
    def __init__(self, nombre, descripcion, ps, costo_perder, ataque):
        super().__init__(nombre, descripcion)
        self.ps = ps
        self.costo_perder = costo_perder
        self.ps_actual = ps
        self.ataque = ataque

    def lanzar(self):
        print('Lanzando la carta basica ', self.nombre)
    
    def retirar(self, magia):
        print(f'La carta basica {self.nombre} fue retirada')
        return magia - self.costo_perder

    def atacar(self, magia):
        print(f'La carta basica {self.nombre} ataca con {self.ataque}')
        return magia - 2

    def ver_informacion(self):
        print('=' * 10)
        print('Carta Basica: ', self.nombre)
        print(f'Descripcion: {self.descripcion}')
        print(f'Ataque: {self.ataque} danho: {self.ataque.obtener_puntos_ataque()}')
        print('-' * 6)
        print(f'PS: {self.ps_actual}\tCosto: {self.costo_perder} M')
        print('=' * 10)        

class CartaMagica(Carta):
    '''Abstraccion del elemento Carta Magica en el juego'''
    
    def __init__(self, nombre, descripcion, ps, costo_perder, ataque, reserva_magica):
        super().__init__(nombre, descripcion)
        self.ps = ps
        self.costo_perder = costo_perder
        self.ps_actual = ps
        self.ataque = ataque
        self.reserva_magica = reserva_magica
    
    def lanzar(self):
        '''Se indica a los jugadores cual carta fue utilizada en el turno actual'''
        print('Lanzando la carta magica ', self.nombre)
    
    def retirar(self, magia):
        '''Cuando una carta es retirada, el jugador afectado sufre una penalizacion en sus puntos de magia, equivalente a un valor determinado'''
        print(f'La carta magica {self.nombre} fue retirada')
        return magia - self.costo_perder

    def atacar(self, magia):
        '''Las cartas pueden realizar ataques, 
        en caso que una carta cuente con una reserva de magia, esta se utilizara
        antes que los puntos de magia reales de la carta en cuestion'''

        print(f'La carta magica {self.nombre} ataca con {self.ataque}')
        if self.reserva_magica > 0:
            self.reserva_magica - self.costo_perder
            self.jugar_atq_especial()
            return magia
        return magia - self.costo_perder    # Atacar tiene un costo de magia del jugador.
    
    def jugar_atq_especial(self):
        '''Se indica el uso de la resera de magia con la que cuenta la carta'''
        print(f'>> {self.nombre} juega su reserva especial de magia')

    def ver_informacion(self):
        '''Se muestra en pantalla la informacion de la carta'''
        
        print('=' * 10)
        print('Carta Magica: ', self.nombre)
        print(f'Descripcion: {self.descripcion}')
        print(f'Ataque: {self.ataque} danho: {self.ataque.obtener_puntos_ataque()}')
        print('-' * 6)
        print(f'PS: {self.ps_actual}\tCambio: {self.costo_perder} M')
        print('=' * 10)
