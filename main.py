# Добавление импортов
from tkinter import * 
import tkinter as tk
import random

#Переменные
first_number = 0
second_number = 0


#Создаём окно
root_Main = Tk() 
root_Main.geometry('300x400')

#Добавляем изменяемость чисел
first_number = random.randint(0, 200)
second_number = random.randint(0, 200)

#Создаем пример
example = Label(text = str(first_number) + "+"+ str(second_number) + "=")
example.pack()

#Создаем кнопки
btn1 = Button(text='Ответ')
btn1.place(relx=0.3, rely=0.9)

btn2 = Button(text='Ответ')
btn2.place(relx=0.5, rely=0.9)

btn3= Button(text='Ответ')
btn3.place(relx=0.7, rely=0.9)


root_Main.mainloop()
