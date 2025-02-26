text1 = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel.' 
text2 = 'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
concatination = text1 + text2

words = concatination.split()
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
    