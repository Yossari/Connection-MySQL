from tkinter import *
from tkinter import ttk

window = Tk()
frame_app = Frame(window, width=400, height=600, bg="red")
frame_app.pack()

# Widgets dentro del contender APP
frame_navbar = Frame(frame_app, width=400, height=100)
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=400, height=150)
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=400, height=500)
frame_options.grid(row=2, column=0)

# Widgets dentro del contender OPTIONS
frame_food = Frame(frame_options, width=350, height=350, bg="green")
frame_food.place(x=25, y=30)
# frame_drinks = Frame(frame_options, width=350, height=200, bg="#eba2a2")
# frame_drinks.place(x=25, y=380)
label_food = Label(frame_food, 
              text="Comida",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_food.place(x=20, y=290)
def formulario():
    Label(frame_food, text="SE HA ENVIADO TU FORMULARIO", bg="red").grid(row=4, column=0)
    
nombre = Entry(frame_food)
nombre = Label(frame_food, text="correo:", bg="pink")
nombre.grid(row=0, column=0)

n = Entry(frame_food, width=50)
n.grid(row=1,column=0)

cuenta = Entry(frame_food)
cuenta = Label(frame_food, text="Contraseña:",bg="blue")
cuenta.grid(row=2,column=0)

c = Entry(frame_food, width=50)
c.grid(row=3,column=0)

grado = Entry(frame_food)
grado = Label(frame_food, text="Edad:", bg="yellow")
grado.grid(row=4,column=0)

g = Entry(frame_food, width=50)
g.grid(row=5, column=0)

boton_enviar = Button(frame_food, text="ENVIAR", bg="gray", command=formulario)
boton_enviar.grid(row=6, column=0)

# Widgets dentro del contender NAVBAR
title = Label(frame_navbar, 
              text="datos",
              font=("Calibri", "14"))
title.place(x=320, y=40)

# Widgets dentro del contender TITLE
title1 = Label(frame_title, 
              text="¡Bienvenido(a)!", 
              font=("Calibri", "22", "bold"),
              justify=LEFT)
title1.place(x=25, y=10)
title2 = Label(frame_title, 
              text="¿Quieres ser parte de nuestra \ncomunidad?", 
              font=("Calibri", "18"),
              justify=LEFT)
title2.place(x=25, y=50)

window.mainloop()
