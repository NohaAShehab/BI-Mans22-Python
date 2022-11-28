"""
    sets
    unordered datatype in python ,
    that doesn't allow element duplication
    no indices
"""
"1- to define a set "
s = {"Ahmed", "Mohamed", "Mohamed", True, 'iti', 2022}
print(s)
"2- get len of the set "
print(len(s))
"3- empty set "
mys = set([])
"4- add element to the set"
s.add("item addedddddddd ")

"5- pop element from the set : random removing element from the set "
popped_item = s.pop()
print(s)
print(popped_item)
print(s)

"6- remove element from the set"
if "iti" in s:
    s.remove("iti")
    print(s)

"7- update set "
s1= {"python", "sql"}
s2 = {"python", "iti", "bi", 'Big data'}

s1.update(s2)
print(s1)

