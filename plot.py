from os import system
import numpy as np
from matplotlib import pyplot as plt

x = 0.05 * np.arange(21)
y = np.zeros(21)
for i in range(21):
	system("./encoder.sh ./data/maze/grid10.txt " + str(i/20.0) + " > mdpfile")
	system("./valueiteration.sh mdpfile > value_and_policy_file")
	system("./decoder.sh ./data/maze/grid10.txt value_and_policy_file " + str(i/20.0) + " > solution")
	f = open("solution", "r")
	y[i] = len(f.readline().split())

plt.plot(x, y)
plt.ylabel('Number of actions to reach end state')
plt.xlabel('p')
plt.show()

