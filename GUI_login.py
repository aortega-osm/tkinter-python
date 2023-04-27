import tkinter as tk
from tkinter import ttk , messagebox


ventana = tk.Tk()
ventana.geometry("300x130")
ventana.title("Login")

# grid
ventana.rowconfigure(0,weight=1)
ventana.rowconfigure(1,weight=1)
ventana.rowconfigure(2,weight=3)
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=3)

etiquetaUsuario=ttk.Label(ventana,text="Usuario:")
etiquetaUsuario.grid(row=0,column=0,sticky="NSWE")
entrada1=ttk.Entry(ventana,width=40)
entrada1.grid(row=0,column=1)


etiquetaContraseña=ttk.Label(ventana,text="Contraseña:")
etiquetaContraseña.grid(row=1,column=0,sticky="NSWE")
entrada2=ttk.Entry(ventana,width=40,show="*")
entrada2.grid(row=1,column=1)

def login():
    messagebox.showinfo("Datos:",f"usuario:{entrada1.get()} contraseña:{entrada2.get()}")

botonLogin=ttk.Button(ventana,text="Login",command=login)
botonLogin.grid(row=2,column=1,sticky="NSWE")

ventana.mainloop()