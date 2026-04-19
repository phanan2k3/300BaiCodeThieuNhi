def kiemtrachangle(n):
    if n % 2 == 0:
        return "Số chẵn"
    else:
        return "Số lẻ"
    
try:
    n = int(input("Nhập số nguyên dương để kiểm tra chẳng lẻ: "))
    kq = kiemtrachangle(n)
    print(kq)
except ValueError:
    print("Mời bạn nhập đúng định dạng")