import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('800x400')
ventana.title('Manejo de Grid')
# ventana.iconbitmap('icono.ico')

# configurar el grid
ventana.rowconfigure(0,weight=1)
ventana.rowconfigure(1,weight=5)
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=5)
# Métodos de los eventos
def evento1():
    boton1.config(text='Botón 1 presionado')

def evento2():
    boton2.config(text='Botón 2 presionado')

def evento3():
    boton3.config(text='Botón 3 presionado')

def evento4():
    boton4.config(text='Botón 4 presionado',fg="blue",bg="red",relief=tk.GROOVE)

# # bg="blue")background(segundo plano,fondo)
# relif=tk.GROOVE(Relieve)
# fg="red")foreground(primer plano,la fuente)
# salta error si se configura en un boton que utilice ttk

 # widtg es la cantidad de caracteres qye ocupa la caja de texto,
# justify=tk.


# # Definimos dos botones
boton1 = ttk.Button(ventana, text='boton1', command=evento1)
boton1.grid(row=0, column=0,sticky="NSWE")
# # N(norte,arriba),E(Este,derecha),S(Sur,abajo),W(Oeste,izquierda)
# # con columnspan
boton2 = ttk.Button(ventana, text='Botón 2', command=evento2)
boton2.grid(row=1,column=0,sticky="NSWE")

boton3 = ttk.Button(ventana, text='Botón 3', command=evento3)
boton3.grid(row=0, column=1,sticky="NSWE")

boton4 = tk.Button(ventana, text='Botón 4', command=evento4)
boton4.grid(row=1, column=1,sticky="NSWE")
ventana.mainloop()

# PADDING (ESPACIO QUE SE DEJA ENTRE LOS ELEMENTOS)
# pady arriba y abajo padx derecha izquierda (dentro) ipadx izquierda y derecha ipady abajo y arriba
# ipad dentro y pad fuera


