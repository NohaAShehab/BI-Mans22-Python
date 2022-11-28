# name = "Ahmed"
# # name[3] = "d"
#
# name = name.replace("e", "E")
"""
    list ---> basic data structure in python
    --> mutable datastructure
"""
"1- to define a list"
l = []
myl = list([])

"2- list can hold different elements from differnet datatypes even if another list "
information = ["Ahmed", True, ['sql', 'python', 'bi'],2022,2022, 22.5, 2022]
"3- get no of elements in the list "
print(len(information))

"4- access elements in the list using the index "
print(information[1])
print(information[2][1])
"5- lists are mutable ---> you can change elements"
information[1] = 'iti'

"6- you can append an element to the list --> at the end of the list "
information.append("new element added")

# information[10] ='lalalalaaa'  # not allowed

"7- insert element at certain position"
information.insert(2, "Nohaaaaaaaaaaaaa")
information.insert(20, "Nohaaaaaaaaaaaaa")  # if position doesn't exist ===> will add it at the end

"8- remove element from the list "
popped_item = information.pop()  # pop remove the last element in the list
### and returns with it.
print(popped_item)
print(information)

"9- pop element at certain index "
popped_element = information.pop(2)
print(popped_element, information)

"10-remove element "
information.remove(2022)
print(information)

"11- get the index of certain element "
print(information.index("Ahmed"))

"12- list concatentation"
courses1 = ["python", "Bi", 'sql']
courses2= ["communication skills","Big data", 'statistics']
bi = courses1 + courses2
print(bi)

"13- extend a list "
courses1 = ["python", "Bi", 'sql']
courses2= ["communication skills","Big data", 'statistics']

courses1.extend(courses2)
print(courses1)

"14- sort list --- -> list must be from the same type "
names = ["Awatef", 'Hadeer','Meran', 'Eman',
         'Mina','Shrouq', 'Asmaa', 'Aml', 'Esraa', 'Yasmin',
         'Mohamed', "Mohamed Gad", 'Dief', 'Mohamed Attya', 'Mahmoud']
names.sort()  # sort data ascending in the same object
print(names)

names.sort(reverse=True)
print(names)
"15- reverse a list "
l = ['Ahmed', 'Ali', True, False, ['python', 'bi']]
l.reverse()
print(l)

l[0].reverse()
print(l)
"16- loop over the list "
for item in l:
    print(f"item = {item}")

"17- split string to a list "
myinfo= "noha:iti:30:Engineeering"
myinfo = myinfo.split(":")
print(myinfo)

message='Nice to meet you.'
message = message.split("e")
print(message)


"18-cast string to a list"
name = 'noha'
name = list(name)
print(name)

"membership"
names = ["Awatef", 'Hadeer','Meran', 'Eman',
         'Mina','Shrouq', 'Asmaa', 'Aml', 'Esraa', 'Yasmin',
         'Mohamed', "Mohamed Gad", 'Dief', 'Mohamed Attya', 'Mahmoud']
print('Awatef' in names)

"min , max ---> must be from the same type "
print(min(names))
print(max(names))

"empty list is considered to be a falsy value"

l = []
if l:
    print("hi")
else:
    print("bye")