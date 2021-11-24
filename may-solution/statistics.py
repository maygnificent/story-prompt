import json
from collections import Counter

if __name__ == '__main__':
    
    # parse text file 
    recordList = []
    with open('record.txt') as file:
        for line in file:
            # create dictionary from 'json strings'
            recordDict = json.loads(line)
            recordList.append(recordDict)
    
    # find min/max number 
    firstNum = recordList[0]['number']
    maxNum, minNum = firstNum, firstNum
    avg, sumNum= 0, 0
    for item in recordList:
        sumNum += item['number']
        maxNum = max(maxNum, item['number'])
        minNum = min(minNum, item['number'])
    avg = sumNum / len(recordList)
    print("Biggest number: " + str(maxNum))
    print("Smallest number: " + str(minNum))
    print("Average of numbers: " + str(avg))

    # find most common responses
    measureCounter = Counter(items['unit_of_measure'] for items in recordList)
    print("3 Most Common Units of Measure: " + str(measureCounter.most_common(3)))

    placeCounter = Counter(items['place'] for items in recordList)
    print("3 Most Common Places: " + str(placeCounter.most_common(3)))

    adjCounter = Counter(items['adjective'] for items in recordList)
    print("3 Most Common Adjectives: " + str(adjCounter.most_common(3)))

    nounCounter = Counter(items['noun'] for items in recordList)
    print("3 Most Common Nouns: " + str(nounCounter.most_common(3)))


