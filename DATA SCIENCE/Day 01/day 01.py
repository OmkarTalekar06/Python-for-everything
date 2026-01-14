import matplotlib.pyplot as plt
import statistics

marks = [78, 85, 43, 54 , 72, 66, 95, 60]

students = list(range(1, len(marks) + 1))

mean = sum(marks) / len(marks)
median = statistics.median(marks)

print("Marks : ", marks)
print("Mean : ", mean)
print("Median : ", median)

plt.bar(students, marks, color='skyblue')
plt.xlabel("Roll Number")
plt.ylabel("Marks")
plt.title("Student's performance")
plt.ylim(0, 100)
plt.xticks(students)

for i, mark in enumerate(marks):
    plt.text(students[i], mark+1,str(mark), ha='center')


plt.axhline(mean, color='red', linestyle = '--', label=f'Mean = {mean:.2f}')
plt.legend()
plt.show()

plt.plot(students, marks, marker='o', color="green")
plt.xlabel("Roll Number")
plt.ylabel("Marks")
plt.title("Students performance line graph")
plt.ylim(0, 100)
plt.xticks(students)

plt.axhline(mean, color="red", linestyle='--', label=f"Mean = {mean:.2f}")
plt.legend()
plt.show()
