import matplotlib.pyplot as plt
import numpy as np

# В функции matplotlib нужно передавать массивы numpy
x = np.array([4, 5, 6, 7, 8])
y = np.array([1, 2, -6, 0, 4])

y = np.arange(0, 5, 1)          # [0, 1, 2, 3, 4]
x = np.array([a*a for a in y])  # [0, 1, 4, 9, 16]

y2 = [0, 1, 2, 3]
x2 = [i+1 for i in y2]
plt.plot(x, y, 'r--o', x2, y2, ':s', color='#0000CC')
plt.grid() # Добавим сетку на график
plt.show()

plt.plot(x, y)
line = plt.plot(x2, y2, color=(1, 0, 1, 0.8)) # Возвращает объект Line2D
plt.setp(line, linestyle='-.', marker='>', markerfacecolor='w', linewidth='4')
plt.grid()
plt.show()

x3 = np.arange(-2*np.pi, 2*np.pi, 0.1)
y3 = np.cos(x3)
plt.plot(x3, y3)
plt.fill_between(x3, y3, where=(y3 < 0), color='r', alpha=0.5)
plt.fill_between(x3, y3, where=(y3 > 0), color='g', alpha=0.5)
plt.grid()
plt.show()
