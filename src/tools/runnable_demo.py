class Runnable:
    def __init__(self, func):
        self.func = func

    def __or__(self, other):
        def chained_func(*args, **kwargs):
            return other(self.func(*args, **kwargs))

        return Runnable(chained_func)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


def add(x, y):
    return x + y


add_runner = Runnable(add)
print(add_runner(1, 2))  # 3


def double(x):
    return x * 2


double_runner = Runnable(double)


# 6  # add_runner.__or__(double_runner) -> double_runner(add_runner(1, 2)) -> double_runner(3) -> double(3) -> 6
result_runner = add_runner | double_runner
print(result_runner(1, 2))
