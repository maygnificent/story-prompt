import sys
import json

if __name__ == '__main__':

    # convert input to dictionary
    inputString = sys.argv[1]
    inputDict = json.loads(inputString)

    # check for missing inputs
    while len(inputDict) < 5:
        missingInput = ''
        try:
            if 'number' not in inputDict:
                missingInput = 'number'
                inputDict['number'] = int(input("Please enter a number: "))
            
            if 'unit_of_measure' not in inputDict:
                missingInput = 'unit_of_measure'
                inputDict['unit_of_measure'] = input("Please enter a unit of measure: ")
            
            if 'place' not in inputDict:
                missingInput = 'place'
                inputDict['place'] = input("Please enter a place: ")

            if 'adjective' not in inputDict:
                missingInput = 'adjective'
                inputDict['adjective'] = input("Please enter an adjective: ")
            
            if 'noun' not in inputDict:
                missingInput = 'noun'
                inputDict['noun'] = input("Please enter a noun: ")
            
        except ValueError:
            print(f"Invalid input. Please enter a(n) {missingInput}: ")
            continue
        
        else:
            break

    # check string input length
    for item in inputDict:
        # checks for strings with over 100 chars or empty strings / strings with just spaces
        if item != 'number' and (len(inputDict[item]) > 100 or not(inputDict[item] and not inputDict[item].isspace())):
            inputDict[item] = input(f"Please enter another {item} (max 100 characters): ")

    # archive inputs to 'record' file
    archive = open("record.txt", "a")
    # archive.write(str(inputDict) + '\n')
    archive.write(json.dumps(inputDict) + '\n')
    archive.close

    # place each input into template
    output = f"One day Anna was walking her {inputDict['number']} {inputDict['unit_of_measure']} commute to {inputDict['place']} and found a {inputDict['adjective']} {inputDict['noun']} on the ground."
    print (output)
