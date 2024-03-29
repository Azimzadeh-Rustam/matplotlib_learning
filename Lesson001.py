import matplotlib
import matplotlib.pyplot as plt

print(matplotlib.get_backend())

plt.plot([1, 2, -6, 0, 4])

# Если не вызвать эту функцию, то программа моментально отрисует график
# и сразу закроет окно, и будет выпонять программу дальше. Но при вызове этой функции,
# будет отрисован график, также остановлена работа программы до этого момента. После закрытия
# окна графика, программа будет работать дальше.
plt.show()
