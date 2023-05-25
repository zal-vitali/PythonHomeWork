# ## Задача 1. 
# Создайте пользовательский аналог метода map().

# numbers = [1,2,3,4,5]
# print(numbers)
# numbers = list(map(lambda x: x-1, numbers))
# print(numbers)

def my_map(func,list):
    result = []
    for i in list:
        result.append(func(i))
    return result

numbers = [1,2,3,4,5]
print(numbers)
numbers = list(my_map(lambda x: x-1, numbers))
print(numbers)