# Вычислить число c заданной точностью d
nums = float(input("введите число которое необходимо округлить: "))
d = float(input(" введите точность округления d в формате (d=0.01): "))
count=0
while d!=float(1):
    d=d*10
    count+=1
iStr=str(nums)
iInt=float(iStr[:3+count-1:])
print(iInt)

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# nums = int(input())
# listDel = []
# for i in range(2,nums):
#     while i**2 <= nums: # перебор до минимально делителя
#         if nums % i == 0:
#             listDel.append(i)
#             nums //= i
#         else:
#             break
# if nums > 1: # добавление в список наименьшего делителя
#     listDel.append(nums)
# print(listDel)

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# from random import randint
# listNums = [randint(0,5) for i in range(10)]
# print(f"исходный список {sorted(listNums)}")
# finalListNums =[]
# for i in range(len(listNums)):
#     count =0
#     for j in range(len(listNums)):
#         if listNums[i]==listNums[j]:
#             count+=1
#     if count==1:
#         finalListNums.append(listNums[i])
# print(f"вывод уникальных НЕПОВТОРЯЮЩИХСЯ значений {sorted(finalListNums)}")
# unique = list(set(listNums))
# for i in listNums:
#     if i not in finalListNums:
#         finalListNums.append(i)
# print(f"вывод значений без повторений {sorted(finalListNums)}")

# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# import random
# k = int(input("Введите натуральную степень k = "))
# inputZnach = [random.randint(0, 100) for i in range(k + 1)]
# outputTxt = ''
# if k == 0:
#     outputTxt = 'x = 0'
# else:
#     for i in range(len(inputZnach)):
#         if i != len(inputZnach) - 1 and inputZnach[i] != 0 and i != len(inputZnach) - 2: 
#             outputTxt += f'{inputZnach[i]}x^{len(inputZnach) - i - 1} + '
#         elif i == len(inputZnach) - 2 and inputZnach[i] != 0: 
#             outputTxt += f'{inputZnach[i]}x'
#             if inputZnach[i] != 0:
#                 outputTxt += ' + '
#         elif i == len(inputZnach) - 1 and inputZnach[i] != 0: 
#             outputTxt += f'{inputZnach[i]}  = 0'
#         elif i == len(inputZnach) - 1 and inputZnach[i] == 0: 
#             outputTxt += 'x = 0'
# file = open('text.txt', 'w')
# for i in outputTxt:
#     file.write(i)
# file.close()