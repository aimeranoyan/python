revenue = int(input("Enter company's revenue: "))
costs = int(input("Enter company's costs: "))
if revenue > costs:
    print('Your profit is positive')
    profit = revenue - costs
    profitability = profit / costs
    print(f"{profitability:.3f}")
elif revenue == costs:
    print('You have no profit and no loss')
else:
    print('You went to a loss')

workers = int(input('Enter the number of workers: '))
profit_per_worker = profit / workers
print(profit_per_worker)