from collections import Counter
def wordCount(name):
	with open(name, 'r') as f:
		return Counter(f.read().split())

print("Number of words :",wordCount('word.txt'))

