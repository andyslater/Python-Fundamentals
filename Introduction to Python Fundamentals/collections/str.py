# str = homogeneous immutable 
#  string methods: https://docs.python.org/3/library/stdtypes.html#string-methods

print( len("asdfasf") )

print("a"+"ndy")

# join is a more efficient method to add string togehter

#make alpabet
print( ''.join(chr(c + ord('a')) for c in range(26)) )



joined = ";".join(['this','and','5'])
print(joined)

l = joined.split(";")
print(l)

joined = ''.join(l)  # most efficient way to concatenate text
print(joined)


# partition and extraction
departure, sep, arrival = 'london:bdl'.partition(':')
print(departure, sep, arrival )

departure, _, arrival = 'jfk:stm'.partition(':')  # use _ when you dont need the sep in a variable
print(departure, arrival )

#format
print("{0} this is the first, {1} this is the second. is {1} bigger than {0}".format(1,2))

print("{} this is the first, {} this is the second".format(1,2)) # numbers not needed if used only once and in order

print("{name} is {age} year old".format(name="andy", 
                                        age="55")
      )

xvals = (22,33,44)
values = (1,2,3,4)
print("v1={v[0]}, v2={v[2]}, v3={v[3]}, xv={v[1]}".format(v=values,xv=xvals))

import math
print("pi={m.pi}, e={m.e}".format(m=math))

import math
print("pi={m.pi:.3f}, e={m.e:.3f}".format(m=math))  # can apply formatting to the value printed in the format method

help(str) # for more

# string slicing s{start:stop:step]
s = '0123456789'
print(s[1])
print(s[1:])
print(s[1:-1])
print(s[:0:-1])
print(s[2::-1]) # start at 2 and include it, then go backwards till 0 . then going backward 0 is the the other end?

set('this is a sting')  # turned into a set will remove the duplicates, but not in nay order


# anagram?
sorted('this is a string'.replace(' ','')) == sorted('this is a string'.replace(' ',''))



def hanoi(n, a='A', b='B', c='C'):
    """Move n discs from a to c using b as middle."""
    if n == 0:
        return
    hanoi(n - 1, a, c, b)
    print(a, '->', c)
    hanoi(n - 1, b, a, c)


def main():
    hanoi(4)

print("a {}".format(22))

