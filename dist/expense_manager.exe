import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json
import os

DATA_FILE = "data.json"

balance = 0
transactions = []

# تحميل البيانات
if os.path.exists(DATA_FILE):
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            balance = data.get("balance", 0)
            transactions = data.get("transactions", [])
    except:
        pass


def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            {
                "balance": balance,
                "transactions": transactions
            },
            file,
            ensure_ascii=False,
            indent=4
        )


def update_balance():
    balance_label.config(
        text=f"الرصيد الحالي: {balance:.2f} جنيه"
    )


def refresh_list(data=None):

    listbox.delete(0, tk.END)

    if data is None:
        data = transactions

    for item in data:

        text = (
            f"{item['date']} | "
            f"{item['type']} | "
            f"{item['category']} | "
            f"{item['amount']:.2f} جنيه"
        )

        listbox.insert(tk.END, text)


def add_income():
    global balance

    try:
        amount = float(amount_entry.get())

        transactions.append({
            "type": "دخل",
            "category": "دخل",
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

        balance += amount

        save_data()
        refresh_list()
        update_balance()

        amount_entry.delete(0, tk.END)

    except:
        messagebox.showerror("خطأ", "أدخل رقم صحيح")


def add_expense():

    global balance

    try:
        amount = float(amount_entry.get())

        transactions.append({
            "type": "مصروف",
            "category": category_var.get(),
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

        balance -= amount

        save_data()
        refresh_list()
        update_balance()

        amount_entry.delete(0, tk.END)

    except:
        messagebox.showerror("خطأ", "أدخل رقم صحيح")


def delete_transaction():

    global balance

    selected = listbox.curselection()

    if not selected:
        return

    index = selected[0]

    transaction = transactions[index]

    if transaction["type"] == "دخل":
        balance -= transaction["amount"]
    else:
        balance += transaction["amount"]

    transactions.pop(index)

    save_data()
    refresh_list()
    update_balance()


def clear_all():

    global balance
    global transactions

    answer = messagebox.askyesno(
        "تأكيد",
        "هل تريد حذف كل البيانات؟"
    )

    if answer:
        balance = 0
        transactions = []

        save_data()
        refresh_list()
        update_balance()


def search_transactions():

    key = search_entry.get().strip()

    if key == "":
        refresh_list()
        return

    result = []

    for item in transactions:

        if (
            key.lower() in item["type"].lower()
            or key.lower() in item["category"].lower()
            or key.lower() in item["date"].lower()
            or key in str(item["amount"])
        ):
            result.append(item)

    refresh_list(result)


def show_stats():

    income = sum(
        t["amount"]
        for t in transactions
        if t["type"] == "دخل"
    )

    expenses = sum(
        t["amount"]
        for t in transactions
        if t["type"] == "مصروف"
    )

    report = (
        f"إجمالي الدخل: {income:.2f} جنيه\n\n"
        f"إجمالي المصروفات: {expenses:.2f} جنيه\n\n"
        f"الرصيد الحالي: {balance:.2f} جنيه"
    )

    messagebox.showinfo(
        "الإحصائيات",
        report
    )


def export_excel():

    if not transactions:
        messagebox.showwarning(
            "تنبيه",
            "لا توجد بيانات للتصدير"
        )
        return

    wb = openpyxl.Workbook()
    ws = wb.active

    ws.title = "التقرير"

    ws.append([
        "التاريخ",
        "النوع",
        "التصنيف",
        "المبلغ"
    ])

    for item in transactions:

        ws.append([
            item["date"],
            item["type"],
            item["category"],
            item["amount"]
        ])

    income = sum(
        t["amount"]
        for t in transactions
        if t["type"] == "دخل"
    )

    expenses = sum(
        t["amount"]
        for t in transactions
        if t["type"] == "مصروف"
    )

    ws.append([])
    ws.append(["إجمالي الدخل", income])
    ws.append(["إجمالي المصروف", expenses])
    ws.append(["الرصيد الحالي", balance])

    wb.save("financial_report.xlsx")

    messagebox.showinfo(
        "نجاح",
        "تم إنشاء ملف financial_report.xlsx"
    )


window = tk.Tk()

window.title("Financial Manager Pro")
window.geometry("900x700")

title = tk.Label(
    window,
    text="💰 Financial Manager Pro",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

balance_label = tk.Label(
    window,
    text="الرصيد الحالي: 0",
    font=("Arial", 16)
)
balance_label.pack(pady=10)

amount_entry = tk.Entry(
    window,
    width=25,
    font=("Arial", 14)
)
amount_entry.pack(pady=5)

categories = [
    "طعام",
    "مواصلات",
    "إنترنت",
    "فواتير",
    "تعليم",
    "ترفيه",
    "أخرى"
]

category_var = tk.StringVar()
category_var.set(categories[0])

category_menu = tk.OptionMenu(
    window,
    category_var,
    *categories
)
category_menu.pack(pady=5)

tk.Button(
    window,
    text="إضافة دخل",
    width=20,
    bg="green",
    fg="white",
    command=add_income
).pack(pady=2)

tk.Button(
    window,
    text="إضافة مصروف",
    width=20,
    bg="red",
    fg="white",
    command=add_expense
).pack(pady=2)

tk.Button(
    window,
    text="عرض الإحصائيات",
    width=20,
    bg="blue",
    fg="white",
    command=show_stats
).pack(pady=2)

tk.Button(
    window,
    text="تصدير Excel",
    width=20,
    bg="purple",
    fg="white",
    command=export_excel
).pack(pady=2)

tk.Button(
    window,
    text="حذف العملية المحددة",
    width=20,
    bg="orange",
    command=delete_transaction
).pack(pady=2)

tk.Button(
    window,
    text="حذف جميع البيانات",
    width=20,
    bg="darkred",
    fg="white",
    command=clear_all
).pack(pady=2)

search_entry = tk.Entry(
    window,
    width=30
)
search_entry.pack(pady=5)

tk.Button(
    window,
    text="بحث",
    command=search_transactions
).pack()

listbox = tk.Listbox(
    window,
    width=110,
    height=20
)
listbox.pack(pady=10)

refresh_list()
update_balance()

window.mainloop()