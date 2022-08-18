price = [57.8, 46.51, 97, 10.01, 1, 1000, 856.45, 985.10, 15, 94.55, 11.56]
price.sort()
for price in price:
    rur = int(price)
    kop = (price - int(price)) * 100
    print(f'{rur:02.0f} руб. {kop:02.0f} коп.')

price_2 = [57.8, 46.51, 97, 10.01, 1, 1000, 856.45, 985.10, 15, 94.55, 11.56]
price_2.sort(reverse = True)
for price_2 in price_2:
    rur = int(price_2)
    kop = (price_2 - int(price_2)) * 100
    print(f'{rur:02.0f} руб. {kop:02.0f} коп.')

