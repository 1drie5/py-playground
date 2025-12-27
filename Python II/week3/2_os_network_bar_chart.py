import numpy as np
import matplotlib.pyplot as plt

grades = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D', 'E']
os_marks = [89, 86, 85, 79, 81, 80, 83, 76]
network_marks = [75, 75, 84, 83, 79, 86, 91, 79]

x = np.arange(len(grades))
width = 0.35

plt.bar(x - width/2, os_marks, width, color='orange', label='OS')
plt.bar(x + width/2, network_marks, width, color='blue', label='Network')

plt.xlabel('Grades')
plt.ylabel('Marks')
plt.title('Grade-wise Result: OS vs Network')
plt.xticks(x, grades)
plt.legend()

plt.show()
