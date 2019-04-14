from random import randint
import pygal
from matplotlib import pyplot as plt

class Die():
    def __init__(self, sidenumber=6):
        self.sidenumber = sidenumber

    def roll(self):
        number = randint(1, self.sidenumber)
        return number


n = 100
results = []
die = Die()
for i in range(n):
    m = die.roll()
    results.append(m)

x = list(range(1, 7))
frequencies = []
for number in range(1, die.sidenumber+1):
    frequency = results.count(number)
    frequencies.append(frequency)
print(frequencies,x)

hist = pygal.Bar()
hist.title = "骰子情况的分布"
hist.x_labels = ['1', '2', '3', '4', '5', '6']

hist.add('D6', frequencies)
print(hist)
hist.render_to_file('D6results.svg')
# plt.bar(x, frequencies)
# plt.show()
