# Добавление импортов
from tkinter import * 
import tkinter as tk
import random

#Переменные
first_number = 0
second_number = 0


#Создаём окно
root_Main = Tk() 

#Добавляем изменяемость чисел
first_number = random.randint(0, 200)
second_number = random.randint(0, 200)

#Создаем пример
example = Label(text = str(first_number) + "+"+ str(second_number) + "=")
example.pack()


btn = Button(text='Ответ')
btn.pack()


root_Main.mainloop()
