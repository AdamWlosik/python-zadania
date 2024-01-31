def print_doc(function):
    def wrapper(*args, **kwargs):
        self = args[0]
        print(self.__class__.__doc__)
        return function(*args, **kwargs)

    return wrapper
