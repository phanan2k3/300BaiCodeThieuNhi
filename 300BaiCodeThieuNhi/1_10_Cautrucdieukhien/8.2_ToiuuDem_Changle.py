def countChangle(lists):
    countChang = 0
    countLe = 0
    chang = []
    le = []
    for i in lists:
        if i % 2 == 0:
            chang.append(i)
            countChang += 1
        else:
            le.append(i)
            countLe += 1
    return countChang, countLe

try:
    lists = []
    l = int(input("Nhập độ dài: "))
    while l <= 0:
        print("Độ dài k được bé hơn 0")
        l = int(input("Nhập độ dài: "))
    for i in range(l):
        while True:
            try:
                num = int(input("Nhập số bất kỳ vào list: "))
                break
            except ValueError:
                print("Lỗi")
        lists.append(num)
    print(lists)
    chang, le = countChangle(lists)
    print(f"Số đếm của danh sách chẳng là : {chang}")
    print(f"Số đếm của danh sách lẻ là : {le}")

            
except ValueError:
    print("Lỗi")