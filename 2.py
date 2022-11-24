#Задача 2.  Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

N = int(input (f"Введите число: "))

def multi(x):
    if x == 1:
        return 1
    else:
        return x * multi(x - 1)

list = []
for i in range(1, N + 1):
    list.append(multi(i))

print(f"Произведения чисел от 1 до {N}:  {list}")