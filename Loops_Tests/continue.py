for i in range(1, 11):
    if i % 3 == 0 and i % 5 == 0:
        # con la llave continue podemos decirle que omite, y que siga con
        # el loop
        continue

    print(i)

print('bye')
