def timSoNguyenTo(n):
    if n < 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1, 1):
            if n % i == 0:
                return False
        return True

                    
            
try:
    n = int(input("Nhập số cần kiểm tra: "))
    while n <= 0:
        print(f"Số phải là số nguyên dương")
        n = int(input("Nhập số cần kiểm tra: "))
    kq = timSoNguyenTo(n)
    print(kq)
except ValueError:
    print("Lỗi")