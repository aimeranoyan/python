# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.
import json
with open('lessons_quanity.txt', 'r') as f_classes:
    class_list = [line.split() for line in f_classes]
    # print(class_list)

    keys = [el[0] for el in class_list]
    values = [el[1:] for el in class_list]
    # print(keys)
    # print(values)

    for v in values:
        for i in v:
            x = '(prc)'
            if x in i:
                i = i.replace(x, '')
                print(i)
    print(values)



        # def replace_fun(target, val):
        #    for i, j in val.items():
         #       target = target.replace(i, j)
          #      val = None
           # return target



    # strn = '50(prc)'
    # print(strn.replace('(prc)', ''))








# separating lists into x: y
# for item in class_list:
# val = item.split()
# x = item[0]
# y = item[1:]
# print(x, y)
# if val != '-':
# item.remove(item[::-1])

# if item.endswith(')') == True:
# print(item)
# class_list.remove(item[1])

# x = ['(lab)', '(prc)', '(lec)']
# for n in item[n]:
# for i in x:
# if n == x[i]:
# remove
# n
# i = l_obj.remove()
# el.remove('(lab)')
# el.remove('(prc)')
# el.remove('(lec)')
# cl = el.remove('(lab)', '(prc)', '(lec)' )
# print(class_list)
# if el in ['(lab)', '(prc)', '(lec)':
# j_str = f'"{el[0]}" {sum(el[1:])}"'
# print(j_str)
# >>> s:   '{"C": [[1, 2, "string"], [3, 4, "second string"]]}'
# dict(i.split('=') for i in S.split())