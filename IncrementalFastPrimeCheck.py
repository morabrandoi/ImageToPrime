class IncrementalFastPrimeChecker():
    def __init__(self, startNum, verbose=False):
        self.startNum = startNum
        self.curNum = startNum
        self.verbose = verbose
    
    def getCurNum(self):
        return self.curNum

    def increment(self):
        self.curNum += 1

    def isPrime(self):
        pass