for program_number in range(1, 101):
    if program_number % 15 == 0:
        print("FuzzBuzz")
    elif program_number % 5 == 0:
        print('Buzz')
    elif program_number % 3 == 0:
        print('Fuzz')
    else:
        print(program_number)

