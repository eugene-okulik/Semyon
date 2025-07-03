def repeat_me(count):

    def perl(func):

        def wrapper(*args):
            for i in range(count):
                func(*args)

        return wrapper

    return perl


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
