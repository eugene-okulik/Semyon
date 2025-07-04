PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


old_list = PRICE_LIST.split()
names = old_list[::2]
prices = old_list[1::2]
actual_price = [int(p[:-1]) for p in prices]
price_dict = dict(zip(names, actual_price))
print(price_dict)
