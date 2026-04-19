# Hạn chế áp dụng tính chất bắt cầu người nào muốn
# Lớn nhất thì hãy để nó so sánh với tất cả
def findMax3_1(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
try:
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    c = int(input("Nhập số c: "))
    kq = findMax3_1(a, b, c)
    print(kq)
except ValueError:
    print("Người dùng nhập chưa chính xác")    