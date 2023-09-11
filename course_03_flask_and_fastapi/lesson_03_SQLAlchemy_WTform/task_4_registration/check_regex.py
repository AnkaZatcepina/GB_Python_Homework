import re
pattern = "^.*(?=.*\d)(?=.*[a-zA-Z]).*$"
password = 'qwerty1'
result = re.findall(pattern, password)
if (result):
    print("Valid password")
else:
    print("Password not valid")