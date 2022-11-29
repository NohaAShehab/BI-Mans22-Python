
#
# def askfornums(no_of_times):
#     nums = []
#     for i in range(no_of_times):
#         while True:
#             num = input("please enter number : ")
#             if num.isdigit():
#                 nums.append(num)
#                 break
#     return nums
#
# nums=askfornums(3)
# print(nums)
# """ this a message """



"""
    variable scoping
    global scope: any variable defined in the python script is considered
    to have global scope ---> You can read or modify it inside a function
    localscope : any variable defined inside a function
    can be accessed only in the function
"""
#
# name = input("please enter your name : ")
#
# def printinputname():
#     print(name)
#
#
# printinputname()

################################################
# "2- modify the global variable from inside a function"
# course = 'python'
# def changeCourse():
#     course = 'BI'  # new local variable from the changecourse fun
#     print(f"inside the function {course}")
#
# changeCourse()
# print(course)

##############################################

# def test():
#     print("test")
#
# def test(message):
#     print(message)
#
# test("hi")
#
# # test= 'iti'
# test("bye")


# def sumnums(num1, num2):  # num1 , num2 are arguments
#     res = num1 + num2
#     print(res)
#     return res
#
# res=sumnums(4,5)
# print(res)
# name = 'Mostafa'
# def sumnums():
#     num1 = input("please enter num1: ")
#     num2 = input("please enter num2 : ")
#     res = num1+ num2
#     return res
# r=sumnums()
# print(r)
"""modify the global variable from inside the function """
# course = 'python'
# def changecourse():
#     global course
#     course = 'BI'
#
#
# changecourse()
# print(f"this after the function {course}")
# ############################################################
# def outerfunction():
#     course = 'python'  # local variabel can be accessed anywhere in the function
#     # or the inner functions
#     def changecourse():
#         print(f" from the changecourse function {course}")
#     changecourse()
#
# outerfunction()

# def outerfunction():
#     course = 'python'  # local variabel can be accessed anywhere in the function
#     # or the inner functions
#     def changecourse():
#         course = "BI"  # new local variable for the changecourse
#         ## can be accessed only inside this function
#         print(f" from the changecourse function {course}")
#     changecourse()
#     print(f" after calling the function {course}")
#
# outerfunction()
# print("====bye====")
###############################################33

def outerfunction():
    course = 'python'  # local variabel can be accessed anywhere in the function
    # or the inner functions
    def changecourse():
        nonlocal course
        course = "BI"  # new local variable for the changecourse
        ## can be accessed only inside this function
        print(f" from the changecourse function {course}")
    changecourse()
    print(f" after calling the function {course}")

outerfunction()
print("====bye====")





















