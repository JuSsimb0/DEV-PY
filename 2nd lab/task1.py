money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
survived_months = 0

while True:
    money_capital = money_capital + salary - spend
    if money_capital < 0:
        break
    spend = spend * (1 + increase)
    survived_months += 1

print("Количество месяцев, которое можно протянуть без долгов:", survived_months)
