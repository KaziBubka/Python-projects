# Write a function generateDictionary that reads the file font3.txt
# and generate a dictionary where the key is the character ane the
# value is the 8*8 bit list representation of the character.

import csv
import re

from gfxhat import lcd, fonts
from PIL import Image, ImageFont, ImageFont
from click import getchar


def clearScreen(lcd):
    lcd.clear()
    lcd.show()


# taking in the object, its x-y starting coordinate, and displaying to gfxhat

def displayObject(obj, x, y):
    lcd.clear()
    xp = x

    # looping over y coordinate
    for y1 in obj:

        # looping over x coordinate
        for x2 in y1:

            if x2 == 1:
                pixel = 1
            else:
                pixel = 0

            lcd.set_pixel(xp, y, pixel)
            xp = xp + 1

        y = y + 1
        lcd.set_pixel(xp, y, pixel)
        xp = x

    lcd.show()


def fileOpen(filepath):
    return open(filepath, 'r')


def generateDictionary(file):
    dictionary = {}
    for line in file:
        newLine = re.split(',', line.strip())
        key = newLine[1]
        value = convertToBin(newLine[0])
        dictionary[key] = value
    return dictionary


def convertToBin(inp):
    someList = [
        inp[2]+''+inp[3],
        inp[4]+''+inp[5],
        inp[6]+''+inp[7],
        inp[8]+''+inp[9],
        inp[10]+''+inp[11],
        inp[12]+''+inp[13],
        inp[14]+''+inp[15],
        inp[16]+''+inp[17]
    ]

    for i in range(len(someList)):
        # converting each string item in list to a binary value
        # [2:] is needed because bin() converts into format '0b---' so we need to cut off first 2 values
        someList[i] = bin(int(someList[i], 16))[2:].zfill(8)

    return someList


def main():
    newFile = fileOpen('font3.txt')
    dictionary = generateDictionary(newFile)

    newInp = input('Enter a key: ')

    displayObject(dictionary[newInp], 63, 40)

    getchar()
    clearScreen(lcd)


main()
