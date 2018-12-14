''' Python 3 sorting playgroud ''' 


strArr = ['charlie', 'micheal', 'susan', 'kevin', 'sarah', 'bill', 'dawn', 'kim']
# newstr = strArr[:]
# print(strArr)

# strArr.append('pinky')
# # basic sort of an array. Returns the original instance as a sorted array.

# strArr.sort()
# print(strArr)
# print(newstr)

# for name in strArr:
#     print('Hi my name is ' + name.title() + ".")

numArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
unsortArr = [3, 7, 5, 1, 8, 9, 4, 2, 10, 6]

# print(numArr)
# numArr.reverse()
# print(numArr)
# numArr.sort()
# print(numArr)
# print(unsortArr)
# unsortArr.sort()
# print(unsortArr)


a = [1, 2, 3]
b = [4, 5, 6]
print("A: ", a)
print("B: ", b)
# a, b = b, a
# print("A is now: ", a)
# print("B is now: ", b)
a[0], b[2] = b[2], a[0]
print("A is now: ", a)
print("B is now: ", b)


x = [1, 2, 3, 4, 5]
def rev(arr):
    rvsArr = arr[::-1]
    print(rvsArr)
    return rvsArr

rev(x)
print(x)
print(x[::-1])

print(x[-1:])
print(x[:-1])
print(x[:])
