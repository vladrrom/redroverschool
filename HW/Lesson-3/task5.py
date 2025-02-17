sum = 0
while True:
    try:
        n = int(input("Введите целое число:"))
        if n < 0:
            break
        sum += n
    except ValueError:
        print("На вход должно подаваться целое число.")
print(sum)