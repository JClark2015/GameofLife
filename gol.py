import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def zeroorone():
	compare = np.random.rand()
	val = np.random.rand()
	if(val >= compare):
		return 1
	if(val < compare):
		return 0

def init():
	axes.set_xlim(0, w)
	axes.set_ylim(0, h)	
	axes.set_facecolor('y')
	plt.title('The Game of Life (periodic boundaries)')
	return ln,

def update(frame):
	global ca
	caf()
	xdata = [0 for x in range(w)]
	ydata = [0 for x in range(h)]
	for i in range(h):
		for j in range(w):
			if(ca[i][j] == 1):
				xdata.append(j)
				ydata.append(i)
	ln.set_data(xdata,ydata)
	return ln,

def caf():
	global ca
	
	ca_new = [[0 for x in range(w)] for y in range(h)]
	for step in range(h):
	
		for i in range(w):
			live_neighbors = 0

			#cell neighbors
			n_a = 0
			n_b = 0
			n_c = 0
			n_d = 0
			n_e = 0
			n_f = 0
			n_g = 0
			n_h = 0

			#define neighbors for each case of cell position
			#top left
			if((step == 0) and (i == 0)):
				n_a = ca[h-1][w-1]
				n_b = ca[step][w-1]
				n_c = ca[step+1][w-1]
				n_d = ca[step+1][i]
				n_e = ca[step+1][i+1]
				n_f = ca[step][i+1]
				n_g = ca[h-1][i+1]
				n_h = ca[h-1][i]

			#top right
			if((step == 0) and (i == w-1)):				
				n_a = ca[h-1][i-1]
				n_b = ca[step][i-1]
				n_c = ca[step+1][i-1]
				n_d = ca[step+1][i]
				n_e = ca[step+1][0]
				n_f = ca[step][0]
				n_g = ca[h-1][0]
				n_h = ca[h-1][w-1]
				
			
			#bottom left
			if((step == h-1) and (i == 0)):
				n_a = ca[step-1][w-1]
				n_b = ca[step][w-1]
				n_c = ca[0][w-1]
				n_d = ca[0][i]
				n_e = ca[0][i+1]
				n_f = ca[step][i+1]
				n_g = ca[step-1][i+1]
				n_h = ca[step-1][i]

			#bottom right
			if((step == h-1) and (i == w-1)):
				n_a = ca[step-1][i-1]
				n_b = ca[step][i-1]
				n_c = ca[0][i-1]
				n_d = ca[0][i]
				n_e = ca[0][0]
				n_f = ca[step][0]
				n_g = ca[step-1][0]
				n_h = ca[step-1][i]

			#top row
			if((step == 0) and (i > 0) and (i < w-1)):
				n_a = ca[h-1][i-1]
				n_b = ca[step][i-1]
				n_c = ca[step+1][i-1]
				n_d = ca[step+1][i]
				n_e = ca[step+1][i+1]
				n_f = ca[step][i+1]
				n_g = ca[h-1][i+1]
				n_h = ca[h-1][i]
			
			#left-most column
			if((step > 0) and (step < h-1) and (i == 0)):
				n_a = ca[step-1][w-1]
				n_b = ca[step][w-1]
				n_c = ca[step+1][w-1]
				n_d = ca[step+1][i]
				n_e = ca[step+1][i+1]
				n_f = ca[step][i+1]
				n_g = ca[step-1][i+1]
				n_h = ca[step-1][i]

			#bottom row
			if((step == h-1 ) and (i > 0) and (i < w-1)):
				n_a = ca[step-1][i-1]
				n_b = ca[step][i-1]
				n_c = ca[0][i-1]
				n_d = ca[0][i]
				n_e = ca[0][i+1]
				n_f = ca[step][i+1]
				n_g = ca[step-1][i+1]
				n_h = ca[step-1][i]

			#right-most row
			if((step > 0) and (step < h-1) and (i == w-1)):
				n_a = ca[step-1][i-1]
				n_b = ca[step][i-1]
				n_c = ca[step+1][i-1]
				n_d = ca[step+1][i]
				n_e = ca[step+1][0]
				n_f = ca[step][0]
				n_g = ca[step-1][0]
				n_h = ca[step-1][i]

			#normal case
			if((step > 0) and (step < h-1) and (i > 0) and (i < w-1)):
				n_a = ca[step-1][i-1]
				n_b = ca[step][i-1]
				n_c = ca[step+1][i-1]
				n_d = ca[step+1][i]
				n_e = ca[step+1][i+1]
				n_f = ca[step][i+1]
				n_g = ca[step-1][i+1]
				n_h = ca[step-1][i]


			#now check each cell's neighbors as they are defined above
			if(n_a == 1):
				live_neighbors+=1
			if(n_b == 1):
				live_neighbors+=1
			if(n_c == 1):
				live_neighbors+=1
			if(n_d == 1):
				live_neighbors+=1
			if(n_e == 1):
				live_neighbors+=1
			if(n_f == 1):
				live_neighbors+=1
			if(n_g == 1):
				live_neighbors+=1
			if(n_h == 1):
				live_neighbors+=1
			

			#Any live cell with fewer than two live neighbours dies, as if by underpopulation.
			if(live_neighbors < 2):
				ca_new[step][i] = 0
			#Any live cell with two or three live neighbours lives on to the next generation.
			if((ca[step][i] == 1) and ((live_neighbors == 2) or (live_neighbors == 3))):
				ca_new[step][i] = 1
			#Any live cell with more than three live neighbours dies, as if by overpopulation.
			if(live_neighbors > 3):
				ca_new[step][i] = 0
			#Any dead cell with exactly three live neighbours becomes a live cell, as if by 			reproduction.
			if((ca[step][i] == 0) and (live_neighbors == 3)):	
				ca_new[step][i] = 1					 	



		step += 1
		
	ca = ca_new 
	

