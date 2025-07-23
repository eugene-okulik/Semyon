class Flowers:
    root = True
    stem = True
    def __init__(self, petal_color, number_of_petals, time_to_go, price):
        self.petal_color = petal_color
        self.number_of_petals = number_of_petals
        self.time_to_go = time_to_go
        self.price = price


class Rose(Flowers):
    def __init__(self, petal_color, number_of_petals, time_to_go, price, thorny = True):
        super().__init__(petal_color, number_of_petals, time_to_go, price)
        self.thorny = thorny


class Chamomile(Flowers):
    def __init__(self, petal_color, number_of_petals, time_to_go, price, loves = True):
        super().__init__(petal_color, number_of_petals, time_to_go, price)
        self.loves = loves


class Tulip(Flowers):
    def __init__(self, petal_color, number_of_petals, time_to_go, price, wild=True):
        super().__init__(petal_color, number_of_petals, time_to_go, price)
        self.wild = wild


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def total_price(self):
        total = 0
        for flower in self.flowers:
            total += flower.price
        print(f"Стоимость букета: {total} руб.")
        return total

    def momento_mori(self):
        total = 0
        for flower in self.flowers:
            total += flower.time_to_go
        avg = total / len(self.flowers)
        print(f"Среднее время жизни букета: {avg} дней")
        return avg

    def sort(self, by='number_of_petals'):
        if by == 'number_of_petals':
            self.flowers.sort(key=lambda f: f.number_of_petals)
        elif by == 'price':
            self.flowers.sort(key=lambda f: f.price)
        elif by == 'time_to_go':
            self.flowers.sort(key=lambda f: f.time_to_go)
        elif by == 'petal_color':
            self.flowers.sort(key=lambda f: f.petal_color)
        else:
            print("Неизвестный параметр сортировки")
            return
        print(f"Сортировка по {by}:")
        for f in self.flowers:
            print(f"{f.__class__.__name__}: {f.petal_color}, {f.number_of_petals} лепестков, {f.price} руб., {f.time_to_go} дней")

    def find(self, by, value):
        found = [f for f in self.flowers if getattr(f, by, None) == value]
        if not found:
            print(f"Цветы с {by} = {value} не найдены.")
        else:
            print(f"Найдено цветов с {by} = {value}: {len(found)}")
            for f in found:
                print(f"{f.__class__.__name__}: {f.petal_color}, {f.number_of_petals} лепестков, {f.price} руб., {f.time_to_go} дней")
        return found

f1 = Rose('Red', 30, 10, 150)
f2 = Tulip('Yellow', 12, 7, 80, wild=True)
f3 = Chamomile('White', 24, 5, 40)
f4 = Rose('Pink', 25, 12, 170, thorny=False)
f5 = Tulip('Purple', 10, 8, 90)
bouquet = Bouquet([f1, f2, f3, f4, f5])

bouquet.total_price()
bouquet.momento_mori()
bouquet.sort('petal_color')
bouquet.find('petal_color', 'Yellow')
