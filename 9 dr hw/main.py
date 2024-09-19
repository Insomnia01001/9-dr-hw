son1 = int(input("son kiriting"))
son2 = int(input("son kiriting"))
son3 = int(input("son kiriting"))
son_sort = (son1,son2,son3)
son_sort1 = son_sort.sort()
input_char = input("Ixtiyoriy belgi kiriting: ")

if input_char.isdigit():
    print("son")
elif input_char.isalpha():
    print("harf")
elif len(input_char) == 1:
    print("belgi")
else:
    print("Iltimos, faqat bitta belgi kiriting.")
son1 = int(input("son kiriting"))
son2 = int(input("son kiriting"))
son3 = int(input("son kiriting"))
result1 = son1+son2+son3
result2 = min(son1,son2,son3)
print(result1)
print(result2)


