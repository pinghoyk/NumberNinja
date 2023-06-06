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


#Переменные для кнопкок
text_1 = 0
text_2 = 0
text_3 = 0


#Изменения кнопок
text_1 = random.randint(0, 200)
text_2 = random.randint(0, 200)
text_3 = random.randint(0, 200)



#Создаем кнопки
btn1 = Button(text=str(text_1))
btn1.place(relx=0.3, rely=0.9)

btn2 = Button(text=str(text_2))
btn2.place(relx=0.5, rely=0.9)

btn3= Button(text=str(text_3))
btn3.place(relx=0.7, rely=0.9)


root_Main.mainloop()
