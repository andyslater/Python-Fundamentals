#
# 
#
# https://www.youtube.com/watch?v=CB_NCoxzQnk
# https://coderwall.com/p/temqxa/quicksort-in-python
#

#array = [97, 200, 100, 101, 211, 107]
#quicksort(array)

def dprint( level, *args ):
    if level <= 4 :
        print(*args)

# array -> [97, 100, 101, 107, 200, 211]
def partition(array, begin, end):
    pivot = begin
    for i in xrange(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot



def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)







# quick sort using the fsar right as the holder for the pivot see for example, below (# https://coderwall.com/p/temqxa/quicksort-in-python)
#   


def myq_sort(list):
    _myq_sort(list,0,len(list)-1)
    print("sorted list ", list)

def get_pivot(list,start,end):
    # determine the pivot point by choosing 3 values from the ends and middle and then selecting the median. THis helps with lists that are already sorted
    mid = (start+(end-start)//2)
    pval_list = [ list[start], list[end], list[mid] ]
    # order all three, then pick middle
    if pval_list[1]<pval_list[0]:
        pval_list[0],pval_list[1] = pval_list[1],pval_list[0] 
    if pval_list[2]<pval_list[1]:
        pval_list[2],pval_list[1] = pval_list[1],pval_list[2] 
    pval = pval_list[1]
    ppoint = start if pval == pval_list[0] else mid
    ppoint = end if pval == pval_list[2] else ppoint

    #ppoint = start
    return ppoint


def _myq_sort(list,start,end):
    # if small ist then swap as needed
    if end-start <= 2:
        l = list[start:end+1]
        l.sort()
        for i in range(start,end+1):
            list[i] = l[i-start]
        dprint(3, "short list start {} end {} sorted {} returning list {}".format(start,end,l,list))
        return

    ppoint = get_pivot(list,start,end)
    pval = list[ppoint]

    dprint(1, "\nstart {} end {} ppoint {} ({}) sublist {} full list {}".format( start, end, ppoint, pval, list[start:end+1],list))

    # swap data in ppoint and end point. this puts the pval in the end where it will stay till the end of the process. then it is put back into the next_swap location
    list[end], list[ppoint] = list[ppoint], list[end]
    dprint(2, "{} ({}) swapped to {} list {}".format(ppoint, list[end], end, list))

    # calculate last cpoint value for comparison
    cpoint_max = end -1
    ipoint = start
    cpoint = ipoint +1 

    # start swapping
    while cpoint <= cpoint_max:
        while ipoint < cpoint_max and list[ipoint] <= list[end]:
            dprint(3, "data at insertion point {} ({}) already valid, advancing ipoint".format(ipoint,list[ipoint]))
            ipoint += 1

        if ipoint == cpoint_max:
            dprint(4, 'ipoint {} reached max possible insertion point {}. extiting swapping'.format(ipoint,cpoint_max))
            break

        if cpoint <= ipoint: cpoint = ipoint +1  # really only happens on the very first look when the initial values are valid
        dprint(4, 'ipoint {} ({}) cpoint {} ({}) list {}'.format(ipoint,list[ipoint],cpoint,list[cpoint],list))
        
        # find next swap
        while cpoint <= cpoint_max:
            if list[cpoint] <= list[end]:   # swap found
                msg = "checkpoint {} ({}) < {} swapped with ipoint {} ({}) ".format(cpoint, list[cpoint], list[end], ipoint, list[ipoint])
                list[ipoint], list[cpoint] = list[cpoint],list[ipoint]
                cpoint += 1 # advance the new check pointer even if we break, since what we are subbing in wil be invalid 
                ipoint += 1 # advance the insertion point
                dprint(4, msg,'advanced ipoint {} ({}) and cpoint {} ({}) list {}'.format(ipoint, list[ipoint], cpoint, list[cpoint], list))
                break
            else:
                dprint(4, 'cpoint {} ({}) not valid advancing cpoint'.format(cpoint, list[cpoint]))
            cpoint += 1 # advance the check point if we dont break


    # get the pivot value in end into the insertion point 
    # may have gotten here on a boundary condition ipoint == cpoint_max which meands nothing more to check, but the value that the insertion point is on may be <= the pval (insert was stopped at end rather than invalid valur)
    if ipoint == cpoint_max : 
        if list[ipoint] > list[end]:    list[ipoint], list[end] = list[end], list[ipoint]
        ipoint = end
    else:
        list[ipoint], list[end] = list[end], list[ipoint]
    
    dprint(3,"restored pivotvalue ({}) to split location {} for new list {}".format(list[ipoint],ipoint,list))

    # recurse
    dprint(1, 'start {} ipoint {} end {} list{}'.format(start,ipoint, end, list))
    dprint(3, "left list {}".format(list[start:ipoint]))
    dprint(3, "right list {}".format(list[ipoint+1:end+1]))
    if  (ipoint -1) - start >= 1: #length must be > 1
        _myq_sort(list,start,ipoint -1)
    else:
        dprint(4, "skipping left list, size is 1")
        
    if end - (ipoint +1) >= 1:
        _myq_sort(list,ipoint +1, end)
    else:
        dprint(4, "skipping right list size is {} start {} end {} list{}".format(end - (ipoint +1),ipoint+1,end,list))
    
myq_sort([8,3,5,9,7,6,2,15])




import random
random.randrange(5000)

myq_sort([randrange(10000) for i in range(50)])


