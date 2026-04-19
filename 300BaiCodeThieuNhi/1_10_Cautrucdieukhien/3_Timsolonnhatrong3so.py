def findMax3(a, b, c):
    if a > b:
        if b > c:
            return a
        elif b < c:
            if a > c:
                return a
            else:
                return c
    elif a < b:
        if b > c:
            return b
        else:
            return c
    else:
        return None

try:
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    c = int(input("Nhập số c: "))
    kq = findMax3(a, b, c)
    print(kq)
except ValueError:
    print("Người dùng nhập chưa chính xác")    