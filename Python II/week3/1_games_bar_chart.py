import numpy as np
import matplotlib.pyplot as plt

games = np.array(['Cricket', 'Football', 'Hockey', 'Tennis'])
india = np.array([60, 50, 20, 10])
others = np.array([30, 50, 25, 10])

x = np.arange(len(games))
width = 0.35

plt.bar(x - width/2, india, width, color='blue', label='India')
plt.bar(x + width/2, others, width, color='pink', label='Others')

plt.xlabel('Games')
plt.ylabel('Values')
plt.title('Games played in India vs Others')
plt.xticks(x, games.tolist())
plt.legend()

plt.show()
