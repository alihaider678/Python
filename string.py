#Print String
message = 'Hello Ali'
print(message)


#Find Length of message
message = 'Hello Ali'
print(len(message))

#Print Specific message from string
message = 'Hello Ali'
print(message[6])
print(message[0:5])
print(message[6:])


#Print in different cases
message = 'Hello Ali'
print(message.lower())
print(message.upper())

print(message.count('Hello Ali'))

#Find specific word at what place?
print(message.find('Ali'))

#Replace String text
message = 'Hello World'
message = message.replace('World', 'Universe')
print(message)

#Concatenate String
greeting = 'Hello'
name = 'Ali'
message = greeting + ', ' + name + '. Welcome!'
print(message)
#This Concatenate methos which we describe upper, Not Suitable.

#Another Method
greeting = 'Hello'
name = 'Ali'
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

#Another Method, In which we directly passing the variables
greeting = 'HELLO'
name = 'Ali'
message = f'{greeting}, {name.upper()}. WELCOME!'
print(message)





