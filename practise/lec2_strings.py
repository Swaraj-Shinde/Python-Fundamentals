#Lecture 2 on strings
#its imp to save program before running it

#Topic 1: to find number of characters in a string
message='Hello World!'
print(len(message))

#Topic 2: to access individual or set of characters of a string
print(message[0])
print(message[:4])
print(message[6:])

#Topic 3: to make string lowercase or uppercase
print(message.lower())
print(message.upper())

#Topic 4: to count how many times a character or word has occured in the string
print(message.count('l'))
print(message.count(' '))
print(message.count('World'))
print(message.count('World!'))
print(message.count('a'))

#Topic 5: to find index of a character in a string
print(message.find('H'))
print(message.find('l')) #if a character gets repeated, it'll show only first index
print(message.find(' '))
print(message.find('Hello'))
print(message.find('ello'))

#Topic 6: to replace characetrs in a string
message=message.replace('World','Swaraj')
print(message)
message=message.replace('a','b')
print(message)
message=message.replace('b','aa')
print(message)
message=message.replace('l',' ')
print(message)
message=message.replace(' ','!')
print(message)

#Topic 7: to add two or more strings

#Method 1:
greeting='Hello'
name='Swaraj'
print(greeting+name)
#not a good practise

#Method 2:
message='{} {}'.format(greeting,name)
print(message)

#Method 3:
print(f'{greeting} {name} Shinde')
print(f'{greeting.lower()} {name} Shinde')

#Topic 8: to find what functions we can use with a variable
print(dir(message))
print(help(str.lower)) #to get help regarding specific function