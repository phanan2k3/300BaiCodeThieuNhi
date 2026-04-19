try:
    for i in range(1, 11, 1):
        for j in range(1, 11, 1):
            k = i * j
            print(f"{i} x {j} = {k}")
        print(f"---------------")
    
except ValueError:
    print("Nhập sai dữ liệu")