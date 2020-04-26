def forLoop(n):
    res = []
    for i in range(n+1):
        res.append(i)
    return res

def listCompre(n):
    return [i for i in range(n + 1)]

def whileLoop(n):
    k = 0
    res = []
    while k < n:
        res.append(k + 1)
        k += 1
    return res

import datetime
def timeAnalysis(fx, n):
    start = datetime.datetime.now()
    fx(n)
    end = datetime.datetime.now()
    return end - start

print('Time taken to generate list with for loop:', timeAnalysis(forLoop, 1000000000))
print('Time taken to generate list with list comprehension:', timeAnalysis(listCompre, 1000000000))
print('Time taken to generate list with while loop:', timeAnalysis(whileLoop, 1000000000))




