#Dictonary

student = {'name' : 'Ali', 'Age' : 23, 'courses' : ['Math', 'Database']}
print(student)

#Print specific value
print(student.get('name'))

#print value which is not exist in dict
print(student.get('phone', 'Not Found'))

#If dict already exist then we add new key like as below
student['phone'] = '0307-0614159'
print(student)

#Update Dict
student.update({'name' : 'Husne', 'Age' : 22, 'courses' : ['CS', 'DS']})
print(student)

#Delete Dict
del student['Age']
print(student)

#Now let we want to popup only name of that student
name = student.pop('name')
print(student)
print(name)

#Length of Dict?
print(len(student))
#Print only keys?
print(student.keys())
#Print only values?
print(student.values())

# with For loop display key

for key in student:
	print(key)

# with For loop display key and values

for key, value in student.items():
	print(key, value)