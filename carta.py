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
        return magia - 0

    def ver_informacion(self):
        print('=' * 10)
        print('Carta Basica: ', self.nombre)
        print(f'Descripcion: {self.descripcion}')
        print(f'Ataque: {self.ataque} danho: {self.ataque.obtenerPuntoAtaque()}')
        print('-' * 6)
        print(f'PS: {self.ps_actual}\tCosto: {self.costo_perder} M')
        print('=' * 10)        

class CartaMagica(Carta):
    
    def __init__(self, nombre, descripcion, ps, costo_perder, ataque):
        super().__init__(nombre, descripcion)
        self.ps = ps
        self.costo_perder = costo_perder
        self.ps_actual = ps
        self.ataque = ataque
    
    def lanzar(self):
        print('Lanzando la carta magica ', self.nombre)
    
    def retirar(self, magia):
        print(f'La carta mágica {self.nombre} fue retirada')
        return magia - self.costo_perder

    def atacar(self, magia):
        print(f'La carta magica {self.nombre} ataca con {self.ataque}')
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

class CartaApoyo(Carta):
    def __init__(self, nombre, descripcion):
        super().__init__(nombre, descripcion)
    
    def lanzar(self):
        print('Lanzando la carta de apoyo ', self.nombre)
    
    def retirar(self, magia):
        print(f'La carta de apoyo {self.nombre} fue retirada')

    def ver_informacion(self):
        print('=' * 10)
        print('Carta: ', self.nombre)
        print(f'Descripcion: {self.descripcion}')
        print('=' * 10)

