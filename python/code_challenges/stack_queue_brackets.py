from data_structures.queue import Queue


def multi_bracket_validation(string):
	opening = "([{"
	closing = ")]}"
	matching = {")": "(", "]": "[", "}": "{"}
	stack = []
	for char in string: 
		if char in opening:
			stack.append(char)
		elif char in closing: 
			if len(stack) == 0:
				return False
			if stack[-1] == matching[char]:
				stack.pop()
			else:
				return False
	return len(stack) == 0
