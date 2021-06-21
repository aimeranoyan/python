# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.
with open('company_names.txt', 'w') as f_workers:
    name_salary = {
        'Ivanov': 10000.0,
        'Petrov': 15000.0,
        'Sidorov': 25000.1,
        'Ivanova': 15000.7,
        'Petrova': 19000.9,
        'Sidorova': 26000.1,
        'Oktyabrsky': 30000.5,
        'Petrovsky': 26000.4,
        'Znamensky': 12000.0,
        'Koretzky': 31000.9}

    lines = [item + ' ' + str(name_salary[item]) + '\n' for item in name_salary]

    for line in lines:
        f_workers.writelines(line)

    low_workers = [item for item in name_salary if name_salary[item] < 20000]
    avg_salary = sum(name_salary.values()) / len(name_salary.values())

    print(f'Salary is less than 20k: {low_workers} \nAvarage salary is: {avg_salary}')