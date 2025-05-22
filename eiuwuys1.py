import random

number = random.randint(1, 100)
print("Tôi đã chọn một số từ 1 đến 100. Đoán xem!")

while True:
    guess = int(input("Nhập số bạn đoán: "))
    if guess < number:
        print("Quá nhỏ!")
    elif guess > number:
        print("Quá lớn!")
    else:
        print("Chính xác! Bạn đã thắng!")
        break
