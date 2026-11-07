import tkinter as tk
from tkinter import messagebox

balance = 0

def update_balance():
    label_balance.config(text=f"الرصيد: {balance:.2f}")

def add_income():
    global balance

    try:
        amount = float(entry.get())
        balance += amount

        listbox.insert(tk.END, f"دخل +{amount}")

        update_balance()
        entry.delete(0, tk.END)

    except:
        messagebox.showerror("خطأ", "أدخل رقم صحيح")

def add_expense():
    global balance

    try:
        amount = float(entry.get())
        balance -= amount

        listbox.insert(tk.END, f"مصروف -{amount}")

        update_balance()
        entry.delete(0, tk.END)

    except:
        messagebox.showerror("خطأ", "أدخل رقم صحيح")


window = tk.Tk()
window.title("إدارة المصروفات")
window.geometry("500x500")

title = tk.Label(
    window,
    text="برنامج إدارة المصروفات",
    font=("Arial", 18)
)
title.pack(pady=10)

label_balance = tk.Label(
    window,
    text="الرصيد: 0",
    font=("Arial", 16)
)
label_balance.pack()

entry = tk.Entry(
    window,
    font=("Arial", 14)
)
entry.pack(pady=10)

btn_income = tk.Button(
    window,
    text="إضافة دخل",
    bg="green",
    fg="white",
    command=add_income
)
btn_income.pack(pady=5)

btn_expense = tk.Button(
    window,
    text="إضافة مصروف",
    bg="red",
    fg="white",
    command=add_expense
)
btn_expense.pack(pady=5)

tk.Label(
    window,
    text="سجل العمليات",
    font=("Arial", 14)
).pack(pady=10)

listbox = tk.Listbox(
    window,
    width=50,
    height=12
)
listbox.pack()

window.mainloop()