"""
List Comprehensions
"""
list_price = [10, 33, 55, 88]
halved = [price / 2 for price in list_price]

halved_2 = []
for price in list_price:
    h = price / 2
    halved_2.append(h)

print(halved)
print(halved_2)


names = ['Ana', 'Juan', 'Oscar']
names = ['Mr ' + name for name in names]
for n in names: print('Name: ' + n)

words = ['Celamos', 'Four', 'One']
quality = [word.count('a') for word in words]
print(quality)
