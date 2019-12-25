num = int(input("Введите число: "))
n = num
max_n = 0
while n > 0:
    if n % 10 == 9:
        max_n = 9
        break
    if n % 10 > max_n:
        max_n = n % 10
    n //= 10

print(f"Максимальная цифра в числе {num} - это {max_n}")
