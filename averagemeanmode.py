#get input
max = (int(input("How many tests do you want to record? ")))
test = []
for i in range(0, max):
    test.append(int(input("Enter test #" + str(i + 1) + ": ")))

#average
def getAvg(someList):
    avg = 0
    for i in someList:
        avg += i
    return avg/len(someList)
    
#mode
def getMode(someList):
    modes = []
    occurence = 0
    for i in someList:
        if someList.count(i) > occurence:
            occurence = someList.count(i)
            modes.append(i)
        elif someList.count(i) == occurence and i not in modes:
            modes.append(i)
    return modes 

#median
def getMedian(someList):
    someList.sort()
    median = 0
    if (len(someList)%2 != 0):
        return someList[int(len(someList)/2)]
    else:
        median = (len(someList)-1)/2
        return (someList[int(median)] + someList[int(median + 1)] )/2

print("Average: ", getAvg(test))
print("Mode(s): ", getMode(test))
print("Median: ", getMedian(test))

    
