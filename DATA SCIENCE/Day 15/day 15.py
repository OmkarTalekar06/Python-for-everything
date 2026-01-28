import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


activities = ["Walking", "Running", "Gym", "Yoga"]
minutes = [30, 20, 45, 15]


root = tk.Tk()
root.title("Fitness Activity Dashboard")
root.geometry("900x500")

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)


left_frame = tk.Frame(main_frame, padx=20)
left_frame.pack(side="left", fill="y")

tk.Label(
    left_frame,
    text="Daily Fitness Time (minutes)",
    font=("Arial", 14, "bold")
).pack(pady=10)

entries = []

for i, act in enumerate(activities):
    tk.Label(left_frame, text=act).pack()
    e = tk.Entry(left_frame, width=10)
    e.insert(0, minutes[i])
    e.pack(pady=4)
    entries.append(e)


right_frame = tk.Frame(main_frame)
right_frame.pack(side="right", fill="both", expand=True)

fig = Figure(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=right_frame)
canvas.get_tk_widget().pack(fill="both", expand=True)


def draw_graphs():
    fig.clear()

   
    ax1 = fig.add_subplot(221)
    ax1.bar(activities, minutes)
    ax1.set_title("Activity-wise Time")
    ax1.set_ylabel("Minutes")

   
    ax2 = fig.add_subplot(222)
    ax2.plot(activities, minutes, marker='o')
    ax2.set_title("Fitness Trend")
    ax2.set_ylabel("Minutes")

   
    ax3 = fig.add_subplot(212)
    ax3.pie(minutes, labels=activities, autopct="%1.1f%%")
    ax3.set_title("Activity Distribution")

    fig.tight_layout()
    canvas.draw()

def auto_update(event=None):
    for i in range(len(entries)):
        value = entries[i].get()
        minutes[i] = int(value) if value.isdigit() else 0
    draw_graphs()

for entry in entries:
    entry.bind("<KeyRelease>", auto_update)

draw_graphs()
root.mainloop()
