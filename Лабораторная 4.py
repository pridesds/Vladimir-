salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов


def couting_money_capital(salary, spend, months, increase): #Расчёт необходимой подушки безопасности
    money_capital_needed = 0  #Изначально подушка безопасности равна 0

    for month in range(months):
        if salary < spend: #Если зарплаты не хватает на покрытие расходов
            money_capital_needed += (spend - salary)  #Добавляю недостаток в подушку

        spend *= (1 + increase) #Увеличиваю расходы на 3% для следующего месяца

    return round(money_capital_needed)

money_capital = couting_money_capital(salary, spend, months, increase) #Определяю необходимую подушку безопасности

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)