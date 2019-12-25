time = int(input("Введите время в секундах: "))
hour = time//3600
minute = (time - hour*3600)//60
second = time - hour*3600 - minute*60
print(f"Это будет: {hour}:{minute}:{second}")
