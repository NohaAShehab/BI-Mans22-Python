#
# print()
print('Ahmed', "noha", "iti", "Bi", 2022)
#
# """
#     function accept variable number of parameters 0 or more
# """
#
# # def sumnums( *nums):
# #     print(nums)
# #     print(type(nums))
# #     summ = 0
# #     for num in nums:
# #         summ +=num
# #     print(f"sum={summ}")
# #
# #
# #
# # sumnums()
# # sumnums(10, 30, 40 ,50)
#
# def sumnums( *args):
#     print(args)
#     print(type(args))
#     summ = 0
#     for num in args:
#         summ +=num
#     print(f"sum={summ}")
# sumnums()
# sumnums(10, 30, 40 ,50)
############################################################
# def askforstudents(coursename, *students):
#     print(coursename, students)
#
# askforstudents("python", "Ahmed", "Mohamed", "Ali")
###############################################
# def askforstudents( *students,coursename='python'):
#     print(coursename, students)
#
# askforstudents("Ahmed", "Mohamed", "Ali", coursename='SQL' )

#################################
# def introduceYourself(**info):
#     print(info)


def introduceYourself(**kwargs):
    print(kwargs)

introduceYourself(name='noha',work='iti', food='kiwi', city='mansoura')
introduceYourself()
introduceYourself(fname='Ahmed', lanme='Mostafa')
introduceYourself(fullname='omarAhmed')


temp = "My name is {username}, I works at {work}"
print(temp.format(username='noha', work='iti'))








