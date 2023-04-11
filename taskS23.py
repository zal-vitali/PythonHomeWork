# ## Задача 3. 
# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def countSubString(substring,fhrase):
    result = []

    for els in substring:
        count = 0
        for elf in fhrase:
            if els == elf:
                count +=1
        result.append(((f'{els}-'),count))
    return result  


substring = input('Введите подстроку: ')
fhrase = input('Введите фразу: ')

print(countSubString(substring,fhrase))
