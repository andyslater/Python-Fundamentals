
# for REPL to include use "from exceptions.exceptionalx import *"

def convert(s):
    x = -1   
    try:
        x = int(s)
        print('convert ok ', x )
    except (ValueError, TypeError):
        pass # must have something here. THis will simply do nothing. without this or someother statement this will generate an errror
    return x


import sys
def convert2(s):
    try:
        return int(s)
    except (ValueError, TypeError) as e :
        print("conversion error", e, file=sys.stderr)  # print this to stderr
        raise # raise the exception again
    else:
        # this executes only if there is no exception
        print('no exception')
    finally:
        print("did this last")


def sqrt(x,cnt=5):
    
    if x<0:
        raise ValueError("Cannot use -ve numbers: ", x)
    
    guess = x
    i = 0
    while guess * guess != x and i < cnt :
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess, guess*guess

# exception types




