##Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic
## The elements in monotonic array, from left to right, are entirely non-increasing or entirely non-decreasing. (neighboor elements can be equal)

def isMonotonic(array):
	if len(array)<=2:
		return True
			
	direction = array[1]-array[0]
	for i in range(2, len(array)):
		if direction ==0:
			direction = array[i]-array[i-1]
			continue
		if breaksDirection(direction, array[i-1], array[i]):
			return False
	
	return True

def breaksDirection(direction, previousInt, currentInt):
	diff = currentInt - previousInt
	# a<b<c is true
	if direction>0: # if c-b>0 true then we need a-b<0 (which is the oppisite direction) so it's true
		return diff < 0 
	return diff >0 # Otherwise direction<0 we need diff>0 
		
			
