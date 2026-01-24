import tkinter as tk
import matplotlib.pyplot as plt
import csv
import os

orders = []

def add_order():
    category = category_var.get()
    platform = platform_var.get()
    amount = amount_entry.get()

    if amount.isdigit():
        amount = int(amount)
        orders.append([platform, category, amount])

        listbox.insert(tk.END, f"{platform} | {category} | ${amount}")
        amount_entry.delete(0, tk.END)
        update_summary()

def update_summary():
    total = sum(order[2] for order in orders )
    count = len(orders)
    avg = total / count if count else 0

    total_label.config(text=f"Total Amount: ${total}")
    avg_label.config(text=f"Average Order: ${avg:2f}")

def save_to_csv():

    file_path = os.path.join(os.path.dirname(__file__), "orders.csv")
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)

        for order in orders:
            writer.writerow(order)
    
    orders.clear()
    listbox.delete(0, tk.END)

def show_graph():
    platform_totals= {}
    
    for order in orders:
        platform = order[0]
        amount = order[2]

        if platform in platform_totals:
            platform_totals[platform] += amount
        else:
            platform_totals[platform] = amount

    if not platform_totals:
        return

    plt.figure()
    plt.bar(platform_totals.keys(), platform_totals.values())
    plt.xlabel("E-Commerce Platform")
    plt.ylabel("Total Amount")
    plt.title("Platform wise spendings")
    plt.show()

root = tk.Tk()
root.title("Ecommerce orders summary")
root.geometry("460x560")

tk.Label(root, text="Select Platform").pack(pady=5)
platform_var = tk.StringVar(value="Amazon")
tk.OptionMenu(root, platform_var, "Amazon", "Flipcart", "Myntra", "Ajio", "Meesho").pack()

tk.Label(root,text="Select Category").pack(pady=5)
category_var = tk.StringVar(value="Electronics")
tk.OptionMenu(root, category_var, "Electronics", "Clothing", "Groceries", "Books", "Others").pack()

tk.Label(root, text="Enter Amount").pack(pady=5)
amount_entry = tk.Entry(root, width=20)
amount_entry.pack(pady=5)

tk.Button(root, text="Add Order", command=add_order).pack(pady=5)
tk.Button(root, text="Show Graph", command=show_graph).pack(pady=5)
tk.Button(root, text="Save Orders to CSV", command=save_to_csv).pack(pady=5)

tk.Label(root, text="Added Orders").pack(pady=5)
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=5)

total_label = tk.Label(root, text="Total Amount : $0")
total_label.pack(pady=5)

avg_label = tk.Label(root, text="Average Order: $0")
avg_label.pack(pady=5)

root.mainloop()
