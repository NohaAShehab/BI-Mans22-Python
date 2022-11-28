"""
    define a function
"""
#
# def funname():
#     pass
#
# def helloword():
#     print("----Hello World----")
#
#
#
# x=helloword()
# print(x)
# def helloworld():
#     print("hello world")
#     return
# x = helloworld()

""" function accept arguments """
# def sumnum(x,y):
#     res = x  +y
#     print(res)
#
# sumnum(5,6)

"function that returun "
# def makefullname(fname,lname):
#     fullname = fname + lname
#     return fullname
#
# res = makefullname("noha", "shehab")
# print(res)

""" functions with default arguments """
def sumnum(num1=0, num2=0):
    print(f"num1={num1}, num2={num2}")
    res =  num1 + num2
    print(res)
    return res

x = sumnum(10)

m = sumnum()

# mm = sumnum(10,20)
mm = sumnum(num2=10, num1=20)