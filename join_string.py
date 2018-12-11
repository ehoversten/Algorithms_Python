''' Python 3 String Playground '''

strArr = "This is my string"

print(strArr)
print(strArr.split())
print(strArr.split(' '))

commaStr = "One, Two, Three, and a forth"
print(commaStr)
print(commaStr.split(', '))

newStr = strArr.split()
print(newStr)
jstr = ' '.join(newStr)
print(jstr)
