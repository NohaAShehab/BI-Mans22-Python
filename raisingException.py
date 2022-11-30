# def raiseIntException(numericstring):
#     if numericstring.isdigit():
#         return int(numericstring)
#     raise Exception ("Integer number required")
#
# def calculator():
#     num1= input("please enter num1 : ")
#     num1 = raiseIntException(num1)
#     num2 = input("please enter num2 : ")
#     num2 = raiseIntException(num2)
#
#     # num2 = input("please enter num2: ")
#     # if num2.isdigit():
#     #     num2 = int(num1)
#     # else:
#     #     raise Exception("num1, num2 should be integers ")
#     operation = input("please enter operation : ")
#
#
#     if operation in ["+", "-", "/", "*"]:
#         if operation=="+":
#             res = num1 + num2
#         elif operation=='-':
#             res  = num1 - num2
#         elif operation=='*':
#             res  = num1 *num2
#         elif operation=='/':
#             res  = num1 / num2
#
#         return res
#
#
# res=calculator()
# print(res)
###############################################3




def raiseIntException(numericstring):
    if numericstring.isdigit():
        return int(numericstring)
    raise Exception ("Integer number required")

def calculator():
    num1= input("please enter num1 : ")
    num1 = raiseIntException(num1)
    num2 = input("please enter num2 : ")
    num2 = raiseIntException(num2)
    operation = input("please enter operation : ")


    if operation in ["+", "-", "/", "*"]:
        if operation=="+":
            res = num1 + num2
        elif operation=='-':
            res  = num1 - num2
        elif operation=='*':
            res  = num1 *num2
        elif operation=='/':
            if num2==0:
                raise Exception("Division by zero not allowed ")
            res  = num1 / num2

        return res
    else:
        raise  Exception("Operation not allowed ")

res=calculator()
print(res)





