# The two text files 2000_BoysNames.txt and 2000_GirlsNames.txt list the popularity of
# boys names and girls names in 2000. The format of the file is simple, one line per
# entry with the name followed by a space followed by the number of children carrying
# that name. You must write a python program that reads each text file then converts it
# into a csv format: "name",count then saves the entry in a csv file. The output csv file
# must include the following header as its first line: "First Name","Count"

import csv

with open('2000_BoysNames.txt', 'r') as txtIn:
    with open('boys_names.csv', 'w') as csvOut:

        csvOut.write('Name, Count\n')
        for line in txtIn:
            csvOut.write(line)

with open('2000_GirlsNames.txt', 'r') as txtIn2:
    with open('girls_names.csv', 'w') as csvOut2:

        csvOut2.write('Name, Count\n')
        for line in txtIn2:
            csvOut2.write(line)
            print(line)

with open('font3.txt', 'r') as txtIn3:
    with open('font3.csv', 'w') as csvOut3:

        # csvOut3.write('Name, Count\n')
        for line in txtIn3:
            csvOut3.write(line)
            # print(line)

# file_path = 'boys_names.csv'
# file_path2 = 'girls_names.csv'


# def csvToList(filepath):

#     with open(filepath, 'r') as f:
#         reader = csv.reader(f)
#         csvList = list(reader)

#         print(csvList)


# csvToList(file_path)
# csvToList(file_path2)
