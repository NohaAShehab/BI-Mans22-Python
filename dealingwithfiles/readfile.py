
try:
    fileobj=open("mycv.txt", "r")
except FileNotFoundError as fe:
    print(fe)
else:
    # print(fileobj)
    # data = fileobj.read()  # read all the content in a string
    # print(data)
    ###
    "read from the 10byte "
    # fileobj.seek(10)
    # data = fileobj.read()
    # print(data)
    "read the file line by line "
    # lines = fileobj.readlines()  # read file content into a list
    # print(lines)

    for l in fileobj:
        print(f"l = {l}")

    fileobj.close()