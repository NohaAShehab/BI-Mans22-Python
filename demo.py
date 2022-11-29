"""
    number :3
    [
    [1],       ------> 1
    [2,4],  --------> 2*1 , 2*2
    [3,6,9] ---> 3*1 , 3*2, 3*3
    ]

    multiply num * [1---> num]

"""


num = input("please enter number : ")
if num.isdigit():
    num = int(num)
    multiplication_table = []
    for i  in range(1, num+1):
        items = []
        for j in range(1, i+1):
            res = i*j
            # print(res)
            items.append(res)

        # print(f"----------{items}---------------")
        multiplication_table.append(items)
    else:
        print(multiplication_table)