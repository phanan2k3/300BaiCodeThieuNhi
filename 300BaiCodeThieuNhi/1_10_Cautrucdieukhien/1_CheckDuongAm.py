# Kiem tra so nguyen duong so nguyen am
a = float(input("Nhập số nguyên bạn muốn kiểm tra: "))
def kiemtraDuongAm(a):
    if a < 0:
        print("Đây là số nguyên âm")
    else:
        print("Đây là số nguyên dương")
    return a

kq = kiemtraDuongAm(a)
print(kq)