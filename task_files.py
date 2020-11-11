# task1
# with open('names_task1.txt', 'r') as file:
#     # print(file.read())
#     summ = 0
#     numm = 0
#     for i in file:
#         vall = int(i[len(i)-2])
#         summ = summ + vall
#         numm = numm + 1
#         if vall < 3:
#             print(i[:-1])
# print(f"Средний балл: {summ/numm}")

# task2
# file = open('task2.txt', 'r+')
# while True:
#     some = input("введите данные: ")
#     if some == '':
#         break
#     file.write(some+'\n')
# file.close()

# task3
# with open('task3.txt', 'r') as file:
#     print(f"Количество строк: {len(file.readlines())}")
#     file.seek(0)
#     lines = 1
#     for word in file.readlines():
#         words = word.split()
#         line_new = word.replace(' ', '')
#         print(f"Строка {lines}: {len(line_new)} символов, Слов: {len(words)}")
#         lines += 1

# tsak4
# with open('task4.txt', 'r') as file:
#     result = list(map(int, filter(str.isdigit, ''.join(file.readlines()))))
#     print(sum(result))

# task5
# from functools import reduce

# with open('task4.txt', 'r') as file :
#     lines = 1
#     with open('task5fin.txt', 'w+') as f :
#         for line in file.readlines():
#             nums = list(map(int, line.split()))
#             res = reduce(lambda x, y: x * y, nums)
            
#             f.writelines('Произведение чисел '+ str(lines) + ' строки: ' + str(res) + str('\n'))
#             lines += 1

# task6
# with open('task4.txt', 'r') as file :
#     lines = 1
#     with open('task6.txt', 'w+') as f :
#         for line in file.readlines() :
#             nums = list(map(int, line.split()))
#             mini = min(nums)
#             maxi = max(nums)
#             f.writelines('Строка ' + str(lines) + ': ' + 'Минимальное число - '
#                         + str(mini) + ', Максимальное число - ' + str(maxi) + str('\n'))
#             lines += 1

# task7 
# with open('task7int.txt', 'r') as file_int:
#     s_num = list(map(int, file_int.read().split()))
#     s_num = sorted(s_num)
# with open('task7out.txt', 'w') as file_out:
#     for num in s_num:
#         file_out.write(str(num) + '\n')

# task8

# hello = input('Здравствуйте!: ').lower()

# if hello == 'hello' :
#     print('''1) google_kazakstan
# 2) google_paris
# 3) google_uar
# 4) google_kyrgystan
# 5) google_san_francisco
# 6) google_germany
# 7) google_moscow
# 8) google_sweden''')

#     strana = int(input('Выберите страну (1-8): '))

#     if strana == 1 :
#         with open('google_kazakstan.txt', 'a') as f :
#             complaint = input ('Напишите свою жалобу : ')
#             f.writelines(complaint + '\n')
#             print('Спасибо! Мы записали вашу жалобу.')

#     elif strana == 2 :
#         with open('google_paris.txt', 'a') as f :
#             complaint = input ('Напишите свою жалобу : ')
#             f.writelines(complaint + '\n')
#             print('Спасибо! Мы записали вашу жалобу.')

#     elif strana == 3 :
#         with open('google_uar.txt', 'a') as f :
#             complaint = input ('Напишите свою жалобу : ')
#             f.writelines(complaint + '\n')
#             print('Спасибо! Мы записали вашу жалобу.')

#     elif strana == 4 :
#         with open('google_kyrgystan.txt', 'a') as f :
#             complaint = input ('Напишите свою жалобу : ')
#             f.writelines(complaint + '\n')
#             print('Спасибо! Мы записали вашу жалобу.')

#     elif strana == 5 :
#         with open('google_san_francisco.txt', 'a') as f :
#             complaint = input ('Напишите свою жалобу : ')
#             f.writelines(complaint + '\n')
#             print('Спасибо! Мы записали вашу жалобу.')

#     elif strana == 6 :
#         with open('google_germany.txt', 'a') as f :
#             complaint = input ('Напишите свою жалобу : ')
#             f.writelines(complaint + '\n')
#             print('Спасибо! Мы записали вашу жалобу.')

#     elif strana == 7 :
#         with open('google_moscow.txt', 'a') as f :
#             complaint = input ('Напишите свою жалобу : ')
#             f.writelines(complaint + '\n')
#             print('Спасибо! Мы записали вашу жалобу.')
            
#     elif strana == 8 :
#         with open('google_sweden.txt', 'a') as f :
#             complaint = input ('Напишите свою жалобу : ')
#             f.writelines(complaint + '\n')
#             print('Спасибо! Мы записали вашу жалобу.')

#     else :
#         print('Такой страны нет в списке')      

# else :
#     print("Напишите 'hello'")

# task9
# import json

# with open('task9.json', 'r+') as f:
#     data = json.load(f)
#     print(data['age'])

# task10
# import json

# file_json = {"name": "John",
#             "age": 30,
#             "city": "New York"
#             }

# with open('task10.json', 'r+') as f :
#     json.dump(file_json, f)