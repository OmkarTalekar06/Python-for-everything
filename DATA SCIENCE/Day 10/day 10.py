import random 
import matplotlib.pyplot as plt

roll_no = list(range(1,41))
Eligible = []
notEligible = []

attendence= [random.randint(40, 100) for _ in roll_no]

colors = []

for a, r in zip(attendence, roll_no):
    if a < 70:
        colors.append("red")
        notEligible.append(r)
        
    else:
        colors.append("green")
        Eligible.append(r)

print("Roll no | Attendence | Eligiblity")
print("----------------------")
for r, a in zip(roll_no, attendence):
    status = "Eligible" if a >= 70 else "Not Eligible"
    print(f"{r:6}|{a:10}%|{status}")

print("\nELigible Roll numbers : ", Eligible)
print("Not ELigible Roll numbers : ", notEligible)

plt.figure()
plt.bar(roll_no, attendence)
plt.ylim(0, 100)
plt.xlabel("Roll Number")
plt.ylabel("Attendence Percentage")
plt.title("Student Attendence Analysis")

for i in range(len(roll_no)):
    plt.bar(roll_no[i], attendence[i], color = colors[i])

plt.axhline(70, linestyle="--", label="Eligiblity Limit(70%)")
plt.legend()

plt.show()
