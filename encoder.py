from os import sys

f = open(sys.argv[1], "r")
grid = []
for line in f:
	grid.append(list(map(int, line.split())))
f.close()
if(len(sys.argv) == 3):
	p = float(sys.argv[2])
else:
	p = 1
n = len(grid)
states = [[-1 for _ in range(n)] for _ in range(n)]
state = 0
for i in range(n):
	for j in range(n):
		if(grid[i][j] == 2):
			s = state
		if(grid[i][j] == 3):
			e = state
		if(grid[i][j] != 1):
			states[i][j] = state
			state += 1
S = state
print("numStates " + str(S))
print("numActions 4")
print("start " + str(s))
print("end " + str(e))

I = [-1, 0, 0, 1]
J = [0, -1, 1, 0]
for i in range(n):
	for j in range(n):
		state = states[i][j]
		if(state >= 0 and state != e):
			validActions = []
			for a in range(4):
				if(i+I[a] >= 0 and i+I[a] < n and j+J[a] >= 0 and j+J[a] < n):
					if(grid[i+I[a]][j+J[a]] != 1):
						validActions.append(a)
			if(p == 1):
				for a in validActions:
					print("transition " + str(state) + " " + str(a) + " " + str(states[i+I[a]][j+J[a]]) + " -1 1")
			elif(p > 0 and p < 1):
				numValidActions = len(validActions)
				for a in validActions:
					print("transition " + str(state) + " " + str(a) + " " + str(states[i+I[a]][j+J[a]]) + " -1 " + str(p + (1-p)/numValidActions))
					for b in validActions:
						if(b != a):
							print("transition " + str(state) + " " + str(a) + " " + str(states[i+I[b]][j+J[b]]) + " -1 " + str((1-p)/numValidActions))
			elif(p == 0):
				numValidActions = len(validActions)
				for a in validActions:
					for b in validActions:
						print("transition " + str(state) + " " + str(a) + " " + str(states[i+I[b]][j+J[b]]) + " -1 " + str(1.0/numValidActions))

print("discount 1")
