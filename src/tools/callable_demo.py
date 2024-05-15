class CallableWrapper:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before calling function")
        result = self.func(*args, **kwargs)
        print("After calling function")
        return result


def say_hello(name):
    print(f"Hello, {name}!")
    return f"Hello, {name}!"


# 创建 CallableWrapper 的实例，传入 say_hello 函数
wrapper = CallableWrapper(say_hello)

# 调用 wrapper 实例，它表现得像函数一样
greeting = wrapper("Alice")
print(greeting)  # 输出 "Before calling function", "After calling function", 然后是 "Hello, Alice!"
