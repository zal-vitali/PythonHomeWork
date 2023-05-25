# ## Задача 2. 
# Создайте декоратор, повторяющий функцию заданное количество раз.

def repeat(num):
    def our_repeat(func):
        def decorator(*args):
            for _ in range(num):
                result = func(*args)
            return result
        return decorator
    return our_repeat

@repeat(5)
def hello_world(text):
    print(text)

hello_world("Это какая-то магия. Я не понимаю, как это работает :,-(")