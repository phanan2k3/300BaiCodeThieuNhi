"""
- Nhập số lượng môn học 
- Tính Avg của các môn học
- Hiển thị ra điểm trung bình
- Căn cứ vào điểm trung bình đó để tính ra xếp loại
"""
# Hàm tính tổng các môn học
def sumMonHoc(subjects):
    # Viết biểu thức tính
    # Lấy value của dict để cộng
    subjects.values()
    return sum(subjects.values())

# Hàm tính trung bình môn học
def avgMonHoc(subjects):
    scoreTb = sumMonHoc(subjects) / len(subjects)
    return scoreTb

# Hàm xếp loại
def xepLoai(scoreTb):
    if scoreTb >= 8.5:
        return "Xuất sắc"
    elif scoreTb >= 7.0 and scoreTb < 8.5:
        return "Khá"
    elif scoreTb >= 5.5 and scoreTb < 7.0:
        return "Trung bình"
    else: 
        return "yếu"

try:
    # Khai báo giỏ hàng chứa danh sách môn học + điểm
    subjects = {}
    # Nhập số môn và điểm tương ứng
    soMon = int(input("Nhập số môn bạn muốn kiểm tra : "))
    # Kiểm tra soMon lớn hơn 0 vì môn học phải có
    while soMon <= 0:
        print("Yêu cầu nhập số môn lớn hơn 0")
        soMon = int(input("Nhập số môn bạn muốn kiểm tra : "))
    # Thêm số môn và điểm vào dict
    for i in range(soMon):
        tenMon = input("Nhập tên môn học: ")
        while tenMon in subjects:
            print(f"Môn học {tenMon} đã tồn tại ")
            tenMon = input("Nhập tên môn học: ")
        soDiem = float(input(f"Nhập số điểm tương ứng với {tenMon} : "))
        while soDiem < 0 or soDiem > 10:
            print("Điểm k bao giờ âm hay lớn hơn 10 nha người đẹp")
            soDiem = float(input(f"Nhập số điểm tương ứng với {tenMon}  : "))
        # Đưa vào dict
        subjects[tenMon] = soDiem

    scoreTb = avgMonHoc(subjects)    
    kq = xepLoai(scoreTb)
    print(scoreTb)
    print(kq)

except ValueError:
    print("Người dùng nhập value k phải là điểm")