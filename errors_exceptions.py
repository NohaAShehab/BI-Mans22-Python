"""
    errors ---> syntax error ---> must be fixed
        ---> logical error
        ---> runtime error / Exception ===> unexpected
        error causes the application to stop


"""

# print("iti")
# def sumnum(num1, num2):
#     res = num1 * num2
#     print(res)
#
# sumnum(2,2)
# sumnum(2,3)
# print("---------------- hi-------------------")
# num = input("please enter num1 ") #string
# num = int(num)
# print("------------- bye ----------------------")
################################3 Exception handling
# num = input("please enter num: ")
# try:
#     num= int(num)
# except:
#     print("problem happened while casting the num : ")
#
#
# print("---------------------- bye-------------------")
# message = 'hello'
# message2 ='iti'
# num = num+10


############################
# num = input("please enter num: ")
# try:
#     num= int(num)
# except:
#     print("problem happened while casting the num : ")
#     exit()
#
#
# print("---------------------- bye-------------------")
# message = 'hello'
# message2 ='iti'
# num = num+10
############################################

# num = input("please enter num: ")
# try:
#     num= int(num)
# except:
#     print("problem happened while casting the num , so num will be zero ")
#     num = 0
#
#
# print("---------------------- bye-------------------")
# message = 'hello'
# message2 ='iti'
# num = num+10
#################################################
#
# num = input("please enter num: ")
# try:
#     num= int(num)
# except Exception as e:
#     print(f"{e}")
#     exit()
#
#
# print("---------------------- bye-------------------")
# message = 'hello'
# message2 ='iti'
# num = num+10
#
################################


# try:
#     res = 8/0
# except Exception as e:
#     print(f"{e}")
#     exit()

"Exception types "
## ZeroDivisionError, NameError, ValueError


###################################
# name= 'Ahmed'
# try:
#     print(name)
#     print(5/0)
#     x=int("iti")
#
# except NameError as n:
#     print(f"{n} ---> error happened ")
#     name = ''
# except ZeroDivisionError as ze:
#     print(f"{ze} ====> error happended")
#     exit()
# except ValueError as ve:
#     print(f"{ve}")
#     num = 10
# except Exception as e:
#     print(f"{e}")
#     exit()








num = input("please enter num1 :  ")
try:
    num= int(num)
    num += 11
except Exception as e:
    print(e)
else:
    "this line will be executed only if there is no problem "
    pass
finally:
    "this block will be executed always"
    print("-----------Nice to meet you-----------")


















