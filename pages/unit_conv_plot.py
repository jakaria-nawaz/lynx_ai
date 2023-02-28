import csv
import pandas as pd
import matplotlib.pyplot as plt

categories = {
        'Bakery': ['durum', 'salt', 'sugar', 'bread'],
        'Canned goods': ['kidney beans', 'mushroom', 'tomato puree'],
        'Dairy': ['butter', 'cheese', 'egg', 'eggs', 'milk', 'yogurt'],
        'Fish': ['salmon', 'tuna'],
        'Fruits': ['apple', 'orange', 'tangerine'],
        'Grains': ['flour', 'musli', 'pasta', 'rice'],
        'Meat': ['beef', 'chicken', 'chicken breast', 'pork'],
        'Oil': ['cooking oil', 'olive oil'],
        'Spices': ['chilli powder', 'garam masala', 'garlic paste', 'garlic powder', 'ginger paste', 'turmeric powder'],
        'Vegetables': ['carrot', 'garlic', 'onion', 'potatoes', 'tomato']   
    }

