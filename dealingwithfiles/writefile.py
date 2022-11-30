""" open file with write mode --> if
the file doesn't exist ? python will try to open for  it:
if exists ---> (remove old content)--> start writing
from the beginning of the file
"""
try:
    fileobj=open("names.txt", "w")
except Exception as e:
    print(e)
else:
    print(fileobj)

    # fileobj.write("Ahmed\n, Ali\n")
    #
    # fileobj.write("iti\n")
    # fileobj.write("#####################\n")
    # fileobj.seek(10)
    # fileobj.write("----------------------")
    ################## writelines
    fileobj.writelines(["line1","line2", 'iti', "test"])