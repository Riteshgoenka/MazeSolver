import numpy as np
from os import sys

np.random.seed(0)
f = open(sys.argv[1], "r")
grid = []
for line in f:
	grid.append(list(map(int, line.split())))
f.close()
n = len(grid)
states = [[-1 for _ in range(n)] for _ in range(n)]
state = 0
for i in range(n):
	for j in range(n):
		if(grid[i][j] == 2):
			s = state
			x = i
			y = j
		if(grid[i][j] == 3):
			e = state
		if(grid[i][j] != 1):
			states[i][j] = state
			state += 1
S = state
f = open(sys.argv[2], "r")
Pi = []
for line in f:
	Pi.append(int(line.split()[1]))
f.close()
if(len(sys.argv) == 4):
	p = float(sys.argv[3])
else:
	p = 1
state = s
Direction = ['N', 'W', 'E', 'S']
X = [-1, 0, 0, 1]
Y = [0, -1, 1, 0]
while(1):
	a = Pi[state]
	if(p < 1):
		validActions = []
		probActions = []
		for b in range(4):
			if(x+X[b] >= 0 and y+Y[b] < n and x+X[b] >= 0 and y+Y[b] < n):
				if(grid[x+X[b]][y+Y[b]] != 1):
					validActions.append(b)
		numValidActions = len(validActions)
		for b in validActions:
			if(a == b):
				probActions.append(p+(1.0-p)/numValidActions)
			else:
				probActions.append((1.0-p)/numValidActions)
		a = np.random.choice(validActions, p=probActions)
	x += X[a]
	y += Y[a]
	state =	states[x][y]
	if(state == e):
		print(Direction[a])
		break
	print(Direction[a]),
