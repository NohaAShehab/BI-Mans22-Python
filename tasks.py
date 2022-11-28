# no_of_levels = input("please enter number: ")
# print(no_of_levels)
# if no_of_levels.isdigit():
#     no_of_levels = int(no_of_levels)
#     count = 1
#     while count <= no_of_levels:
#         spaces_count = no_of_levels-count
#         astiric_count = count
#         str_print= " "*spaces_count + "*"*astiric_count
#         print(str_print)
#         count +=1
#
#
# else:
#     print("---- You provide number only ")

############################################
mystring = input("please enter message ")
str_len = len(mystring)
position = 0
for char in mystring:
    if char=='i':
        print(f"Char i found at position {position}.")
    position +=1







