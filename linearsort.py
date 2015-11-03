def arr():
	import random
	i = 0
	arr = []
	while i < 101:
		rand = random.randint(0,10000)
		arr.append(rand)
		i+=1
	return arr
def linear(arr):
	for i in range(1, len(arr)):
		current = arr[i]
		position = i 
		while position >0 and arr[position-1]> current:
			arr[position]=arr[position-1]
			position = position-1
			arr[position]=current

arr = arr()



linear(arr)

print arr