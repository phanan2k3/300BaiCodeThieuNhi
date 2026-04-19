def check(lists):
    chang = []
    le = []
    for i in lists:
        if i % 2 == 0:
            chang.append(i)
        else:
            le.append(i)
    return chang, le

try:
    lists = []
    l = int(input("Nhập độ dài của danh sách: "))
    while l <= 0:
        print("Độ dài phải luôn lớn hơn 0!")
        print("Đề nghị nhập lại!")
        l = int(input("Nhập độ dài của danh sách: "))
    for i in range(l):
        while True:
            try:
                num = int(input("Nhập số vào danh sách: "))
                break
            except ValueError:
                print("Lỗi")
        lists.append(num)
    print(lists)
    chang, le = check(lists)
    print(f"Danh sách chẳng: {chang}")
    print(f"Danh sách lẻ: {le}")
except ValueError:
    print("Lỗi chương trình")
