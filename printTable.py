
tableData = [["apples", "oranges", "cherries", "banana"],
             ["Alice", "Bob", "Carol", "David"],
             ["dogs", "cats", "moose", "goose"]]

def prinTable(listoflist):
    colWidth = [0] * len(listoflist)
    n = 0
    while n < len(listoflist):
        maxLen = 0
        for element in listoflist[n]:
            if len(element) > maxLen:
                maxLen = len(element)
        colWidth[n] = maxLen
        n = n + 1
    newList = []
    i = 0
    while i < len(listoflist[0]):
        j = 0
        concave = []
        while j < (len(listoflist)):
            concave.append(listoflist[j][i].rjust(colWidth[j]))
            j = j + 1
        newList.append(concave)
        print(" ".join(newList[i]))
        i = i + 1

prinTable(tableData)


#my take on the subject 
