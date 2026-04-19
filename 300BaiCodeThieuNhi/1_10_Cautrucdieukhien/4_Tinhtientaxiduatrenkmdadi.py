"""Bài toán yêu cầu chúng ta 
tính tiền dựa trên km đã di
1. gia dinh 1 km dau tien la 10.000vnd -> 1m = 10000 / 1000= 10d
2. tu km thu 2 den 10 la 8.500 vaf km 11 la 7.500
2 -> 10 khoang cach trong nay la 9km moi 1 km la 8500
 1 km = 1000m vay 1m = 8500/1000 = 8.5
3. tuong tu cho km 11 tro di
cu 1 km tăng lên 7.500 vay 1m = 7500 / 1000 = 7.5
+ tổng lại là  x + y + z
tuy nhiên đây là cách tính xàm vì người ta toàn lấy đủ số chứ ai rảnh mà tính theo m rồi sao lời
"""
def countTaxiCash_Km(km):
    x = 0
    if km <= 1:
        x = 10000
    elif km > 1 and km < 11:
        x = 10000  + ((km - 1) * 8500)
    else: 
        x = 10000  + 9 * 8500 + ((km - 10) * 7500)
    return x

try:
    km = int(input("Xin mời nhập quãng đường bạn chạy: "))
    if km < 0:
        print("Quãng đường k có âm nhe người đẹp")
    else:
        kq = countTaxiCash_Km(km)
        print(kq)
except ValueError:
    print("Người dùng nhập sai quãng đường chạy")
