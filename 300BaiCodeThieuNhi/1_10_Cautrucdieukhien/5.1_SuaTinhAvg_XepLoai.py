def sumMonHoc(subjects):
    return sum(subjects.values())

def avgMonHoc(subjects):
    scoreTB = sumMonHoc(subjects) / len(subjects)
    return scoreTB

def xepLoai(scoreTB):
    if scoreTB >= 8.5:
        return "Xuất sắc"
    elif scoreTB >= 7.0 and scoreTb < 8.5:
        return "Khá"
    elif scoreTB >= 5.5 and scoreTb < 7.0:
        return "Trung bình"
    else: 
        return "yếu"

try:
    subjects = {}
    soMon = int(input("Nhập số môn bạn cần check: "))
    while soMon <= 0:
        print("Số môn k thể không có đề nghị nhập lại! ")
        soMon = int(input("Nhập số môn bạn cần check: "))
    for i in range(soMon):
        tenMon = input("Mời bạn nhập tên môn học: ")
        while tenMon in subjects:
            print(f"Môn {tenMon} học này đã tồn tại đề nghị nhập lại! ")
            tenMon = input("Mời bạn nhập tên môn học: ")
        soDiem = float(input(f"Nhập số điểm bạn đạt được tương ứng với môn {tenMon}: "))
        while 0 < soDiem or soDiem > 10:
            print(f"Số điểm không được vượt quá khoảng cách từ 0 - 10, Yêu cầu nhập lại!")
            soDiem = float(input(f"Nhập số điểm bạn đạt được tương ứng với môn {tenMon}: "))
        subjects[tenMon] = soDiem

    # Hiển thị kết quả     
    scoreTB = avgMonHoc(subjects)
    print(f"Số điểm trung bình bạn đạt được là: {scoreTB}")
    xepLoaiHoc = xepLoai(scoreTB)
    print(f"Bạn được xếp vào loại: {xepLoaiHoc}")
except ValueError:
    print("Lỗi nhập liệu")