import pandas as pd
import random

# Класс представляющий собой блюдо
class Dish:
    name = ''
    quantity = 0
    calorage_per_100 = 0
    protein_per_100 = 0
    fat_per_100 = 0
    carbohydrates_per_100 = 0
    href = ''

    def __init__ (self, name, quantity, calorage, protein, fat, carbohydrates, href):
        self.name = name
        self.quantity = quantity
        self.calorage_per_100 = calorage
        self.protein_per_100 = protein
        self.fat_per_100 = fat
        self.carbohydrates_per_100 = carbohydrates
        self.href = href


class DishesList:
    dishesList = pd.DataFrame

    def __init__ (self, file_path):
        self.dishesList = pd.read_table(file_path, sep="/\.\./", header=None, names=["name","calorage", "protein", "fat", "carbohydrates","href"], encoding="utf-8")

    def getDish (self):
        number = random.randint(0,self.dishesList.shape[0]-1)
        d_name = self.dishesList['name'][number]
        d_calorage = float(self.dishesList['calorage'][number])
        d_protein = float(self.dishesList['protein'][number])
        d_fat = float(self.dishesList['fat'][number])
        d_carbohydrates = float(self.dishesList['carbohydrates'][number])
        d_href = self.dishesList['href'][number]
        d_quantity = 0
        if (d_calorage >= 100 and d_calorage < 200):
            d_quantity = random.randint(1,3)
        if (d_calorage >= 0 and d_calorage < 100):
            d_quantity = random.randint(2,3)
        if (d_calorage > 200 ):
            d_quantity = random.randint(1,2)
        return Dish(d_name, d_quantity, d_calorage, d_protein, d_fat, d_carbohydrates, d_href)
