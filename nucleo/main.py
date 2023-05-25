
import juego
import jugador as j
import carta as c
import ataques.attack as atq
import utiles

class App():
    
    def __init__(self):
        self.player1 = self.crear_jugador()
        self.player2 = self.crear_jugador()
        self.juego = juego.Juego(self.player1, self.player2)

    def menu_bienvenida(self):
        '''Mostramos una pantalla de bienvenida para el juego.'''
        print(utiles.logotipo)
        utiles.decorar_opcion(1, 'Empezar juego')
        utiles.decorar_opcion(2, 'Instrucciones')
        utiles.decorar_opcion(3, 'Salir')
        opcion = input('Elige una opcion: ')

        # Ciclo para el menu del juego
        while not self.validar_entrada(opcion):
            print('Parece que esa opcion no esta disponible')
            opcion = input('Elige una opcion: ')

        # Mapeamos la acción.
        if opcion == '1':
            self.comenzar()
        elif opcion == '2':
            utiles.limpiar()
            self.mostrar_instrucciones()
        else:
            quit()

    def mostrar_instrucciones(self):
        '''Traemos las instrucciones del juego para mostrarselas al jugador'''
        print(utiles.obtener_intrucciones())
        input('Presiona una tecla para jugar...')
        self.comenzar()

    def crear_jugador(self):
        '''Creamos a un jugador de la partida'''
        nombre = input('¿Como te llamas?: ')
        return j.Jugador(nombre, [
            c.CartaBasica('Messi', 'Mundial', 10, 4, atq.Derribo()),
            c.CartaBasica('CR7', 'SIIIUUU', 12, 3, atq.CartaDelJuicio())
        ], 10) 

    def comenzar(self):
        '''Se muestran por pantalla las acciones del juego'''
        utiles.limpiar()
        while True:
            self.iniciar_vista_combate(self.player1)
            utiles.limpiar()
            self.iniciar_vista_combate(self.player2)
            utiles.limpiar()

            print(self.juego.player1_ataca())
            if self.player2.carta_activa.ps_actual > 0:
                print(self.juego.player2_ataca())
            # Mostrar el marcador
            self.mostrar_stats(self.player1, self.player2)

            # Asignamos un ganador
            if self.__validar_estado(self.player2):
                self.ganador = self.player1
                break
            elif self.__validar_estado(self.player1):
                self.ganador = self.player2
                break
        print('El ganador es:', self.ganador.nombre)
    
    def __validar_estado(self, jugador):
        '''Corrobora si existe algun jugador derrotado'''
        if jugador.magia <= 0:  # Si la magia del jugador es cero, entonces pierde.
            return True
        for card in jugador.mazo:   # Si alguna carta aún tiene PS, no pierde el combate.
            if card.ps_actual > 0:
                return False
        return True

    def escoger_carta(self, player):
        '''Este metodo permite al jugador seleccionar una carta de su mazo para lanzarla.'''
        while True:
            try:
                index = int(input('Elige tu carta: '))
                if index < 0 or index >= len(player.mazo):
                    print('Esa carta no esta disponible...')
                else:
                    player.carta_activa = player.mazo[index]
                    break
            except ValueError:
                print('Ups, parece que esa carta no esta disponible...')

    def iniciar_vista_combate(self, player):
        '''Muestra el menu de acciones al jugador,
        mapea la accion seleccionada.'''
        turno = True
        while (turno):
            accion = self.mostrar_menu_accion(player)

            if accion == '1':
                self.vista_jugador_ataca(player)
                turno = False
            if accion == '2':
                self.vista_curar_carta(player)
            if accion == '3':
                quit()
                break

    def vista_jugador_ataca(self, player):
        '''Procedimiento que permite mostrar el mazo de cartas al jugador,
        tambien escoger una carta de dicho mazo'''
        self.mostrar_mazo(player)
        self.escoger_carta(player)

    def vista_curar_carta(self, player):
        '''Se escoge una carta del mazo para curarla'''
        self.mostrar_mazo(player)
        self.escoger_carta(player)
        print(player.curar_carta())

    def ver_informacion_carta(self, carta):
        '''Se muestra en pantalla la informacion de una carta'''
        print('=' * 10)
        print(f'{carta.__str__()}: {carta.nombre}')
        print(f'Descripcion: {carta.descripcion}')
        print(f'Ataque: {carta.ataque}')
        print(f'Danho: {carta.ataque.obtener_puntos_ataque()}')
        print('-' * 6)
        print(f'PS: {carta.ps_actual}  Costo: {carta.costo_perder}M')
        print('=' * 10)

    def mostrar_mazo(self, player):
        '''Esta función imprimie en pantalla las cartas del jugador'''
        print('----------')
        print(f'Mazo de {player.nombre} | Magia: {player.magia}')
        i = 0   # Contador de numero de carta.
        for c in player.mazo:
            print(f'{i})')
            self.ver_informacion_carta(c)
            i += 1
        print('----------')

    def validar_entrada(self, opcion):
        '''Funcion que ayuda a validar entradas en menus'''
        return opcion in ('1', '2', '3')

    def mostrar_menu_accion(self, player):
        '''Se muestra a los usuarios las acciones disponibles en su turno'''
        print(f'-- Turno de: {player.nombre} --')
        print('1) Lanzar ataque')
        print('2) Curar carta')
        print('3) Salir (sin guardar)')
        opcion = input('Que quieres hacer? ')

        while not self.validar_entrada(opcion):
            print('Ups, parece que la opcion no esta disponible')
            opcion = input('Que quieres hacer? ')
        # Despejamos la pantalla
        utiles.limpiar()
        return opcion

    def mostrar_stats(self, p1, p2):
        '''Despliega en pantalla los PS de las cartas activas'''
        # Mostramos ps de las cartas activas.
        print('\n=====\nMarcador\n=====')
        print(f'{p1.nombre} tu carta {p1.carta_activa.nombre} tiene: {p1.carta_activa.ps_actual}/{p1.carta_activa.ps} PS')
        if p1.carta_activa.ps_actual <= 0:
            print(f'{p1.nombre} tu carta {p1.carta_activa.nombre} fue retirada...')
            p1.retirar_carta()
        print('----------')
        
        print(f'{p2.nombre} tu carta {p2.carta_activa.nombre} tiene: {p2.carta_activa.ps_actual}/{p2.carta_activa.ps} PS')
        if p2.carta_activa.ps_actual <= 0:
            print(f'{p2.nombre} tu carta {p2.carta_activa.nombre} fue retirada...')
            p2.retirar_carta()
        print('=====')

        # Agregamos un intro para continuar.
        input('Presiona una tecla para seguir...')
        utiles.limpiar()   # Limpiamos la pantalla para seguir jugando.

if __name__ == '__main__':
    App().menu_bienvenida()