if __name__ == '__main__':
	h = 100
	w = h
	ca = [[0 for x in range(w)]for y in range(h)]

	input = int(input("Enter 1 for random GoL, 2 for Glider example:"))
	
		
	if(input == 1):
		ca = [[zeroorone() for x in range(w)]for y in range(h)]
		print("hi")
	elif(input == 2):		
		ca[40][10] = 1
		ca[40][11] = 1
		ca[39][10] = 1
		ca[39][11] = 1

		ca[42][44] = 1
		ca[42][45] = 1
		ca[41][44] = 1
		ca[41][45] = 1

		ca[42][19] = 1
		ca[41][19] = 1
		ca[41][20] = 1
		ca[40][20] = 1
		ca[40][21] = 1
		ca[39][20] = 1
		ca[39][21] = 1
		ca[39][22] = 1
		ca[38][20] = 1
		ca[38][21] = 1
		ca[37][19] = 1
		ca[37][20] = 1
		ca[36][19] = 1
	
		ca[44][36] = 1
		ca[43][36] = 1
		ca[43][38] = 1
		ca[42][37] = 1
		ca[42][39] = 1
		ca[41][37] = 1
		ca[41][40] = 1
		ca[40][37] = 1
		ca[40][39] = 1
		ca[39][36] = 1
		ca[39][38] = 1
		ca[38][36] = 1
	
		ca[47][19+2] = 1
		ca[47][18+2] = 1
		ca[48][18+2] = 1
		ca[49][18+2] = 1
		ca[49][16+2] = 1
		ca[50][16+2] = 1
		ca[50][17+2] = 1
		print("hi2")



	xdata, ydata = [], []
	fig, axes = plt.subplots()
	
	ln, = plt.plot([], [], 'bs', markersize = 2)

	ani = FuncAnimation(fig, update, frames=1000, init_func=init, blit=True, repeat=False)
	plt.show()


		
		
	



