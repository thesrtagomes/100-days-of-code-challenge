amount_of_money = 1000
for year in range(10):
    amount_of_money += amount_of_money * 0.05
    print(f'Year {year+1} is: ${amount_of_money:.2f}')
