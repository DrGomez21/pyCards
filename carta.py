import abc
import ataques.ataque as atq

class Carta(metaclass=abc.ABCMeta):
    
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def lanzar(self):
        pass

    def retirar(self):
        pass

    def ver_informacion(self):
        pass

class CartaBasica(Carta):
    
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
        print(f'Ataque: {self.ataque} danho: {self.ataque.obtenerPuntoAtaque()}')
        print('-' * 6)
        print(f'PS: {self.ps_actual}\tCosto: {self.costo_perder} M')
        print('=' * 10)        

class CartaMagica(Carta):
    
    def __init__(self, nombre, descripcion, ps, costo_perder, ataque, reserva_magica):
        super().__init__(nombre, descripcion)
        self.ps = ps
        self.costo_perder = costo_perder
        self.ps_actual = ps
        self.ataque = ataque
        self.reserva_magica = reserva_magica
    
    def lanzar(self):
        print('Lanzando la carta magica ', self.nombre)
    
    def retirar(self, magia):
        print(f'La carta magica {self.nombre} fue retirada')
        return magia - self.costo_perder

    def atacar(self, magia):
        print(f'La carta magica {self.nombre} ataca con {self.ataque}')
        if self.reserva_magica > 0:
            self.reserva_magica - self.costo_perder
            return magia
        return magia - self.costo_perder    # Atacar tiene un costo de magia del jugador.
    
    def jugar_atq_especial(self, magia):
        print(f'{self.nombre} juega su ataque especial de magia')
        return magia - 4

    def ver_informacion(self):
        print('=' * 10)
        print('Carta Magica: ', self.nombre)
        print(f'Descripcion: {self.descripcion}')
        print(f'Ataque: {self.ataque} danho: {self.ataque.obtenerPuntoAtaque()}')
        print('-' * 6)
        print(f'PS: {self.ps_actual}\tCambio: {self.costo_perder} M')
        print('=' * 10)
