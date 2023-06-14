import tkinter as tk
from tkinter import ttk

import juego
import jugador as j
import carta as c
import ataques.attack as atq
import utiles


class App():
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.juego = None
        self.ventana = tk.Tk()

        self.menu_bienvenida()

    def menu_bienvenida(self):
        '''Mostramos una pantalla de bienvenida para el juego.'''
        self.ventana.title("Juego de cartas")

        titulo_label = ttk.Label(self.ventana, text="Bienvenido al Juego de Cartas", font='Helvetica 16 bold')
        titulo_label.pack(pady=20)

        comenzar_button = ttk.Button(self.ventana, text='Empezar juego', command=self.comenzar)
        comenzar_button.pack()

        instrucciones_button = ttk.Button(self.ventana, text='Instrucciones', command=self.mostrar_instrucciones)
        instrucciones_button.pack()

        salir_button = ttk.Button(self.ventana, text='Salir', command=self.ventana.quit)
        salir_button.pack()

        self.ventana.mainloop()

    def mostrar_instrucciones(self):
        '''Traemos las instrucciones del juego para mostrarselas al jugador'''
        instrucciones = utiles.obtener_instrucciones()

        instrucciones_window = tk.Toplevel(self.ventana)
        instrucciones_window.title("Instrucciones")

        instrucciones_label = tk.Label(instrucciones_window, text=instrucciones, font='Helvetica 12')
        instrucciones_label.pack(padx=10, pady=10)

        volver_button = ttk.Button(instrucciones_window, text='Volver', command=instrucciones_window.destroy)
        volver_button.pack(pady=10)

    def crear_jugador(self):
        '''Creamos a un jugador de la partida'''
        nombre = input('¿Como te llamas?: ')
        return j.Jugador(nombre, [
            c.CartaBasica('Messi', 'Mundial', 10, 4, atq.Derribo()),
            c.CartaBasica('CR7', 'SIIIUUU', 12, 3, atq.CartaDelJuicio())
        ], 10) 

    def comenzar(self):
        '''Se muestran por pantalla las acciones del juego'''
        self.player1 = self.crear_jugador()
        self.player2 = self.crear_jugador()
        self.juego = juego.Juego(self.player1, self.player2)

        self.ventana.destroy()
        self.ventana = tk.Tk()
        self.ventana.title("Juego de cartas")

        self.jugador_actual_label = ttk.Label(self.ventana, text='', font='Helvetica 14 bold')
        self.jugador_actual_label.pack(pady=20)

        self.accion_label = ttk.Label(self.ventana, text='', font='Helvetica 14')
        self.accion_label.pack(pady=20)

        self.mostrar_stats(self.player1, self.player2)

        self.lanzar_ataque_button = ttk.Button(self.ventana, text='Lanzar ataque', command=self.vista_jugador_ataca)
        self.lanzar_ataque_button.pack()

        self.curar_carta_button = ttk.Button(self.ventana, text='Curar carta', command=self.vista_curar_carta)
        self.curar_carta_button.pack()

        self.salir_button = ttk.Button(self.ventana, text='Salir', command=self.ventana.quit)
        self.salir_button.pack()

        self.actualizar_jugador_actual_label()

        self.ventana.mainloop()

    def actualizar_jugador_actual_label(self):
        '''Actualiza el texto del jugador actual en la interfaz'''
        self.jugador_actual_label.config(text=f'Turno de: {self.juego.jugador_actual.nombre}')

    def mostrar_stats(self, p1, p2):
        '''Despliega en pantalla los PS de las cartas activas'''
        self.accion_label.config(text='=====\nMarcador\n=====')

        p1_info = f'{p1.nombre} tu carta {p1.carta_activa.nombre} tiene: {p1.carta_activa.ps_actual}/{p1.carta_activa.ps} PS'
        if p1.carta_activa.ps_actual <= 0:
            p1_info += f'\n{p1.nombre} tu carta {p1.carta_activa.nombre} fue retirada...'

        self.accion_label.config(text=f'{self.accion_label.cget("text")}\n{p1_info}\n----------')

        p2_info = f'{p2.nombre} tu carta {p2.carta_activa.nombre} tiene: {p2.carta_activa.ps_actual}/{p2.carta_activa.ps} PS'
        if p2.carta_activa.ps_actual <= 0:
            p2_info += f'\n{p2.nombre} tu carta {p2.carta_activa.nombre} fue retirada...'

        self.accion_label.config(text=f'{self.accion_label.cget("text")}\n{p2_info}\n=====')

    def vista_jugador_ataca(self):
        '''Procedimiento que permite mostrar el mazo de cartas al jugador,
        también escoger una carta de dicho mazo'''
        self.mostrar_mazo(self.juego.jugador_actual)
        self.escoger_carta(self.juego.jugador_actual)
        self.actualizar_jugador_actual_label()

        if self.juego.jugador_actual is self.player1:
            self.mostrar_stats(self.player1, self.player2)
        else:
            self.mostrar_stats(self.player2, self.player1)

        if self.juego.jugador_actual.carta_activa.ps_actual > 0:
            self.accion_label.config(text=self.juego.jugador_ataca())
            self.actualizar_jugador_actual_label()

        if self.__validar_estado(self.juego.jugador_siguiente):
            self.accion_label.config(text=f'El ganador es: {self.juego.jugador_actual.nombre}')
            self.lanzar_ataque_button.config(state='disabled')
            self.curar_carta_button.config(state='disabled')

    def vista_curar_carta(self):
        '''Se escoge una carta del mazo para curarla'''
        self.mostrar_mazo(self.juego.jugador_actual)
        self.escoger_carta(self.juego.jugador_actual)
        self.actualizar_jugador_actual_label()

        if self.juego.jugador_actual is self.player1:
            self.mostrar_stats(self.player1, self.player2)
        else:
            self.mostrar_stats(self.player2, self.player1)

        if self.juego.jugador_actual.carta_activa.ps_actual > 0:
            self.accion_label.config(text=self.juego.jugador_curar_carta())
            self.actualizar_jugador_actual_label()

    def mostrar_mazo(self, jugador):
        '''Desplegamos el mazo del jugador'''
        self.accion_label.config(text=f'Mazo de cartas de {jugador.nombre}:')
        for i, carta in enumerate(jugador.mazo):
            self.accion_label.config(text=f'{self.accion_label.cget("text")}\n{i+1}. {carta.nombre}')

    def escoger_carta(self, jugador):
        '''Se solicita al jugador que escoja una carta del mazo'''
        carta_elegida = int(input(f'{jugador.nombre} elige una carta: '))
        jugador.escoger_carta(carta_elegida)

    def __validar_estado(self, jugador):
        '''Validamos si el jugador ya ha ganado el juego'''
        return jugador.mazo_vacio() or jugador.carta_activa.ps_actual <= 0


if __name__ == "__main__":
    app = App()