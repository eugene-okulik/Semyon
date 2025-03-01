words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
word = words.values()
a, b, c, d = word
keys = words.keys()
a1, b1, c1, d1 = keys
print(a1, b1, c1, d1)
while True:
    a2 = a1 * a
    b2 = b1 * b
    c2 = c1 * c
    d2 = d1 * d
    print(a2)
    print(b2)
    print(c2)
    print(d2)
    break


# Другой вариант.
words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for key, value in words.items():
    print(key * value)
