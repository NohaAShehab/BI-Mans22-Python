def validatechar(message):
    while True:
        mystr = input(message)
        if mystr.isalpha():
            return mystr