'''
	Programa de calculadora ejecutable y que
	de manera gráfica interactue con el usuario
	para realizar las operaciones
'''

#Importar la libreria gráfica tkinter de python.
from tkinter import *

#Crear la venta del ejecutable.
ventana = Tk()
ventana.title("Calculadora")

i = 0

#Entrada de texto.
e_texto = Entry(ventana, font = "Agency 20")
e_texto.grid(row = 0, column = 0, columnspan = 4,
padx = 5, pady = 5)

#Función para conectar los botones con la entrada de texto.
def click(valor):
	global i
	e_texto.insert(i, valor)
	i += 1
	
#Función que permite limpiar pantalla.
def clean():
	global i
	e_texto.delete(0, END)
	i = 0

#Función que usa una libreria de python para evaluar la entrada de texto.	
def ec():
	global i
	ecuacion = e_texto.get()
	res = eval(ecuacion)
	e_texto.delete(0, END)
	e_texto.insert(0, res)
	i = 0

#Creación de los botones de la calculadora.
botton1 = Button(ventana, text = "1", width = 5, height = 2, bg = "yellow", command = lambda: click(1))
botton2 = Button(ventana, text = "2", width = 5, height = 2, bg = "yellow", command = lambda: click(2))
botton3 = Button(ventana, text = "3", width = 5, height = 2, bg = "yellow", command = lambda: click(3))
botton4 = Button(ventana, text = "4", width = 5, height = 2, bg = "yellow", command = lambda: click(4))
botton5 = Button(ventana, text = "5", width = 5, height = 2, bg = "yellow", command = lambda: click(5))
botton6 = Button(ventana, text = "6", width = 5, height = 2, bg = "yellow", command = lambda: click(6))
botton7 = Button(ventana, text = "7", width = 5, height = 2, bg = "yellow", command = lambda: click(7))
botton8 = Button(ventana, text = "8", width = 5, height = 2, bg = "yellow", command = lambda: click(8))
botton9 = Button(ventana, text = "9", width = 5, height = 2, bg = "yellow", command = lambda: click(9))
botton0 = Button(ventana, text = "0", width = 15, height = 2, bg = "yellow", command = lambda: click(0))

botton_clean = Button(ventana, text = "AC", width = 5, height = 2, bg = "light green", command = lambda: clean())
botton_p1 = Button(ventana, text = "(", width = 5, height = 2, bg = "light green", command = lambda: click("("))
botton_p2 = Button(ventana, text = ")", width = 5, height = 2, bg = "light green", command = lambda: click(")"))
botton_punto = Button(ventana, text = ".", width = 5, height = 2, bg = "light green", command = lambda: click("."))

botton_sum = Button(ventana, text = "+", width = 5, height = 2, bg = "light green", command = lambda: click("+"))
botton_res = Button(ventana, text = "-", width = 5, height = 2, bg = "light green", command = lambda: click("-"))
botton_mul = Button(ventana, text = "*", width = 5, height = 2, bg = "light green", command = lambda: click("*"))
botton_div = Button(ventana, text = "/", width = 5, height = 2, bg = "light green", command = lambda: click("/"))
botton_ig = Button(ventana, text = "=", width = 5, height = 2, bg = "light green", command = lambda: ec())

#Posicionar los botones de la calculadora.
botton_clean.grid(row = 1, column = 0, padx = 5, pady = 5)
botton_p1.grid(row = 1, column = 1, padx = 5, pady = 5)
botton_p2.grid(row = 1, column = 2, padx = 5, pady = 5)
botton_div.grid(row = 1, column = 3, padx = 5, pady = 5)

botton1.grid(row = 2, column = 0, padx = 5, pady = 5)
botton2.grid(row = 2, column = 1, padx = 5, pady = 5)
botton3.grid(row = 2, column = 2, padx = 5, pady = 5)
botton_mul.grid(row = 2, column = 3, padx = 5, pady = 5)

botton4.grid(row = 3, column = 0, padx = 5, pady = 5)
botton5.grid(row = 3, column = 1, padx = 5, pady = 5)
botton6.grid(row = 3, column = 2, padx = 5, pady = 5)
botton_sum.grid(row = 3, column = 3, padx = 5, pady = 5)

botton7.grid(row = 4, column = 0, padx = 5, pady = 5)
botton8.grid(row = 4, column = 1, padx = 5, pady = 5)
botton9.grid(row = 4, column = 2, padx = 5, pady = 5)
botton_res.grid(row = 4, column = 3, padx = 5, pady = 5)

botton0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
botton_punto.grid(row = 5, column = 2, padx = 5, pady = 5)
botton_ig.grid(row = 5, column = 3, padx = 5, pady = 5)


#Añadir todo lo que sucede a nuestra ventana.
ventana.mainloop()