# Дополнительное практическое задание по модулю: "Основные операторы"

# сначала вводим целое число от 3 до 20 и проверяем его на соответствие условию задачи
while True:
    n = int(input("Введите целое число от 3 до 20: "))
    if (n >= 3) and (n <= 20):
        break
    else:
        print()
        print(f"Вы ввели неправильное число {n}! Попробуйте еще раз!")
        print()

print()
print(f"Ваше число: {n}")
print()

# теперь для введенного числа формируем пароль пока в виде строки (str).

result = ""                             # переменная для пароля пока в виде строки (str)

for i in range(1, ((n // 2) + 2)):
    for j in range((i + 1), n):
        if i + j > n:
            break
        else:
            if n % (i + j) == 0:
                result += str(i) + str(j)

print(f"Пароль в виде строки (str): {result}")
print()

# переводим пароль в целое число
result = int(result)
print(f"Пароль в виде целого числа (int): {result}")

