canprint("🧮 آلة حاسبة بسيطة")
print("اختاري العملية: +  -  *  /")

num1 = float(input("دخلي الرقم الأول: "))
operation = input("دخلي العملية: ")
num2 = float(input("دخلي الرقم التاني: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("عملية غلط!")
    result = "مفيش"

if result != "مفيش":
    print(f"النتيجة = {result}")
