def decorator(func):

    def wrapper(first, second, operation=None):
        if first < 0 or second < 0:
            symv = "*"
        elif first == second:
            symv = "+"
        elif first > second:
            symv = "-"
        elif first < second:
            symv = "/"
        else:
            symv = operation
        return func(first, second, symv)

    return wrapper


@decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == "*":
        return first * second
    elif operation == "/" and second != 0:
        return first / second
    elif operation == "/" and second == 0:
        return "Знаменатель не может быть равным 0"
    else:
        return "Неизвестная операция"


num_1, num_2 = map(int, input("Чтобы получить результат, введите два числа через пробел: ").split())
result = calc(num_1, num_2)
print(f"Результат = {result}")
