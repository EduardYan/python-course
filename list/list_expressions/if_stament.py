"""
Filtranding data with if staments
"""

scores = [9000, 67, 88, 12000, 12]
hight_scores = [score for score in scores if score > 20]
print(hight_scores)

names = ['Ana', 'Daniel', 'carlos']
names_mayus = [name for name in names if name == name.capitalize()]
print(names_mayus)

cars = [
    {
        'name': 'Toyota',
        'price': 12000
    },
    {
        'name': 'Ferrari',
        'price': 30000
    },
    {
        'name': 'Mercedes',
        'price': 400000
    }
]
cost_cars = [cost['price'] for cost in cars]
print(cost_cars)
most_cost = [more_cost for more_cost in cars if more_cost['price'] > 50000]
print(most_cost)
