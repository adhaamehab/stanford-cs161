# These are a few helper functions for the Lecture 1 IPython notebook.

import time
from random import choice

# a few helpful functions
def getDigits(x): # takes an integer x and returns a list of digits, most significant first
    return [ int(a) for a in str(x) ]

def makeInt(digits): # takes a list of digits (as returned by getDigits) and returns the integer they represent
    return sum( [ 10**(len(digits)-i-1)*digits[i] for i in range(len(digits))])


# multABunch: runs a multiplication function a bunch, and times how long it takes.
#
# Input: myFn: a function which takes as input two n-digit integers
#              (Notice that in python you can pass a function as input!)
#        nVals: list of n values to test at
# Output: lists nValues and tValues so that running myFn on a list of length nValues[i] took (on average over numTrials tests) time tValues[i] milliseconds.
#
# Other optional args:
#    - numTrials: for each n tests, do numTrials tests and average them
#    - listMax: the input lists of length n will have values drawn uniformly at random from range(listMax)
def multABunch(myFn, nVals, numTrials=20):
    nValues = []
    tValues = []
    for n in nVals:
        # run myFn several times and average to get a decent idea.
        runtime = 0
        for t in range(numTrials):
            lst1 = [ choice(range(10)) for i in range(n) ] # generate a random list of length n
            lst2 = [ choice(range(10)) for i in range(n) ] # generate another random list of length n
            X = makeInt(lst1)
            Y = makeInt(lst2)
            start = time.time()
            myFn( X, Y )
            end = time.time()
            runtime += (end - start) * 1000 # measure in milliseconds
        runtime = runtime/numTrials
        nValues.append(n)
        tValues.append(runtime)
    return nValues, tValues

# next, you can do:
# plt.plot(nValues, tValues)
# or something like that
