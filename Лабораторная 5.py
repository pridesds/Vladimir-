money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов


def months_without_debt(money_capital, salary, spend, increase): #Определение кол-ва месяцев
    months = 0
    while money_capital >= 0:

        months += 1

        #Вычитаю расходы из подушки безопасности
        money_capital += salary  #Добавляю зарплату
        money_capital -= spend  #Вычитаю расходы

        #Когда подушка закончится цикл остановится
        if money_capital < 0:
            months -= 1  #Убираю текущий месяц, так как в нем деньги закончились
            break

        spend *= (1 + increase) #Увеличиваю расходы на 0,05 в каждом следующем месяце

    return months

months = months_without_debt(money_capital, salary, spend, increase)

print("Количество месяцев, которое можно протянуть без долгов:", months)