import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
import juego
import jugador as j
import carta as c
import ataques.attack as atq
import utiles

class Aplication(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.geometry('1000x500')
        self.title('prueba')

        self.juego = None   # Se creará el juego cuando se tenga a los jugadores.
        self.card_flag = False # Las cartas del player 2 comenzaran deshabilitadas.
        self.galeria_mazo_p1 = []
        self.galeria_mazo_p2 = []

        self.crear_widgets()

    def crear_widgets(self):
        self.main_frame = tk.Frame(master=self)

        self.mostrar_logo("logo.png")

        self.crear_boton("jugar.png", "jugar_hover.png", self.iniciar_partida, self.main_frame)
        self.crear_boton("instrucciones.png", "instrucciones_hover.png", lambda : print('Hola'), self.main_frame)
        self.crear_boton("salir.png", "salir_hover.png", lambda : print('Hola'), self.main_frame) 

        self.main_frame.pack(fill=tk.BOTH, expand=True)

    def mostrar_logo(self, img):
        logo = ImageTk.PhotoImage(Image.open(img))
        label = tk.Label(self.main_frame, image=logo)

        label.pack(pady=8)

    def crear_boton(self, img1, img2, cmd, frm):
        # Abrimos las imagenes, una para estado normal, otra para el Hover.
        image_a = ImageTk.PhotoImage(Image.open(img1))
        image_b = ImageTk.PhotoImage(Image.open(img2))

        def on_enter(self):
            '''
            Brinda una respuesta visual al usuario de interacción con el botón.
            '''
            btn['image'] = image_b
        
        def on_leave(self):
            btn['image'] = image_a

        btn = tk.Button(master=frm, image=image_a,
                        border=0,
                        cursor='hand2',
                        command=cmd,
                        relief='sunken')

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.pack(pady=8)

    def iniciar_partida(self):
        '''
        En este método los jugadores introducen sus nombres, para poder ser creados luego.
        '''
        emergente = tk.Toplevel(self)
        emergente.geometry('500x250')

        str_p1 = tk.StringVar()
        str_p2 = tk.StringVar()
        titulo = tk.Label(emergente, text='Escriban sus nombres', font='Roboto 24 bold', pady=8)
        titulo.grid(row=0, columnspan=2)

        input_frame = tk.Frame(emergente)
        input_frame.grid(row=1, columnspan=2)

        input_nombre = ttk.Entry(input_frame, width=40, textvariable=str_p1)
        input_nombre.grid(row=0, column=1, pady=2)

        input_nombre2 = ttk.Entry(input_frame, width=40, textvariable=str_p2)
        input_nombre2.grid(row=1, column=1, pady=2)

        leyenda1 = tk.Label(input_frame, font='Roboto 16', text='Bienvenido:')
        leyenda1.grid(row=2, column=0, padx=2, sticky=tk.E)

        p1 = tk.Label(input_frame, font='Roboto 16', textvariable=str_p1)
        p1.grid(row=2, column=1, pady=2, sticky=tk.W)

        leyenda2 = tk.Label(input_frame, font='Roboto 16', text='Bienvenido:')
        leyenda2.grid(row=3, column=0, padx=2, sticky=tk.E)

        p2 = tk.Label(input_frame, font='Roboto 16', textvariable=str_p2)
        p2.grid(row=3, column=1, sticky=tk.W)

        btn = ttk.Button(emergente, 
            text='Seguir', 
            command=lambda : self.crear_jugadores(str_p1.get(), str_p2.get()))
        btn.grid(row=3, columnspan=2, pady=8)

    def crear_jugadores(self, nombre1, nombre2):
        '''Crea los jugadores y los asigna al juego'''
        player1 = j.Jugador(nombre1, [
            c.CartaBasica('Messi', 'Mundial', 10, 4, atq.Derribo(), "carta_messi.png", "carta_messi_hover.png"),
            c.CartaBasica('CR7', 'SIIIUUU', 12, 3, atq.CartaDelJuicio(), "carta_cr7.png", "carta_cr7_hover.png")
        ], 10)

        player2 = j.Jugador(nombre2, [
            c.CartaBasica('Messi', 'Mundial', 10, 4, atq.Derribo(), "carta_messi.png", "carta_messi_hover.png"),
            c.CartaBasica('CR7', 'SIIIUUU', 12, 3, atq.CartaDelJuicio(), "carta_cr7.png", "carta_cr7_hover.png")
        ], 10)

        self.juego = juego.Juego(player1, player2)

        self.crear_ventana_partida()

    def crear_carta(self, img1, img2, frm):
        # Abrimos las imagenes, una para estado normal, otra para el Hover.
        image_a = ImageTk.PhotoImage(Image.open(img1))
        image_b = ImageTk.PhotoImage(Image.open(img2))

        def on_enter(self):
            '''
            Brinda una respuesta visual al usuario de interacción con la carta.
            '''
            btn['image'] = image_b
        
        def on_leave(self):
            btn['image'] = image_a

        btn = tk.Button(master=frm, image=image_a,
                        border=0,
                        cursor='hand2',
                        relief='sunken')

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.pack(padx=2, side=tk.LEFT)  # Ubicamos las cartas una al lado de la otra.

        return btn

    def crear_ventana_partida(self):
        self.destroy()  # Destruye la pantalla de Menu

        self.ventana_juego = tk.Tk()    # Inicia una ventana de juego.
        self.ventana_juego.geometry('1000x500') # Configura la ventana del juego.

        # Frame que contiene las cartas de abajo
        contenedor = tk.Frame(self.ventana_juego)
        contenedor.pack(side=tk.BOTTOM, anchor=tk.W, pady=8, padx=8)

        ######## Galería del mazo del jugador 1 ########
        for c in self.juego.player1.mazo:
            card = self.crear_carta(c.img, c.img_hover, contenedor)
            card.pack(padx=2, side=tk.LEFT)
            self.galeria_mazo_p1.append(card)

        self.galeria_mazo_p1[0].config(command=lambda : self.update_carta_actual(self.juego.player1,self.juego.player1.mazo[0]))
        self.galeria_mazo_p1[1].config(command=lambda : self.update_carta_actual(self.juego.player1,self.juego.player1.mazo[1]))

        # self.card_p1 = self.crear_carta("carta_messi.png", "carta_messi_hover.png", 
        #     lambda : self.update_carta_actual(self.juego.player1, self.juego.player1.mazo[0]), 
        #     contenedor)
        # self.card_p1.pack(padx=2, side=tk.LEFT)  # Ubicamos las cartas una al lado de la otra.

        # self.card2_p1 = self.crear_carta("carta_cr7.png", "carta_cr7_hover.png", 
        #     lambda : self.update_carta_actual(self.juego.player1, self.juego.player1.mazo[1]),
        #     contenedor)
        # self.card2_p1.pack(padx=2, side=tk.LEFT)

        ##### NUEVA IDEA: HACER UNA LISTA DE BOTONES PARA EL MAZO #####
        # self.galeria_mazo_p1.append(self.card_p1)
        # self.galeria_mazo_p1.append(self.card2_p1)

        nombre_jugador = tk.Label(contenedor, text='Jugador: ' + self.juego.player1.nombre, font='Roboto 18 bold').pack(side=tk.TOP, anchor=tk.W)
        
        ##########PARA EL JUGADOR 2#############
        # Frame que contiene las cartas de arriba
        contenedor_arriba = tk.Frame(self.ventana_juego)
        contenedor_arriba.pack(side=tk.TOP, anchor=tk.E, pady=8, padx=8)

        # Galería del mazo del jugador 2
        for c in self.juego.player2.mazo:
            card = self.crear_carta(c.img, c.img_hover, contenedor_arriba)
            card.pack(padx=2, side=tk.LEFT)
            self.galeria_mazo_p2.append(card)

        self.galeria_mazo_p2[0].config(command=lambda : self.update_carta_actual(self.juego.player2,self.juego.player2.mazo[0]))
        self.galeria_mazo_p2[1].config(command=lambda : self.update_carta_actual(self.juego.player2,self.juego.player2.mazo[1]))

        # self.card_p2 = self.crear_carta("carta_messi.png", "carta_messi_hover.png", 
        #     lambda : self.update_carta_actual(self.juego.player2, self.juego.player2.mazo[0]),  
        #     contenedor_arriba)
        # self.card_p2.pack(padx=2, side=tk.LEFT)
        
        # self.card2_p2 = self.crear_carta("carta_cr7.png", "carta_cr7_hover.png", 
        #     lambda : self.update_carta_actual(self.juego.player2, self.juego.player2.mazo[1]),  
        #     contenedor_arriba)
        # self.card2_p2.pack(padx=2, side=tk.LEFT)

        # self.galeria_mazo_p2.append(self.card_p2)
        # self.galeria_mazo_p2.append(self.card2_p2)

        # Estado inicial de las cartas del jugador 2.
        self.galeria_mazo_p2[0].config(state="disabled")
        self.galeria_mazo_p2[1].config(state="disabled")

        nombre_jugador = tk.Label(contenedor_arriba, text='Jugador: ' + self.juego.player2.nombre, font='Roboto 18 bold').pack(side=tk.TOP, anchor=tk.E)
            
        # Ejecucion de la ventana
        self.ventana_juego.mainloop()

    def actualizar_turno(self):
        if self.card_flag:
            for c in self.galeria_mazo_p2:
                c.config(state='disabled')
            
            #### PARA EL JUGADOR 1 #####
            for c in self.galeria_mazo_p1:
                c.config(state='normal')
            
            # Actualizar el contador de juego
            self.juego.turno += 1
        else:
            for c in self.galeria_mazo_p2:
                c.config(state='normal')

            #### PARA EL JUGADOR 1 #####
            for c in self.galeria_mazo_p1:
                c.config(state='disabled')

            # Actualizar el contador de juego
            self.juego.turno += 1
        self.card_flag = not self.card_flag
        
        # Cuando AMBOS jugadores hayan seleccionado su carta, se hace el combate
        if self.juego.turno > 0 and self.juego.turno % 2 == 0:
            self.jugacion()
            # Mostramos la informacion de a partida
            self.mostrar_stats(self.juego.player1, self.juego.player2)
            # Validar
            if (self.validar_estado(self.juego.player1)):
                self.pantalla_ganador(self.juego.player2.nombre)
            elif (self.validar_estado(self.juego.player2)):
                self.pantalla_ganador(self.juego.player1.nombre)

    def ventana_carta_detalle(self, jugador):
        '''Se mostraran detalles de la carta seleccionada.
        Brinda la posibilidad de realizar una acción.'''
        ventana_detalles = tk.Toplevel(self.ventana_juego)
        ventana_detalles.title('Detalles de la carta')
        ventana_detalles.geometry('300x300')

        nombre = tk.Label(ventana_detalles, text=jugador.carta_activa.nombre, font='Roboto 24 bold')
        nombre.pack(pady=4)

        # Detalles
        descripcion = tk.Label(ventana_detalles, 
            text='Descripcion: ' + jugador.carta_activa.descripcion, 
            font='Roboto 14')
        descripcion.pack(pady=8)

        tk.Label(ventana_detalles, text='Salud: ' + str(jugador.carta_activa.ps_actual), font='Roboto 14').pack()

        atq = tk.Label(ventana_detalles, text='Ataque: ' + jugador.carta_activa.ataque.__str__(), font='Roboto 14')
        atq.pack()

        pts_atq = tk.Label(ventana_detalles, 
            text='Puntos de ataque: ' + str(jugador.carta_activa.ataque.obtener_puntos_ataque()), 
            font='Roboto 14')
        pts_atq.pack()

        botones = tk.Frame(ventana_detalles)
        botones.pack(side=tk.BOTTOM, pady=8, padx=8)

        jugar_btn = ttk.Button(botones, text='Jugar esta carta', command= self.actualizar_turno).pack(pady=2)
        sanar_btn = ttk.Button(botones, 
            text='Curar esta carta', 
            command=lambda : self.curar_carta(jugador)).pack(pady=2)

    def update_carta_actual(self, jugador, carta):
        if carta.ps_actual > 0:
            jugador.carta_activa = carta
            self.ventana_carta_detalle(jugador)
        else:
            messagebox.showinfo('Cementerio', 'Esta carta ya no puede ser utilizada :(')

    def curar_carta(self, jugador):
        messagebox.showinfo('Ambulancia', jugador.curar_carta())

    def jugacion(self):
        messagebox.showinfo(self.juego.player1.nombre + ' ataca', self.juego.player1_ataca())
        if self.juego.player2.carta_activa.ps_actual > 0:
            messagebox.showinfo(self.juego.player2.nombre + ' ataca', self.juego.player2_ataca())

    def validar_estado(self, jugador):
        '''Corrobora si existe algun jugador derrotado'''
        if jugador.magia <= 0:  # Si la magia del jugador es cero, entonces pierde.
            return True
        for card in jugador.mazo:   # Si alguna carta aún tiene PS, no pierde el combate.
            if card.ps_actual > 0:
                return False
        return True

    def mostrar_stats(self, p1, p2):
        '''Despliega en pantalla los PS de las cartas activas'''
        content = f'{p1.nombre} tu carta {p1.carta_activa.nombre} tiene: {p1.carta_activa.ps_actual}/{p1.carta_activa.ps} PS'
        messagebox.showinfo('Marcador', content)

        content = f'{p2.nombre} tu carta {p2.carta_activa.nombre} tiene: {p2.carta_activa.ps_actual}/{p2.carta_activa.ps} PS'
        messagebox.showinfo('Marcador', content)
        
        if p1.carta_activa.ps_actual <= 0:
            '''Si una carta está muerta'''
            messagebox.showinfo('Cementerio', f'{p1.nombre} tu carta {p1.carta_activa.nombre} fue retirada...' )

        if p2.carta_activa.ps_actual <= 0:
            messagebox.showinfo('Cementerio', f'{p2.nombre} tu carta {p2.carta_activa.nombre} fue retirada...' )

    def pantalla_ganador(self, nombre_ganador):
        self.ventana_juego.destroy()

        ganador = tk.Tk()
        ganador.geometry('1000x500') # Configura la ventana del juego.

        lb = tk.Label(ganador, text="EL GANADOR ES: " + nombre_ganador, font='Roboto 32 bold').pack()

        ganador.mainloop()


# def centrar_ventana(ventana):
#     ancho = 1000
#     alto = 500

#     # Obtenemos la dimension de la pantalla
#     ancho_pantalla = ventana.winfo_screenwidth()
#     alto_pantalla = ventana.winfo_screenheight()

#     # Posicion central
#     centro_x = int(ancho_pantalla/2 - ancho / 2)
#     centro_y = int(alto_pantalla/2 - alto / 2)

#     # Ubicamos la ventana en la posicion central
#     ventana.geometry(f'{ancho}x{alto}+{centro_x}+{centro_y}')

if __name__ == '__main__':
    app = Aplication()
    app.mainloop()
