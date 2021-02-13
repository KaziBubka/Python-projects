
# create function to calculate decimal grade from 3 values

import csv
import math


def calculateDecimalGrade(Assign=50, MT=60, FP=100):
    # weight of Assign, MT and FP are 40/100, 35/100 and 25/100 respectively
    decimalGrade = (Assign * 0.4) + (MT * 0.35) + (FP * 0.25)
    print("Decimal grade is: " + str(decimalGrade))
    # print(Assign, MT, FP)
    return decimalGrade


# calculateDecimalGrade()

def testCalcGrade():
    # case 1
    calculateDecimalGrade(50, 60, 70)

    # case 2
    calculateDecimalGrade(63, 34, 33)

    # case 3
    calculateDecimalGrade(90, 34, 33)

    # case 4
    calculateDecimalGrade(90, 82, 100)

# create function to calculate alphabetical grade from decimal grade


def calculateAlphabeticalGrade(DecGrade=67):
    DecGrade = math.floor(DecGrade)
    if DecGrade < 50:
        alphabeticalGrade = 'F'
        print("Alphabetical Grade is: " + str(alphabeticalGrade))
        return alphabeticalGrade

    elif DecGrade >= 50 and DecGrade <= 52:
        alphabeticalGrade = 'D-'
        print("Alphabetical Grade is: " + str(alphabeticalGrade))
        return alphabeticalGrade

    elif DecGrade >= 53 and DecGrade <= 56:
        alphabeticalGrade = 'D'
        print("Alphabetical Grade is: " + str(alphabeticalGrade))
        return alphabeticalGrade

    elif DecGrade >= 57 and DecGrade <= 59:
        alphabeticalGrade = 'D+'
        print("Alphabetical Grade is: " + str(alphabeticalGrade))
        return alphabeticalGrade

    elif DecGrade >= 60 and DecGrade <= 62:
        alphabeticalGrade = 'C-'
        print("Alphabetical Grade is: " + str(alphabeticalGrade))
        return alphabeticalGrade

    elif DecGrade >= 63 and DecGrade <= 66:
        alphabeticalGrade = 'C'
        print("Alphabetical Grade is: " + str(alphabeticalGrade))
        return alphabeticalGrade

    elif DecGrade >= 67 and DecGrade <= 69:
        alphabeticalGrade = 'C+'
        print("Alphabetical Grade is: " + str(alphabeticalGrade))
        return alphabeticalGrade

    elif DecGrade >= 70 and DecGrade <= 72:
        alphabeticalGrade = 'B-'
        print("Alphabetical Grade is: " + str(alphabeticalGrade))
        return alphabeticalGrade

    elif DecGrade >= 73 and DecGrade <= 76:
        alphabeticalGrade = 'B'
        print("Alphabetical Grade is: " + str(alphabeticalGrade))
        return alphabeticalGrade

    elif DecGrade >= 77 and DecGrade <= 79:
        alphabeticalGrade = 'B+'
        print("Alphabetical Grade is: " + str(alphabeticalGrade))
        return alphabeticalGrade

    elif DecGrade >= 80 and DecGrade <= 84:
        alphabeticalGrade = 'A-'
        print("Alphabetical Grade is: " + str(alphabeticalGrade))
        return alphabeticalGrade

    elif DecGrade >= 85 and DecGrade <= 89:
        alphabeticalGrade = 'A'
        print("Alphabetical Grade is: " + str(alphabeticalGrade))
        return alphabeticalGrade

    elif DecGrade >= 90 and DecGrade <= 100:
        alphabeticalGrade = 'A+'
        print("Alphabetical Grade is: " + str(alphabeticalGrade))
        return alphabeticalGrade

    else:
        print("Invalid number")


# calculateAlphabeticalGrade()

def testAlphaGrade():

    # case 1
    calculateAlphabeticalGrade(58.5)

    # case 2
    calculateAlphabeticalGrade(45.35)

    # case 3
    calculateAlphabeticalGrade(56.15)

    # case 4
    calculateAlphabeticalGrade(89.7)


# import csv


def calculateGrades():
    # open csv file
    with open('final303.csv', 'r') as first_file:
        # read each line in csv file
        reader = csv.reader(first_file)
        # store each line in list
        # list1 = list(reader)
        list1 = list(filter(None, reader))
        # print list items to see if it worked
        # print(list1)

        newList = []

        # need each item in list
        for item in list1:
            # checking for empty strings in list
            if (item[2] != "" and item[3] != "" and item[4] != ""):
                # checking if 3rd, 4th and 5th values in list are numbers
                if (item[2].isdigit() and item[3].isdigit() and item[4].isdigit()):
                    # perform decimalgrade calculation using 3rd, 4th and 5th values in list
                    assnGrade = int(item[2])
                    midGrade = int(item[3])
                    finGrade = int(item[4])
                    # store result of decimalgrade calculation
                    decResult = calculateDecimalGrade(
                        assnGrade, midGrade, finGrade)
                    # print(decResult)
                    # append result to 6th value in list
                    item[5] = decResult
                    # perform alphabeticalgrade calculation on 6th value in list
                    # store result of alphabeticalgrade calculation
                    # append result to 7th value in list
                    item[6] = calculateAlphabeticalGrade(decResult)
                    # print list items to see if it worked
                    # print(item)

                    newList.append(item)

                    # print(newList)

    # print(newList)
    # open new file for writing
    with open('updatedfinal303.csv', 'w') as second_file:
        # initialize writer
        file_writer = csv.writer(second_file)
        # write the header
        file_writer.writerow(["FName", "LName", "Assignments",
                              "Mid Term", "Final", "Decimal", "Alphabetical"])

        for line in newList:

            file_writer.writerow(line)


# calculateGrades()
# close file


def convertToDict():
    newDict = {}
    # open CSV file
    with open('updatedfinal303.csv', 'r') as third_file:
        another_reader = csv.DictReader(third_file)
        # skip first 3 lines
        # next(another_reader)
        # next(another_reader)
        # next(another_reader)

        for row in another_reader:
            # print(thing)
            # print(row['FName'], row['LName'] + " : " +
            #       row['Decimal'], row['Alphabetical'])

            key = row['FName'] + " " + row['LName']
            value = [row['Decimal'], row['Alphabetical']]
            newDict[key] = value
    # print(newDict)
    return newDict


# convertToDict()


def showStudentGrades():
    gradeDict = convertToDict()

    while True:
        name = input("Select a full name to find their grades (x to exit): ")

        if (name == "x"):
            print("Thank you")
            break
        try:
            print(gradeDict[name])
        except:
            print("Unable to find student: " + name)


# showStudentGrades()

def main():
    testCalcGrade()
    testAlphaGrade()
    calculateGrades()
    convertToDict()
    showStudentGrades()


main()
