# ## Задача 1. 
# Дано натуральное число N. 
# Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.

#60 -> 2, 2, 3, 5

multipier = list()

def multiplierList(number,multipier):
    for i in range(2, number + 1):
        if number == 1:
            return multipier
        elif number % i == 0:
            multipier.append(str(i))
            return multiplierList(number//i, multipier)

number = 7777777
multiplierList(number,multipier)
print(f"{number} -> {multipier}")