# """ import all module ---> access module
#     elements using the name
#
# """
# # import modules
# #
# # modules.sayhello("Noha")
# #
# #
# # modules.sumnum(10 , 20)
# """
#     import part of the module
# """
# # from modules import sumnum
# # sumnum(10 ,20)
#
#
#
# """ Alias the module name """
# # import  modules as mm
# #
# # mm.sumnum(20,30)
#
# #####################
# from modules import  sumnum as myfun
#
# myfun(20 ,30)
#
#
# from modules import  askforNum
#
# sal =askforNum("please enter salary")


""" import module from a package """
# import  bi.validationModule
#
# fname= bi.validationModule.validatechar("please enter name")
# print(fname)

# import  bi.validationModule as validate
#
# fname= validate.validatechar("please enter name")
# print(fname)

#################################
# from bi.validationModule import validatechar
# course = validatechar("please enter coursename")
# print(course)
#############3
# import iti.mathmodule
#
# iti.mathmodule.sumnums(10,30)

from iti import sumnums

from iti.mathmodule import sumnums
