def countChangle(lists):
    countChang = 0
    countLe = 0
    for i in lists:
        if i % 2 == 0:
            countChang += 1
        else:
            countLe += 1
    return countChang, countLe

try:
    
    l = input("Nhập dãy số nguyên, cách nhau bởi dấu , nhé! : ")
    lists = [int(num) for num in l.split()]
    chang, le = countChangle(lists)
    print(f"Số đếm của danh sách chẳng là : {chang}")
    print(f"Số đếm của danh sách lẻ là : {le}")

        
except ValueError:
    print("Lỗi")