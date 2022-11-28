"""
    dict ---> comma ---> key:value pair datatype
    from python 3.7 ---> dictionary is ordered in the memory
"""
info = ["noha", "iti", "engineering", 30]
"1- define empty dict "
info = {}
myinfo = dict([])

"2- dict can hold data from different datatypes "

myinfo = {
    "name":"noha",
    "spec": "Engineering",
    "age":30,
    "courses": ["python", "PHP", "Databases"],
    "name": "Noha Shehab"
}
"3- access elements of the dict using the key"
print(myinfo["name"])
"4- update elements values"
myinfo["spec"] = "Computer Engineering"
"5- if the key is not in the dict ---> will add it "
myinfo["city"] = 'Mansoura'
print(myinfo)

"6- pop element from the dict "
popped= myinfo.pop("spec")
print(popped)

"7- get the keys of the dict"
keys=myinfo.keys()
print(keys)
keys = list(keys)

"7- get the keys of the values"
values=myinfo.values()
print(values)
values = list(values)
print(values)

myinfo[10] = "iti"  # key
"8- get the dict items "
items = myinfo.items()
print(items)
items = list(items)
print(items)


myd = dict([('name','Ahmed'), ('track', 'bi')])
print(myd)


keys = ["name", "email"]
values = ["shorouq", "shrouq@gmail.com"]
d = {}
counter = 0
for k in keys:
    d[k] = values[counter]
    counter +=1
print(d)


bi = {
    "courses": ["sql", "python", "bi"]
}

for item in bi["courses"]:
    print(item)


"9- loop over dictionary items"
yasmin_info = {
    "name":"Yasmin",
    "email": "yasmin@gmail.com",
    "track": 'bi',
    "courses": ('python', 'sql')
}
# for info in yasmin_info:
#     print(info)



# for info in yasmin_info:
#     print(f"key={info}, value = {yasmin_info[info]}")


for k, v in yasmin_info.items():
    print(f"{k}:{v}")
"in operator "

# if "yasmin" in yasmin_info:
#     print("hi")
# else:
#     print("bye")

if "Yasmin" in yasmin_info.values():
    print("hi")
else:
    print("bye")

"dict update "
info_part01 = {"name":"Ahmed", "track":"bi"}
info_part02 = {"city":"cairo", "age":25, "name":"Ali"}

info_part01.update(info_part02)
print(info_part01)


#########################
info_part01.clear()



