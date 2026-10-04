def logger(func):

    def wrapper(*args, **kwargs):

        print(f"Function {func.__name__} started")

        result = func(*args, **kwargs)

        print("Result:", result)

        print(f"Function {func.__name__} finished")

        return result

    return wrapper


@logger
def calculate(a, b):
    return a + b


calculate(10, 20)
