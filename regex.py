pattern =r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

import re

email  = input("please enter email ")

email_match = re.fullmatch(pattern, email)
if email_match:
    print("valid")
else:
    print('not valid')