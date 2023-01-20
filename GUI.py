# -*- coding:utf-8 -*-
from base64 import encode
from tkinter import *
from tkinter.ttk import Combobox
from tktooltip import ToolTip
import Gen


def start():
    pop_size = int(pop_size_ent.get())
    mut_prob = int(mut_prob_ent.get())
    it_count = int(it_count_ent.get())

    user_height = int(user_height_ent.get())
    user_weight = int(user_weight_ent.get())
    user_age = int(user_age_ent.get())
    user_phys_act = float(user_phys_act_ent.get().replace(',', '.'))
    user_sex = str(user_sex_combo.get())

    genAlg = Gen.GeneticAlgorithm(pop_size,it_count,mut_prob, Gen.User(user_sex, user_age, user_weight, user_height, user_phys_act))
    genAlg.GeneticAlg()


window = Tk()
window.title ('Kurs')
window.geometry('800x500')


user_var_lb = Label(window , text='Данные пользователя:')
user_var_lb.grid(column=0, row=0, sticky=W)

user_height_lb = Label(window, text='Рост (в см):')
user_height_lb.grid(column=0, row=1, padx =10, sticky=W)
user_height_ent = Entry(window, width=20)
user_height_ent.insert(0, '175')
user_height_ent.grid(column=1, row=1)

user_weight_lb = Label(window, text='Желаемый вес (в кг):')
user_weight_lb.grid(column=0, row=2, padx =10, sticky=W)
user_weight_ent = Entry(window, width=20)
user_weight_ent.insert(0, '80')
user_weight_ent.grid(column=1, row=2)

user_age_lb = Label(window, text='Возраст:')
user_age_lb.grid(column=0, row=3, padx =10, sticky=W)
user_age_ent = Entry(window, width=20)
user_age_ent.insert(0, '23')
user_age_ent.grid(column=1, row=3)

user_sex_lb = Label(window, text='Пол:')
user_sex_lb.grid(column=0, row=4, padx =10, sticky=W)
user_sex_combo = Combobox(window, width=17)
user_sex_combo['values'] = ('Муж', 'Жен')
user_sex_combo.current(0)
user_sex_combo.grid(column=1, row=4)

user_phys_act_lb = Label(window, text='Коэффициент физической нагрузки:')
user_phys_act_lb.grid(column=0, row=5, padx =10, sticky=W)
user_phys_act_ent = Entry(window, width=20)
user_phys_act_ent.insert(0, '1,5')
user_phys_act_ent.grid(column=1, row=5)

ToolTip(user_phys_act_ent, msg="Наиболее распространенные варианты:\nМинимальные физические нагрузки (сидячая работа) = 1,2-1,3\nНебольшая дневная активность или легкие упражнения 1-3 раза в неделю = 1,3-1,4\nТренировки в фитнес-зале 4-5 раз в неделю или работа средней тяжести = 1,5-1,6\nИнтенсивные тренировки 4-5 раз в неделю = 1,7-1,8\nЕжедневные тренировки = 1,9-2\nЕжедневные интенсивные тренировки или обычные тренировки 2 раза в день = 2,1-2,2\nИнтенсивные тренировки 2 раза в день или тяжелая физическая работа = 2,4-2,5")
ToolTip(user_phys_act_lb, msg="Наиболее распространенные варианты:\nМинимальные физические нагрузки (сидячая работа) = 1,2-1,3\nНебольшая дневная активность или легкие упражнения 1-3 раза в неделю = 1,3-1,4\nТренировки в фитнес-зале 4-5 раз в неделю или работа средней тяжести = 1,5-1,6\nИнтенсивные тренировки 4-5 раз в неделю = 1,7-1,8\nЕжедневные тренировки = 1,9-2\nЕжедневные интенсивные тренировки или обычные тренировки 2 раза в день = 2,1-2,2\nИнтенсивные тренировки 2 раза в день или тяжелая физическая работа = 2,4-2,5")


set_title_lb = Label(window , text='Задайте параметры работы алгоритма:')
set_title_lb.grid(column=2, row=0, sticky=W)

pop_size_lb = Label(window, text='Размер популяции(количество хромосом):')
pop_size_lb.grid(column=2, row=1, padx =10, sticky=W)
pop_size_ent = Entry(window, width=20)
pop_size_ent.insert(0, '100')
pop_size_ent.grid(column=3, row=1)

mut_prob_lb = Label(window, text='Вероятность мутации хромосомы(%):')
mut_prob_lb.grid(column=2, row=2, padx =10, sticky=W)
mut_prob_ent = Entry(window, width=20)
mut_prob_ent.insert(0, '10')
mut_prob_ent.grid(column=3, row=2)

it_count_lb = Label(window, text='Количество итераций алгоритма:')
it_count_lb.grid(column=2, row=3, padx =10, sticky=W)
it_count_ent = Entry(window, width=20)
it_count_ent.insert(0, '100')
it_count_ent.grid(column=3, row=3)

set_conf_bt = Button(window, text='Старт', command=start)
set_conf_bt.grid(column=3, row=5, sticky=W, padx =10, pady=10)

window.mainloop()