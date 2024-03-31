def sliding_window(func, xs, n):
    for i in range(len(xs)-n+1):
        yield func(xs[i:i+n])


def fibonnaci():
    num1, num2 = 0, 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2


def deprecated(func):
    def wrapper(*args, **kwargs):
        print(f"Warning: {func.__name__} deprecated.")
        return func(*args, **kwargs)
    return wrapper


def deprecated_first_use(func): # возмножны другие варианты, см. консультацию 22.03.2024
    def wrapper(*args, **kwargs):
        if not wrapper.called:
            print(f"Warning: {func.__name__} deprecated.")
            wrapper.called = True
        return func(*args, **kwargs)
    wrapper.called = False
    return wrapper


def cached(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper
