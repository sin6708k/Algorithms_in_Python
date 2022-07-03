import matplotlib.pyplot as plt

fin = open('p2_output.txt', 'r')
n = int(fin.readline())

red = []
blue = []
for i in range(n):
	temp = []
	line = fin.readline()
	temp.append(int(line.split(',')[0].split()[0]))
	temp.append(int(line.split(',')[0].split()[1]))
	red.append(temp)
	temp = []
	temp.append(int(line.split(',')[1].split()[0]))
	temp.append(int(line.split(',')[1].split()[1]))
	blue.append(temp)

for i in range(len(red)):
	plt.plot(red[i][0], red[i][1], 'ro')
	plt.plot(blue[i][0], blue[i][1], 'bo')

for i in range(len(red)):
	plt.plot( [red[i][0], blue[i][0]], [red[i][1], blue[i][1]], 'k-')

plt.show()