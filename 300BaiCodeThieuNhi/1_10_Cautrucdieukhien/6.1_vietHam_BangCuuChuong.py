def bangCuuChuong(a, b):
    for i in range(1, a + 1, 1):
        for j in range(1, b + 1, 1):
            k = i * j
            print(f"{i} x {j} = {k}")
        print(f"---------------")
    

        

try:
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    bangCuuChuong(a, b)
    
except ValueError:
    print(f"Lỗi nhập ký tự")