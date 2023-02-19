# Intro

# nums = [1 , 2, 3, 4, 5]
# for num in nums:
# 	print(num)

#For Loop

nums = [1 , 2, 3, 4, 5]
for num in nums:
	if num == 3:
		print('Found!')
		break
print(num)

#Nested Loop
for num in nums:
	for letter in 'abc':
		print(num, letter)


for i in range(10):
	print(i)


for i in range(1 , 11):
	print(i)


# While Loop

x = 0

while x < 10:
	print(x)
	x += 1

# Another Example with condition
x = 0

while x < 10:
	if x == 5:
		break
	print(x)
	x += 1