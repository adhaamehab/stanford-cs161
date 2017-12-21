# First, let's implement a simple FIFO queue.
class myQueue:
    def __init__(self):
        self.lst = []

    def push(self,x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop(0)
    
    def getList(self):
        return self.lst

    
# next, we'll need a class to deal with m-digit integers
def getDigits(x, base):
    digits = []
    while x > 0:
        digits.append( x % base )
        x = (x / base).__trunc__() # integer division
    return digits
        
# this stores the digits of an integer, and it has a key that returns the keyDigit'th digit.
class myInt:
    def __init__(self,x, base=10, keyDigit=0):
        self.digits = getDigits(x, base)  # these are the digits, so that self.digits[0] is least significant.
        self.keyDigit = keyDigit
        self.value = x
        
    def key(self):
        if len(self.digits) > self.keyDigit:
            return self.digits[self.keyDigit]
        return 0
    
    def updateKeyDigit(self,p):
        self.keyDigit = p
        
    def getValue(self):
        return self.value
    
        