import os
print(os.getcwd())

path = os.getcwd()
fp = open(path+"\\text.txt")
str = fp.read()
print(str, end='')
fp.close()