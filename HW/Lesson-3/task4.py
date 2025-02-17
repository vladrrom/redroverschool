message = input("Введите текст:")
kirl_gls = ("аеиоуыэюя")
count = 0
for letter in message:
    if letter in kirl_gls:
        count += 1
print(count)