goods = []
features = {'Name': '', 'Cost': '', 'Quantity': '', 'Unit': ''}
analytics = {'Name': [], 'Cost': [], 'Quantity': [], 'Unit': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Continue - 'Enter'\n For exit press 'E'\n For analytics press 'A'").upper()
    if control == 'E':
        break
    num += 1
    if control == 'A':
        print(f'\n Current analytics: \n {"." * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]}: {value}')
            print("." * 30)
    for f in features.keys():
        feature_ = input(f'Enter characteristic "{f}": ')
        features[f] = int(feature_) if (f == 'Cost' or f == 'Quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))

goods = int(input("Enter a quantity of goods "))
n = 1
my_dict = []
my_list = []
my_analysis = {}
while n <= goods:
    my_dict = dict({'Name': input("Enter a name "), 'Cost': input("Enter a cost "),
                    'Quantity': input('Enter a quantity '), 'Unit': input("Enter a unit ")})
    my_list.append((n, my_dict))
    n += 1
    my_analysis = dict(
        {'Name': my_dict.get('Name'), 'Cost': my_dict.get('Cost'), 'Quantity': my_dict.get('Quantity'),
         'Unit': my_dict.get('Unit')})
print(my_list)
print(my_analysis)