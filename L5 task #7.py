# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с
# фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков).
import json
with open('firms.txt', 'r+') as f_f:
    lines = f_f.read().split('\n')
    profit_list = []
    profit_dict = {}
    for line in lines:
        line = line.split()
        profit = int(line[2]) - int(line[3])
        profit_dict[str(line[0])] = profit
        print(f'{line[0]}: {profit}')
        if profit > 0:
            profit_list.append(profit)

    avg_profit = sum(profit_list) / len(profit_list)
    avg_dict = {'Average profit': avg_profit}

    final_list = [profit_dict, avg_dict]

    print(f'Average profit: {avg_profit}')
    print(profit_dict)
    print(avg_dict)
    print(final_list)
    f_f.write('\n')
    json.dump(final_list, f_f)