#ID :201451075
#Breadth First Search 8-puzzle solver...
#I have used technique similar to BFS, except for I haven't used tree

def find_index_0(num):			#to find the position of 0 on board
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

def make_move(num):		#num - 9 bit number
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
		moved_list.append([int(final),num])
		
		final = swap(operate, ind, 3)
		moved_list.append([int(final),num])
		
	elif ind==1:
		final = swap(operate, ind, 0)		#0 can go to 0, 2 or 4
		final = final[1:]
		moved_list.append([int(final),num])
		
		final = swap(operate, ind, 2)
		moved_list.append([int(final),num])
		
		final = swap(operate, ind, 4)
		moved_list.append([int(final),num])
	
	elif ind==2:
		final = swap(operate, ind, 1)			#0 can go to 1 or 5
		moved_list.append([int(final),num])
		
		final = swap(operate, ind, 5)
		moved_list.append([int(final),num])
		
	elif ind==3:
		final = swap(operate, ind, 0)			#0 can go to 0, 4, or 6
		final = final[1:]
		moved_list.append([int(final),num])
		
		final = swap(operate, ind, 4)
		moved_list.append([int(final),num])
		
		final = swap(operate, ind, 6)
		moved_list.append([int(final),num])
		
	elif ind==4:
		final = swap(operate, ind, 1)			#0 can go to 1, 3, 5 or 7
		moved_list.append([int(final),num])
		
		final = swap(operate, ind, 3)
		moved_list.append([int(final),num])
		
		final = swap(operate, ind, 5)
		moved_list.append([int(final),num])
		
		final = swap(operate, ind, 7)
		moved_list.append([int(final),num])
	
	elif ind==5:
		final = swap(operate, ind, 2)			#0 can go to 2, 4, 8
		moved_list.append([int(final),num])
		
		final = swap(operate, ind, 4)
		moved_list.append([int(final),num])
		
		final = swap(operate, ind, 8)
		moved_list.append([int(final),num])
	
	elif ind==6:
		final = swap(operate, ind, 3)			#0 can go to 3 or 7
		moved_list.append([int(final),num])
		
		final = swap(operate, ind, 7)
		moved_list.append([int(final),num])
		
	
	elif ind==7:
		final = swap(operate, ind, 4)				#0 can go to 4, 6, 8
		moved_list.append([int(final),num])
		
		final = swap(operate, ind, 6)
		moved_list.append([int(final),num])
		
		final = swap(operate, ind, 8)
		moved_list.append([int(final),num])
		
	
	elif ind==8:
		final = swap(operate, ind, 5)			#0 can go to 5 or 7
		moved_list.append([int(final),num])
		
		final = swap(operate, ind, 7)
		moved_list.append([int(final),num])

	return moved_list


print("\nEnter a 9 digit number showing the orientation of the game (row wise)")
number = int(input())

Q = []								#Queue for BFS
Q.append([number,111111111])		#Queue contains (node, last node of level)

moves = 0							#number of moves
nodes = 0							#number of nodes traversed
last = number

while Q:
	x = Q.pop(0)					#Dequeue
	
	nodes+=1
	
	if x[0]==last:
		moves+=1
	
	listing = make_move(x[0])		#generate child of the node
	
	for i in listing:				#remove previous move
		if i[0]==x[1]:
			listing.remove(i)
			break
	
	if listing[len(listing)-1][1]==last:			#update last element of the level
		last = 	listing[len(listing)-1][0]	
	
	for i in listing:
		if i[0] == 123456780:						#check for solution
			print("Number of moves - " + str(moves+1))
			print("Number of nodes - " + str(nodes))
			print("Solution Found!")
			exit(0)
		Q.append(i)									#Enqueue