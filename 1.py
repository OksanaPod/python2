#Задача 1.  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

N = (input (f"Введите число: "))
sum=0

for i in range(len(N)):
    if N[i] != "." and N[i] != ",":
        sum=sum+ int(N[i])
print(sum)