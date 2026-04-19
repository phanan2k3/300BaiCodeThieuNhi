def lists_changle(lists):
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
    l = int(input("Nhập độ dài của list: "))
    while l <= 0:
        print("Độ dài của list phải lớn hơn 0")
        l = int(input("Nhập độ dài của list: "))
    for i in range(l):
        while True:
            try:
                num = int(input("Nhập số bất kỳ vào lists: "))
                break
            except ValueError:  
                print("Lỗi")
        lists.append(num)
    print(lists)    

    chang, le = lists_changle(lists)
    print(f"Danh sách chẳng là: {chang}")
    print(f"Danh sách lẻ là: {le}")
    

except ValueError:
    print("Nhập sai dữ liệu")