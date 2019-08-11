import numpy as np
from os import sys

f = open(sys.argv[1], "r")
S = int(f.readline().split()[1])
A = int(f.readline().split()[1])
f.readline()
l = f.readline().split()
nonend = list(np.arange(S))
if (int(l[1]) != -1):
	for e in l[1:]:
		nonend.remove(int(e))
T = [dict() for _ in range(S)]
while(1):
	l = f.readline().split()
	if (l[0] == 'discount'):
		gamma = float(l[1])
		break
	s1 = int(l[1])
	a = int(l[2])
	s2 = int(l[3])
	r = float(l[4])
	p = float(l[5])
	if(a in T[s1]):
		T[s1][a].append((s2, r, p))
	else:
		T[s1][a] = [(s2, r, p)]
f.close()

V0 = np.zeros(S)
V1 = np.zeros(S)
t = 0
while(1):
	t += 1
	for s1 in nonend:
		L = list(T[s1].keys())
		V1[s1] = max([sum([x[2] * (x[1] + gamma * V0[x[0]]) for x in T[s1][a]]) for a in L])
	if(np.linalg.norm(V1 - V0, np.inf) <= 1e-16):
		break
	V0 = list(V1)

Pi = [-1 for _ in range(S)]
for s1 in nonend:
	L = list(T[s1].keys())
	Pi[s1] = L[np.argmax(np.array([sum([x[2] * (x[1] + gamma * V1[x[0]]) for x in T[s1][a]]) for a in L]))]

for s in range(S):
	V1[s] = round(V1[s], 11)
	print(str(V1[s]) + " " + str(Pi[s]))
print("iterations " + str(t))
