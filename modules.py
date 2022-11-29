"""
every python file is considered to be a module
You can import it 0
--->
"""
def sayhello(name):
    print(f"Hello {name}")

# sayhello("Ahmed")
# sayhello("Ali")

def askforNum(message):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
sayhello("Ahmed")
sayhello("Ali")
askforNum("please enter num1 ")

def sumnum(num1, num2):
    res = num1 + num2
    print(res)