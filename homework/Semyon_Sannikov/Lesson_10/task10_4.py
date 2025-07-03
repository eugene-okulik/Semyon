PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


old_list = PRICE_LIST.split()
names = old_list[::2]
prices = map(lambda p: int(p[:-1]), old_list[1::2])
print(dict(zip(names, prices)))
