import matplotlib.pyplot as plt

states = ['Maharashtra', 'Rajasthan', 'Uttar Pradesh', 'Gujarat',
          'Delhi', 'Madhya Pradesh', 'Tamil Nadu']

confirmed = [21506, 12720, 12328, 14721, 13738, 12715, 12526]
active = [19142, 11539, 11632, 13750, 12510, 12046, 11186]
recovered = [11879, 11116, 1654, 1735, 1167, 1524, 11312]
deceased = [485, 65, 42, 236, 1061, 145, 28]

# (a) Horizontal bar chart – confirmed cases
plt.barh(states, confirmed)
plt.xlabel("Confirmed Cases")
plt.title("State-wise Confirmed Cases")
plt.show()

# (b) Bar chart – recovered on top of active
plt.bar(states, active, color='red', label='Active')
plt.bar(states, recovered, bottom=active, color='green', label='Recovered')
plt.xlabel("States")
plt.ylabel("Cases")
plt.title("Active and Recovered Cases")
plt.legend()
plt.show()

# (c) Pie charts for Delhi and Uttar Pradesh
delhi_index = states.index('Delhi')
up_index = states.index('Uttar Pradesh')

labels = ['Active', 'Recovered', 'Deceased']

plt.pie([active[delhi_index], recovered[delhi_index], deceased[delhi_index]], labels=labels, autopct='%1.1f%%')
plt.title("COVID-19 Cases in Delhi")
plt.show()

plt.pie([active[up_index], recovered[up_index], deceased[up_index]], labels=labels, autopct='%1.1f%%')
plt.title("COVID-19 Cases in Uttar Pradesh")
plt.show()
