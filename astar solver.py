#ID :201451075
#A* Search 8-puzzle solver (Hamming Priority Function)...
#I have used technique similar to A*, except for I haven't used tree

def find_index_0(num):			#to find the position of 0
	if len(str(num))==8:
		return 0
	for i in range(9):
		x = num % 10
		num = int(num/10)
		if x==0:
			break
	return 8-i
	
def swap(strr, a, b):			#to swap for 2 positions
	t = list(strr)
	temp = t[a]
	t[a] = t[b]
	t[b] = temp
	
	return ''.join(t)

def make_move(num, d):		#num - 9 bit number
	ind = find_index_0(num)
	
	#print(ind)
	#exit()
	
	operate = str(num)
	
	moved_list = []
	
	if len(operate)==8:
		operate = '0' + operate
		#add 0 to first position
	
	if ind==0:
		final = swap(operate, ind, 1)			#0 can go to 1 or 3
		moved_list.append([int(final),num, d, 0])
		
		final = swap(operate, ind, 3)
		moved_list.append([int(final),num, d, 0])
		
	elif ind==1:
		final = swap(operate, ind, 0)		#0 can go to 0, 2 or 4
		final = final[1:]
		moved_list.append([int(final),num, d, 0])
		
		final = swap(operate, ind, 2)
		moved_list.append([int(final),num, d, 0])
		
		final = swap(operate, ind, 4)
		moved_list.append([int(final),num, d, 0])
	
	elif ind==2:
		final = swap(operate, ind, 1)			#0 can go to 1 or 5
		moved_list.append([int(final),num, d, 0])
		
		final = swap(operate, ind, 5)
		moved_list.append([int(final),num, d, 0])
		
	elif ind==3:
		final = swap(operate, ind, 0)			#0 can go to 0, 4, or 6
		final = final[1:]
		moved_list.append([int(final),num, d, 0])
		
		final = swap(operate, ind, 4)
		moved_list.append([int(final),num, d, 0])
		
		final = swap(operate, ind, 6)
		moved_list.append([int(final),num, d, 0])
		
	elif ind==4:
		final = swap(operate, ind, 1)			#0 can go to 1, 3, 5 or 7
		moved_list.append([int(final),num, d, 0])
		
		final = swap(operate, ind, 3)
		moved_list.append([int(final),num, d, 0])
		
		final = swap(operate, ind, 5)
		moved_list.append([int(final),num, d, 0])
		
		final = swap(operate, ind, 7)
		moved_list.append([int(final),num, d, 0])
	
	elif ind==5:
		final = swap(operate, ind, 2)			#0 can go to 2, 4, 8
		moved_list.append([int(final),num, d, 0])
		
		final = swap(operate, ind, 4)
		moved_list.append([int(final),num, d, 0])
		
		final = swap(operate, ind, 8)
		moved_list.append([int(final),num, d, 0])
	
	elif ind==6:
		final = swap(operate, ind, 3)			#0 can go to 3 or 7
		moved_list.append([int(final),num, d, 0])
		
		final = swap(operate, ind, 7)
		moved_list.append([int(final),num, d, 0])
		
	
	elif ind==7:
		final = swap(operate, ind, 4)				#0 can go to 4, 6, 8
		moved_list.append([int(final),num, d, 0])
		
		final = swap(operate, ind, 6)
		moved_list.append([int(final),num, d, 0])
		
		final = swap(operate, ind, 8)
		moved_list.append([int(final),num, d, 0])
		
	
	elif ind==8:
		final = swap(operate, ind, 5)			#0 can go to 5 or 7
		moved_list.append([int(final),num, d, 0])
		
		final = swap(operate, ind, 7)
		moved_list.append([int(final),num, d, 0])

	return moved_list


print("\nEnter a 9 digit number showing the orientation of the game (row wise)")
number = int(input())

Q = []										#Priority Queue
Q.append([number,111111111, 0, 0])			#Queue contains (node, parent, depth, priority function value)

depth = 0
nodes = 0
parent = 111111111

while Q:
	max=0
	for i in range(len(Q)):					#finding index of max priority
		if Q[i]>Q[max]:
			max=i


	x = Q.pop(max)							#Dequeue				
	depth = x[2]
	nodes+=1

	if depth==15:							#Will check only upto 15 moves
		continue

	depth+=1
	
	listing = make_move(x[0], depth)		#generate child of the node state

	
	#Save a previous move and when the list is returned remove the previous element from it

	for i in listing:						#remove previous move
		if i[0]==x[1]:
			listing.remove(i)
			break

	for i in listing:						#setting priority of child nodes
		prior = 0
		y = i[0]
		if y%10==0:
			prior+=1
		y = y/10

		for j in range(8):
			if y%10==8-j:
				prior+=1
			y = y/10

		prior+=i[2]
		i[3]=prior

	
	for i in listing:
		if i[0] == 123456780:			#check for solution
			print("Number of moves - " + str(depth))
			print("Number of nodes - " + str(nodes))
			print("Solution Found!")
			exit(0)
		Q.append(i)						#Enqueue
	parent = x[0]						#Parent update