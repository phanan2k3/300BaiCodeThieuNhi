def leap_year(year):
    if year % 4 != 0:
        return "Không nhuận" 
    elif year % 100 == 0 and year % 400 != 0:
        return "Không nhuận"
    else:
        return "Nhuận"
    
try:
    year = int(input("Nhập số năm bạn cần kiểm tra: "))
    while year <= 0:
        print("Số năm bạn kiểm tra phải lớn hơn 0")
        year = int(input("Nhập số năm bạn cần kiểm tra: "))
    
    kq = leap_year(year)
    print(f"Năm {year} là năm: {kq}")
except ValueError:
    print("Nhập sai dữ liệu")