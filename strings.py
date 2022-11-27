
# message ='I love ITI'
#
# print(message[3])
# print(message[3:8])
#
# "1- get the len  of  the string "
# print(len(message))
#
# "2- get no of occurance of certain char in the string"
# print(message.count("I"))
#
# "3- string concatenation "
# fname = "Noha"
# midname = 'Abdelhady'
# lname = 'Shehab'
# # fullname = fname + midname + midname +lname
# # print(fullname)
#
# "4- string interpolation"
# fullname = fname + midname *2  +lname
# print(fullname)
#
# "5- format string "
# # no_courses = 30
# # track = 'bi'
# # track_info = "track {0} contains {1}  courses "
# # print(track_info.format(track, no_courses))
# # print(track_info.format( no_courses, track))
#
# no_courses = 30
# track = 'bi'
# track_info = "track {trackname} contains {coursesnumber}  courses "
# print(track_info.format(trackname=track, coursesnumber=no_courses))
# print(track_info.format(coursesnumber=no_courses, trackname=track))
# "ask user to enter input "
# username = input("please enter name: ")
#
# userage = input("please enter age")  # always returns with string
#
# "f-format string "
# mymessage =f"welcome user {username} , with age  {userage}"
# print(mymessage)


"string replacment "

message = 'I love python '
print(message.replace("o", "0"))

"string capitalize"
message= 'i love iti'
print(message.capitalize())

"string upper "
print(message.upper())  # lower

"check if the string char are upper or lower"
print(message.isupper())


"check if the value in the string is digit or numeric "
num =  "10"
print(num.isdigit())

"check if the value in the string consists off alphas"
name = 'Hadeer'
print(name.isalpha())

"check if the string consists of spaces "
message = '                                                       '
print(message.isspace())

"strip spaces"
# name = input("please enter your name: ")
# password = input("please enter your password ")
#
# name = name.strip()  # remove the spaces from the begining or the end of the string
#
# print(f"name={name},password={password}")


# name = input("please enter your name: ")
# password = input("please enter your password ")
#
# # name = name.lstrip()  # remove the spaces from the beginning(left) of the string
# #
# # print(f"name={name},password={password}")
#
# name = name.rstrip()  # remove the spaces from the end(right) of the string
#
# print(f"name={name},password={password}")


#########################################3
name = '$   noha shehab # '
name = name.strip("# ")

print(f"name={name}.")
print(name.replace(" ", ""))

#################################
# message = 'I love python'
# print(message.index("p"))
#
# "loops in python while loop , for in loop "
#
# ################################
#
# for c in 'my name is noha':
#     print(c)
#
#
#
# while True:
#     name= input("please enter your name: ")
#     if name.isalpha():
#         break

num = 5 +0j
mynum = 0+1j
complexnum = complex(9,10)
print(complexnum)

a, b, c, d = 10, 66.66, 76.3, 100.54