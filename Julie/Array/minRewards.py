####### O(n^2) time | O(n) space #########
def minRewards(scores):
	rewards = [1 for _ in scores]
	for i in range(1, len(scores)):
		if scores[i] > scores[i-1]:
			rewards[i] = rewards[i-1] + 1
	for i in reversed((range(len(scores)-1))):
		if scores[i] > scores[i+1]:
			rewards[i] = max(rewards[i], rewards[i+1]+1) # use this max is important
	return sum(rewards)
		
#Ex: [8,4,2,1,3,6,7,9,5]
# first for loop, the reward will be [1,1,1,1,2,3,4,5,1]
# second for loop, back revisited the array, for the last two reward [5,1].
# based on the algorithm we need have [2,1] but then it confilict with the first for loop requirement
# So, we need to use MAX



######## O(n) time | O(n) space ##########
def minRewards(scores):
	rewards = [1 for _ in scores]
	localMinIdxs = getLocalMinIdxs(scores)
	for localMinIdx in localMinIdxs:
		expandFromLocalMinIdx(localMinIdx, scores, rewards)
	return sum(rewards)

def getLocalMinIdxs(array):
	if len(array) == 1:
		return [0]
	localMinIdxs = []
	for i in range(len(array)):
		if i == 0 and array[i] < array[i+1]:
			localMinIdxs.append(i)
		if i == len(array)-1 and array[i] <array[i-1]:
			localMinIdxs.append(i)
		if i==0 or i==len(array)-1:
			continue
		if array[i] < array[i+1] and array[i] < array[i-1]:
			localMinIdxs.append(i)
	return localMinIdxs

def expandFromLocalMinIdx(localMinIdx, scores, rewards):
	leftIdx = localMinIdx - 1 
	while leftIdx >= 0 and scores[leftIdx] > scores[leftIdx + 1]:
		rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx +1]+1)
		leftIdx -= 1
	rightIdx = localMinIdx + 1
	while rightIdx < len(scores) and scores[rightIdx] > scores[rightIdx-1]:
		rewards[rightIdx] = rewards[rightIdx-1]+1
		rightIdx += 1 
		
######## O(n) time | O(n) space ##########
def minRewards(scores):
	rewards = [1 for _ in scores]
	for i in range(1, len(scores)):
		if scores[i] > scores[i-1]:
			rewards[i] = rewards[i-1]+1
	for i in reversed((range(len(scores)-1))):
		if scores[i]>scores[i+1]:
			rewards[i] = max(rewards[i], rewards[i+1]+1)
	return sum(rewards)
