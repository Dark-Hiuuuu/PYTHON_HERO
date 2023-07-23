def solveAndPrintLst(n):
    lst = []
    for i in range(1,n+1):
        lst.append(int(input(f"number {i} is:")))
    return lst
def count_Equal(resultList):
    varCompareA = resultList[0]
    countEqual = 0
    for i in resultList:
        if varCompareA == i:
            countEqual += 1
    if countEqual == len(resultList):
        return True
    else: 
        return False
if __name__ == "__main__":
    n = int(input("enter element's number:"))
    print(count_Equal(solveAndPrintLst(n)))

