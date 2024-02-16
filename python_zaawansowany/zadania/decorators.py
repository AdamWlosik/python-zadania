def logged(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        args_str = ", ".join(map(repr, args))
        kwargs_str = ", ".join(f"{key} = {value!r}" for key, value in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"Wywołałeś {func.__name__}({all_args}), która zwróciła: {result}")
        return result

    return wrapper
