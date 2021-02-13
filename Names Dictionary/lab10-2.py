# Write a python program that prompts the user for the name of .csv file then reads and
# displays each line of the file as a Python list. Test your program on the 2 csv files
# that you generated in Task 1.


import csv


def csvToList(filepath):

    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        csvList = list(reader)

        print(csvList)


def askForNames():
    name = int(input('Which names do you want? Enter 1 for boys or 2 for girls: '))

    if name == 1:
        file_path = 'boys_names.csv'
        csvToList(file_path)
    elif name == 2:
        file_path = 'girls_names.csv'
        csvToList(file_path)
    else:
        print('Enter 1 or 2:')


askForNames()
