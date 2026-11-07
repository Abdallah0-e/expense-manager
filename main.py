balance = 0
transactions = []

# تحميل البيانات القديمة
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

        if lines:
            balance = float(lines[0].strip())

            for line in lines[1:]:
                transactions.append(line.strip())

except FileNotFoundError:
    pass


while True:
    print("\n===== إدارة المصروفات =====")
    print("1- إضافة دخل")
    print("2- إضافة مصروف")
    print("3- عرض الرصيد")
    print("4- عرض السجل")
    print("5- حفظ البيانات")
    print("6- خروج")

    choice = input("اختر: ")

    if choice == "1":
        income = float(input("أدخل مبلغ الدخل: "))
        balance += income
        transactions.append(f"دخل: +{income}")
        print("تمت الإضافة بنجاح")

    elif choice == "2":
        expense = float(input("أدخل مبلغ المصروف: "))
        balance -= expense
        transactions.append(f"مصروف: -{expense}")
        print("تمت الإضافة بنجاح")

    elif choice == "3":
        print(f"الرصيد الحالي: {balance}")

    elif choice == "4":
        print("\nسجل العمليات:")

        if not transactions:
            print("لا توجد عمليات")
        else:
            for item in transactions:
                print(item)

    elif choice == "5":

        with open("data.txt", "w", encoding="utf-8") as file:
            file.write(str(balance) + "\n")

            for item in transactions:
                file.write(item + "\n")

        print("تم حفظ البيانات بنجاح")

    elif choice == "6":
        print("وداعاً")
        break

    else:
        print("خيار غير صحيح")