print('Задача 6. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.

money_amount = int(input('Сколько денег на вашем счету? '))
interest_rate = int(input('Введите процентную ставку: '))
desired_income = int(input('Введите желаемую сумму денег: '))
year_counter = 0

while money_amount < desired_income:
    annual_income = money_amount / 100 * interest_rate
    money_amount = int(money_amount + annual_income)
    year_counter += 1
print(f'{year_counter} лет до вашей цели')