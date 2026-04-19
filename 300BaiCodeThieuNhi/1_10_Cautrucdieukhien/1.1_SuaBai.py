def kiemtraduongam(n):
    if n < 0:
        return "Số lẻ"
    elif n > 0:
        return "Số chẳng"
    elif n == 0:
        return "Số 0 không phải nguyên dương cũng không phải nguyên âm"
    
try:
    n = int(input("Mời bạn nhập số cần check: "))
    kq = kiemtraduongam(n)
    print(kq)
except ValueError:
    print("Bạn nhập sai vui lòng nhập 1 số hợp lệ")