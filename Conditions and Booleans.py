
# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=


# Object Identity:  is
a = [1,2,3]
b = [1,2,3]
print(a is b)

language = 'Python'

if language == 'Python':
    print('Language is Python')
elif language == 'java':
    print('Language is java')
else:
    print('No match')


# and
# or
# not

#AND Operator
user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')


#NOT Operator
user = 'Admin'
logged_in = True
if not logged_in:
    print('please log in')
else:
    print('Welcome')





# False Values:
    # False
condition = False
if condition:
   print('Evaluated to True')
else:
   print('Evaluated to False')

    # None
condition = None
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
    # Zero of any numeric type
condition = 0
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
condition = 10
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

