# range is a collection rather than a container
# is an arithmetic range of integers

print( range(5))  # specify stop value only and you get range(0,5), does not include 5

for i in range(5):
    print(i)

for i in range(4, 7): # start and stop values
    print(i)

# range with step
print( list( range( 12, 22, 2)))
print( tuple( range( 12, 22, 3)))


# enumerate returns an indexed tuple for a series of values

for i in enumerate((10,9,8,7)):
    print(i)
    a,b = i
    print("pos={}, val={}".format(a,b))

for pos,val in enumerate((10,9,8,7)):
    print("pos={}, val={}".format(pos,val))




