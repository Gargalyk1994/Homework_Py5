# ;  Напишите программу, которая на вход принимает два числа A и B, 
# ;  и возводит число А в целую степень B с помощью рекурсии.
# ; *Пример:*
# ; A = 3; B = 5 -> 243 (3⁵)
# ;     A = 2; B = 3 -> 8 
A = int(input('Введите число: '))
B = int(input("Введите степень числа: "))

def degree_numbers(A, B):
    if A**B == A:
        return A
    else:
        return A * degree_numbers(A, B-1)

print(degree_numbers(A, B))
    