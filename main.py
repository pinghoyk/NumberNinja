# Добавление импортов
from tkinter import * 
import tkinter as tk
import random

#Переменные для чисел
first_number = 0
second_number = 0


#Создаём окно
root_Main = Tk() 
root_Main.geometry('300x400')

#Добавляем изменяемость чисел
first_number = random.randint(0, 200)
second_number = random.randint(0, 200)


# Создаем пример, на который есть ответ
first_number = random.randint(0, 200)
second_number = random.randint(0, 200)
result = first_number + second_number


#Создаем строку с примером
example = Label(text = str(first_number) + "+"+ str(second_number) + "=")
example.pack()

# Функция, чтобы при нажатии на кнопку мы узнавали ответ
def check_answer(answer):
    if int(answer) == result:
        result_label.config(text="Правильно!")
    else:
        result_label.config(text="Неправильно!")







#Переменные для кнопкок / Добавление рандома и Постоянный правильный 1 ответ 
text_1 = str(result)
text_2 = str(random.randint(0, 300))
text_3 = str(random.randint(0, 300))

# Создаем кнопки
btn1 = Button(text=text_1, command=lambda: check_answer(text_1))
btn1.place(relx=0.3, rely=0.9)

btn2 = Button(text=text_2, command=lambda: check_answer(text_2))
btn2.place(relx=0.5, rely=0.9)

btn3 = Button(text=text_3, command=lambda: check_answer(text_3))
btn3.place(relx=0.7, rely=0.9)



#Добавляем строку с отображением результата
result_label = Label(text="")
result_label.pack()

root_Main.mainloop()
