def avgMonHoc(subjects):
    scoretb = sum(subjects) / len(subjects)
    return scoretb

def xepLoai(scoretb):
    if scoretb >= 8.5:
        return "Xuất sắc"
    elif scoretb >= 7.0 and scoretb < 8.5:
        return "Khá"
    elif scoretb >= 5.5 and scoretb < 7.0:
        return "Trung bình"
    else: 
        return "yếu"

try:
    subjects = []
    soMon = int(input("Nhập số môn bạn cần check: "))
    while soMon <= 0:
        print("Số môn không thể không có!")
        soMon = int(input("Nhập số môn bạn cần check: "))
    for i in range(soMon):
        # tenMon = input(f"Nhập tên môn học {i}: ")
        # while tenMon in subjects:
        #     print(f"Tên môn học đã tồn tại!")
        #     tenMon = input(f"Nhập tên môn học {i}: ")
        soDiem = float(input(f"Nhập số điểm tương ứng: "))
        while soDiem < 0 or soDiem > 10:
            print(f"Số điểm không được vượt qua khoảng cách từ  0 - 10")
            soDiem = float(input(f"Nhập số điểm tương ứng: "))
        subjects.append(soDiem)

    scoretb = avgMonHoc(subjects)
    print(f"Điểm trung bình là: {scoretb}")
    xepLoaiHoc = xepLoai(scoretb)
    print(f"Bạn thuộc loại: {xepLoaiHoc}")
    
except ValueError:
    print("Nhập sai dữ liệu mời nhập lại")