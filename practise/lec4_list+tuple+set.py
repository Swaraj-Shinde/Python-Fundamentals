#Lecture 4: List,Tuple,Dictionary 

#topic 1: lists
courses=['a','b','c','d','e'] #defined using []
print(courses)
print(courses[3]) #to access the elements
print(courses[-1]) #negative indexing,used to access last element
print(courses[:2]) #to access set of elements
print(courses[3:])

#topic 2: add elements in a list
courses.append('f') #adds elements at the last
courses.insert(3,'1') #add element at desires index 
print(courses)

list1=[1,2,3,4]
list2=[5,6,7,8]
list1.append(list2) #these will add list 2 as a single unit
list1.insert(-1,list2)
print(list1)

list3=[0,10]
list1.extend(list3) #it will take individual element of list 3 and add in list 1
print(list1)

#topic 3: remove an element
num=[1,2,3,4,5,6]
num.remove(2)
print(num)
num.pop() #to remove last element, it returns last element
popped_element=num.pop()
print(popped_element)

#topic 4: reverse a list
lista=['a','c','b']
list_b=[1,5,3]
lista.reverse()
print(lista)

#topic 5: sorting a list
lista.sort()
list_b.sort()
print(lista) #alphabetical order for characters
print(list_b) #increasing order for numbers

lista.sort(reverse=True)
list_b.sort(reverse=True)
print(lista) 
print(list_b)

sorted_list=sorted(list_b) #it will keep original list as it
print(sorted_list)

#topic 6:to find index of an element
list3=['a','e','i','o','u']
print(list3.index('e'))

#topic 7: to find whether an element is present in a list
print('a' in list3)
print('b' in list3)

#topic 8: to print all the elements in the list
for any_name in list3:
    print(any_name)

#to print index as well
for index,any_name in enumerate(list3):
    print(index,any_name)

for index,any_name in enumerate(list3,start=1): #it will start index from 1
     print(index,any_name)

#topic 9: to convert list into string using join
string=' '.join(list3) #space between the elements, can add any element
print(string)

#topic 10: to convert string into list using split
string='a e i o u'
new_list=string.split(' ')
print(new_list)

#topic 11: tuples (immutable,cannot change elements)
list_1=[1,2,3,4,5]
list_2=list_1
print(list_1)
print(list_2)
list_1[0]=0
print(list_1) #change made in list 1 but both list got updates
print(list_2)

#tuple used for data which doesnt need to change once entered
tuple_1=(1,2,3,4,5)#now changing data will give error

#topic 12: set(unordered,no duplicates)
set1={1,2,3,4,5,6}
print(set)

set2={2,4,6}

print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))
print(set2.difference(set1)) 

#topic 13: creating empty set,tuple,list
empty_list=[]
empty_list=list()

empty_tuple=()
empty_tuple=tuple()

empty_set={} #wrong method, it rather creates a dictionary
empty_set=set() #correct method
