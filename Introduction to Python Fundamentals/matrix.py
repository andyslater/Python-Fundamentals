#
# matrix
#
m = [[1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]]

print(m)

print(m[::-1]) # reverse order
print( zip(m[::-1]) )

rotated = zip(*m[::-1])
print(rotated) # note rotated points a function that operates on m, that is why its printed as an oobect, andy why changing m changes rotated
m[1][1] = 10000
for i in rotated :
    print(i)

rotated = [list(i) for i in zip(*m[::-1])] # the list(i) converts the tuple of the zip into a list
print(rotated) # note rotated points a function that operates on m, that is why its printed as an oobect, andy why changing m changes rotated
m[1][1] = 100
for i in rotated :
    print(i)


# the long way to rotate a matrix

m = [[1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]]

nm = []


for cols in range(len(m[0])):
    print(cols)
    nm.append([])
print(nm)


for row in m:
    print(row)
    i = 0
    for procrow in row:
        nm[i].append(procrow)
        i += 1

print('nm=',nm)
print('nm.reverse=',nm[::-1])




