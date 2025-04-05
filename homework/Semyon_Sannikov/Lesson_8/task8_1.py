import random

salary = int(input('Введите ваши ожидания по зарплате: '))
bonus = random.choice([False, True])

if bonus:
    bonus_upp = random.randint(1, 50)
    total_salary = salary + bonus_upp
else:
    total_salary = salary

print(f"{salary} {bonus} - '${total_salary}'")
