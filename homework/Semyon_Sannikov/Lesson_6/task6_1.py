# Напишите программу, которая добавляет ‘ing’ в конец слов (к каждому слову) в тексте 
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero” 
# и после этого выводит получившийся текст на экран. Знаки препинания не должны оказаться внутри слова. 
# Если после слова идет запятая или точка, этот знак препинания должен идти после того же слова, но уже преобразованного.
text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
words = text.split()
upgrade_text = []

for word in words:
    if ',' in word:
        word = word.replace(',', 'ing,')
    elif '.' in word:
        word = word.replace('.', 'ing.')
    else:
        word = word + 'ing'
    upgrade_text.append(word)
final_text = upgrade_text
print(' '.join(final_text))
    