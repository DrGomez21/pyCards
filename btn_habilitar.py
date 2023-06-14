import tkinter as tk
from tkinter import ttk 

class Prueba(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.geometry('200x200')
        self.botones()

        self.btn2_enabled = False  # Estado inicial deshabilitado
        
        
    def botones(self):
        self.btn2 = ttk.Button(self, text='cambiante', state="disabled")
        self.btn2.pack()

        self.btn = ttk.Button(self, text='press', command=self.habilitar_boton)
        self.btn.pack()


    def habilitar_boton(self):
        if self.btn2_enabled:
            self.btn2.config(state='disabled')
        else:
            self.btn2.config(state='normal')
        self.btn2_enabled = not self.btn2_enabled


if __name__ == '__main__':
    app = Prueba()
    app.mainloop()
