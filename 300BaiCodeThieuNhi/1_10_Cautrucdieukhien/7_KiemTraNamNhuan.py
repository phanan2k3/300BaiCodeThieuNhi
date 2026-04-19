def checkNamNhuan(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return "Nhuận"
            else:
                return "Không nhuận"
        else:
            return "Nhuận"
    else:
        return "Không nhuận"

try:
    n = int(input("Nhập số năm bạn cần kiểm tra: "))
    while n <= 0:
        print("Số năm bạn kiểm tra phải lớn hơn 0")
        n = int(input("Nhập số năm bạn cần kiểm tra: "))
    
    kq = checkNamNhuan(n)
    print(f"Năm {n} là năm: {kq}")
except ValueError:
    print("Nhập sai dữ liệu")