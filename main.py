# Добавление импортов
from tkinter import * 
import tkinter as tk

#Переменные
first_number = 0
second_number = 0


#Создаём окно
root_Main = Tk() 

#Создаем пример
example = Label(text = str(first_number) + "+"+ str(second_number) + "=")
example.pack()

root_Main.mainloop()
