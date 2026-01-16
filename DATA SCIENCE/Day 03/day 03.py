import tkinter as tk
import matplotlib.pyplot as plt


expenses = {
    "January": [], "February": [], "March": [], "April": [],
    "May": [], "June": [], "July": [], "August": [],
    "September": [], "October": [], "November": [], "December": []
}

def add_expense():
    value = entry.get()
    month = month_var.get()

    if value.isdigit():
        expenses[month].append(int(value))
        listbox.insert(tk.END, f"{month} : ₹{value}")
        entry.delete(0, tk.END)
        update_result()

def update_result():
    total = sum(sum(v) for v in expenses.values())
    count = sum(len(v) for v in expenses.values())
    average = total / count if count else 0
    total_label.config(text=f"Total Expense: ₹{total}")
    avg_label.config(text=f"Average Expense: ₹{average:.2f}")

def show_bar_chart():
    months = []
    totals = []

    for month , vals in expenses.items():
        if vals:
            months.append(month)
            totals.append(sum(vals))
        
    if not totals:
        return
    
    plt.figure(figsize=(10, 5))
    plt.bar(months, totals)

    plt.xlabel("Months")
    plt.ylabel("Total Expense")
    plt.title("Monthly Expense Bar Graph")
    plt.ylim(0, 10000)

    plt.xticks(rotation=45)

    for i, value in enumerate(totals):
        plt.text(months[i], value  + 100, str(value), ha='center')
    
    plt.tight_layout()
    plt.show()

root = tk.Tk()
root.title("Monthly Expense Analyzer")
root.geometry("420x520")

tk.Label(root, text="Enter Expense Amount").pack(pady=5)

entry = tk.Entry(root, width=15)
entry.pack(pady=5)


action_frame = tk.Frame(root)
action_frame.pack(pady=5)

tk.Button(action_frame, text="Add Expense", command=add_expense).pack(side=tk.LEFT, padx=5)

month_var = tk.StringVar(value="January")
tk.OptionMenu(action_frame, month_var, *expenses.keys()).pack(side=tk.LEFT, padx=5)

tk.Label(root, text="Expenses List").pack(pady=5)

listbox = tk.Listbox(root, height=8, width=40)
listbox.pack(pady=5)

total_label = tk.Label(root, text="Total Expense: ₹0")
total_label.pack(pady=5)

avg_label = tk.Label(root, text="Average Expense: ₹0")
avg_label.pack(pady=5)

tk.Button(root, text="Show Bar Graph", command=show_bar_chart).pack(pady=10)

root.mainloop()
