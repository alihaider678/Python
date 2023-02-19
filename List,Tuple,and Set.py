#Lists

courses = ['History', 'Math', 'Physics', 'Computer']

#Print entire list
print(courses)
#Find Length
print(len(courses))

#print specific index 
print(courses[2])
print(courses[0])

#print last item with negative 1
print(courses[-1])

print(courses[0:2])
print(courses[2:])

#Modifying Lists Method
# 1) Appened(end of the list)

courses.append('Calculus')
print(courses)

# 2) Insert(2 arguments: first;location second; value)

courses.insert(0,'ICT')
print(courses)

# 3) Extend(add another list into first list)

courses = ['History', 'Math', 'Physics', 'Computer']
courses2 = ['DLD', 'Database']
courses.extend(courses2)
print(courses)

# 4) Remove(remove method remove specific value)

courses.remove('History')
print(courses)

# 5) Pop(this method automatically remove last item)

courses.pop()
print(courses)

#Sorting Lists
courses.sort()
print(courses)
#sorting in reverse orde
courses.sort(reverse=True)
print(courses)

nums = [1,4,5,2,3]
print(nums)
#sort the number in ascendng order
nums.sort()
print(nums)

print(max(nums))
print(min(nums))
print(sum(nums))

#Finding values
print(courses)

print('Math' in courses)
print('EMO' in courses)

#Looping Values
for item in courses:
	print(item)

# Print list through loop with its indexes
for index, course in enumerate(courses):
	print(index, course)
# Print list through loop with its indexes(start index from 1)
for index, course in enumerate(courses, start = 1):
	print(index, course)

#Spliting Values

students = ['Ali', 'Zeeshan', 'Husne', 'Usman']

students_str = ' , '.join(students)
print(students_str)

#Now we want to again original list
new_list = students_str.split(' , ')
print(new_list)


# Lists are Mutable while as Tuple are immutable

#Tuples

tuple_1 = ('History', 'Math', 'physics', 'Biology')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#tuple_1[0] = 'Art' #Error occured in this line because tuple does not changeable

print(tuple_1)


#Sets

# sets are written in curly braces
# Every time run set chnage order
# Does not contain duplicate values/items

cs_courses = {'Programming Fundamental', 'OOP', 'DSA', 'DB', 'OOP'}

print(cs_courses)

cs_courses = {'Programming Fundamental', 'OOP', 'DSA', 'DB', 'OOP'}
cs_courses_1 = {'Programming Fundamental', 'OOP', 'DSA', 'DB', 'DAA', 'AI', 'ML'}

#check which courses are common in both sets
print(cs_courses.intersection(cs_courses_1))

#check which courses are not in other list
print(cs_courses.difference(cs_courses_1))


#print all courses both sets
print(cs_courses.union(cs_courses_1))



# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()
