import time
from random import choice

# trySelectABunch: runs an implementation of SELECT a bunch, and times how long it takes.
#
# Input: myFn: a function which takes as input a list of integers
# Output: lists nValues and tValues so that running myFn on a list of length nValues[i] took (on average over numTrials tests) time tValues[i] milliseconds.
#
# Other optional args:
#    - Ns: list of inputs n to test
#    - numTrials: for each n tests, do numTrials tests and average them
#    - listMax: the input lists of length n will have values drawn uniformly at random from range(listMax)
#    - random: if True uses a random list.  If not just uses the numbers 1 through n.  (Useful for seeing the effect of bad pivots)
def trySelectABunch(myFn, Ns = range(10,100,10), numTrials=20, listMax = 10, random=True):
    nValues = []
    tValues = []
    for n in Ns:
        # run myFn several times and average to get a decent idea.
        runtime = 0
        for t in range(numTrials):
            if random:
                lst = [ choice(range(listMax)) for i in range(n) ] # generate a random list of length n
            else:
                lst = [ i for i in range(n) ] # just use the numbers 1-n.
            k = choice(range(1,n+1))
            start = time.time()
            myFn( lst , k)
            end = time.time()
            runtime += (end - start) * 1000 # measure in milliseconds
        runtime = runtime/numTrials
        nValues.append(n)
        tValues.append(runtime)
    return nValues, tValues

# We'll also want to use our earlier implementation of mergeSort
def merge(L, R):
    i = 0 # current index in the L array
    j = 0 # current index in the R array
    ret = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            ret.append(L[i])
            i += 1
        else:   # ties go to R.  Doesn't really matter.
            ret.append(R[j])
            j += 1
    while i < len(L):
        ret.append(L[i])
        i += 1
    while j < len(R):
        ret.append(R[j])
        j+= 1
    return ret
        
def mergeSort(A):
    n = len(A)
    if n <= 1:
        return A
    L = mergeSort(A[:round(n/2)])
    R = mergeSort(A[round(n/2):n])
    return merge(L,R)

