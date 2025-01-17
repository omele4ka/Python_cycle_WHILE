print('Задача 2. Коллекторы')

# Напишите робота для коллекторов.
# В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор, 
# пока он не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга сообщите об этом пользователю и поблагодарите его.
 
# Пример:
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50
 
# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.
 
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!

user_name = input('Введите имя должника: ')
debt_amount = int(input('Введите сумму долга: '))

print(f'{user_name}, ваша задолженность составляет {debt_amount} рублей.')
user_money_amount = int(input('Введите сумму для погашения долга: '))

while user_money_amount < debt_amount:
    print(f'Маловато, {user_name}. Давайте ещё раз.')
    user_money_amount = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
    if user_money_amount >= debt_amount:
        break
print(f'Отлично, {user_name}! Вы погасили долг. Спасибо!')