

def input_check(param):    #Проверка ввода целого положительного и не буквы
    try:
        input_data = int(input(param))
        if not (input_data >= 1 ):
            raise ValueError
    except ValueError:
        print("Введите целое положительное число ")
        input_data = input_check(param)
    return input_data


tickets = input_check("Введите нужное количество билетов:")

cost = float(0)

for i in range(1, tickets + 1):    # Проверка возраста:
    age = input_check(f' Введите возраст посетителя, билет #{i}: ')

    if 18 <= age < 25:
        cost += 990
    elif age >= 25:
        cost += 1390


if tickets > 3:   # Проверка на скидку:
    cost -= 0.1 * cost

print("")
print(f"Общая сумма к оплате за {tickets:2} посетителей :{cost} руб")

