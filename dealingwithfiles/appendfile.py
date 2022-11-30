"""
    when you try to open the file with mode
    append
    --> if the file not exists ---> will try to create it

    ---> if the file exists --> open the file for appending
    starting from the end of the file

"""
try:
    fileobj = open("coursecontent.txt", "a")
except Exception as e:
    print(e)
else:
    print(fileobj)
    fileobj.write("Syntax\n")
    fileobj.write("loops\n")
    fileobj.seek(10)
    fileobj.write("#######################\n")
