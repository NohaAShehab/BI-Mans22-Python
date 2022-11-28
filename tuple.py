
"""
    tuple ---> basic data structure in python
    --> immutable datastructure
"""
"1- to define a tuple"
t = ()
myt = tuple([])
#
"2- tuple can hold different elements from differnet datatypes even if another list "
information = ("Ahmed", True, ['sql', 'python', 'bi'],2022,2022, 22.5, 2022)
"3- get no of elements in the tuple "
print(len(information))
#
"4- access elements in the tuple using the index "
print(information[1])
print(information[2][1])


"11- get the index of certain element "
print(information.index("Ahmed"))
#
"12- tuple concatentation"
courses1 = ("python", "Bi", 'sql')
courses2= ("communication skills","Big data", 'statistics')
bi = courses1 + courses2
print(bi)
#

"16- loop over the tuple "
t = ("mm", 'nn', True, "iti")
for item in t:
    print(f"item = {item}")


"18-cast string to a tuple"
name = 'noha'
name = tuple(name)
print(name)

"membership"
names = ("Awatef", 'Hadeer','Meran', 'Eman',
         'Mina','Shrouq', 'Asmaa', 'Aml', 'Esraa', 'Yasmin',
         'Mohamed', "Mohamed Gad", 'Dief', 'Mohamed Attya', 'Mahmoud')
print('Mina' in names)
#
"min , max ---> must be from the same type "
print(min(names))
print(max(names))
#
"empty tuple is considered to be a falsy value"

t = ()
if t:
    print("hi")
else:
    print("bye")

"tuple of one element"
myt = ('iti',)
"cast tuple to a list and vise versa "
myt = list(myt)
myt.append("bla bla bla")
print(myt)
myt =tuple(myt)
print(myt)