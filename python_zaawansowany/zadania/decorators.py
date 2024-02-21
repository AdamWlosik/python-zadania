import time


def logged(func):
    def wrapper(*args, **kwargs):
        """Dekorator wyświetlający z jakimi argumentami dana funkcja została wywołana oraz jej nazwe"""
        result = func(*args, **kwargs)
        args_str = ", ".join(map(repr, args))
        kwargs_str = ", ".join(f"{key} = {value!r}" for key, value in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"Wywołałeś {func.__name__}({all_args}), która zwróciła: {result}")
        return result

    return wrapper


def stars_decorator(func):
    def wrapper(*args, **kwargs):
        """Dekorator dodający gwiadki do wyniku funkcji"""
        print("*" * 12)
        func(*args, **kwargs)
        print("*" * 12)

    return wrapper


class StarsDecorator:
    """Klasa z protokałami __init__ i __call__ dodająca * do wyniku funkcji"""

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("*" * 12)
        self.func(*args, **kwargs)
        print("*" * 12)


def count(func):
    """Dekorator zliczający wywołania funkcji"""
    counts = {}

    def wrapper(*args, **kwargs):
        if func.__name__ in counts:
            counts[func.__name__] += 1
        else:
            counts[func.__name__] = 1

        print(f"Funkcja {func.__name__} została wywołana {counts[func.__name__]} razy")
        return func(*args, **kwargs)

    return wrapper


def arg_check(arg):
    """Dekorator sprawdzający że został przekazany argument odpowiedniego typu"""
    def check(old_func):
        def new_func(arg_type):
            if isinstance(arg_type, arg):
                return old_func(arg)
            else:
                raise TypeError(f"Oczekiwano argumentu typu {arg.__name__}, otrzymano {type(arg_type).__name__}")
        return new_func
    return check


def timethis(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        results = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji '{func.__name__}': {execution_time:} sekund")
        return results
    return wrapper
