""" Task1 :

    Create a program that simulates an etch a sketch machine on the gfxhat. The use use the arrow keys of the keyboard to create the pixels.
        Wrap around the falue of x and y, ie if x is > 127, it goes back to x=0. If y > 63, it goes back to 0. Same for x<0 back to 127, y<0 back to 63.
        Use the function getch from the click module to capture a keystroke
        The key s is use to start again a new drawing on the hat.
        The key q is used to quit.
        The character code for the arrow keys are the following:
            '\x1b[A' UP arrow key
            '\x1b[B' DOWN arrow key
            '\x1b[C' RIGHT arrow key
            '\x1b[D' LEFT arro key
    Your program should also display the text Etch a Sketch somewhere on the screen. Use the function displayText provided. """

""" Task2:

    Write a function displayObject with the folowing signature:

    displayObject(obj,x,y)

    The function displays an object represented as a tuple or a list on the gfxhat at position x,y

    Test your function on the following objects: 

    Write a program that tests your displayObject function. The program prompts the user for the x,y coordinates, the object to display and displays it.
    Feel free to create your own objects to display on the gfxhat. I used piskel to create the two objects. 
 """


from gfxhat import lcd, fonts, backlight
from PIL import Image, ImageFont, ImageDraw
from click import getchar
f1 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
# ^fighter jet object

# pac man object
pm = [[0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
      [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
      [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
      [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
      [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
      [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
      [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0]
      ]


def clearBacklight():

    backlight.set_all(0, 0, 0)
    backlight.show()


def clearScreen(lcd):

    lcd.clear()
    lcd.show()


def displayText(text, lcd, x, y):

    lcd.clear()
    # get width and height
    width, height = lcd.dimensions()
    # create new image
    image = Image.new('P', (width, height))
    # draw said image
    draw = ImageDraw.Draw(image)
    # get font
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x, y), text, 1, font)

    for x1 in range(x, x+w):
        for y1 in range(y, y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)

    lcd.show()


def setLight(r, g, b):
    backlight.set_all(r, g, b)
    backlight.show()


def etchSketch(x, y):
    while True:
        key = getchar()
        lcd.set_pixel(x, y, 1)
        lcd.show()

        # key 's' restarts the game
        if key == 's':
            clearScreen(lcd)

        # key is up arrow
        elif key == '\x1b[A':
            y = y - 1
            if y == 0:
                y = 63
            lcd.set_pixel(x, y, 1)
            lcd.show()

        # key is down arrow
        elif key == '\x1b[B':
            y = y + 1
            if y == 63:
                y = 0
            lcd.set_pixel(x, y, 1)
            lcd.show()

        # key is right arrow
        elif key == '\x1b[C':
            x = x + 1
            if x == 127:
                x = 0
            lcd.set_pixel(x, y, 1)
            lcd.show()

        # key is left arrow
        elif key == '\x1b[D':
            x = x - 1
            if x == 0:
                x = 127
            lcd.set_pixel(x, y, 1)
            lcd.show()

        # key 'q' quits the game
        elif key == 'q':
            lcd.clear()
            lcd.show()
            exit()

        else:
            print("Press a valid option")


def displayObject(obj, x, y):
    lcd.clear()
    xp = x

    # looping over y coordinate
    for y1 in obj:

        # looping over x coordinate
        for x2 in y1:
            lenY = len(obj)
            lenX = len(y1)

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


def mainMenu():

    print()
    print("________Main Menu________")
    print(
        ''' ||  Select:               ||\n
        |    1- Etch Sketch         ||\n
        |    2- Display Object      ||\n
        |    3- exit                ||''')
    print("_________________________")

    option = input()

    if option == "1":

        lcd.clear()

        lcd.show()

        bg = "Etch A Sketch"

        xPoint = int(input("Enter the x coordinate (0 to 127):"))

        yPoint = int(input("Enter the y coordinate (0 to 63):"))

        displayText(bg, lcd, 20, 20)

        etchSketch(xPoint, yPoint)

        mainMenu()

    elif option == "2":

        # clear the screen
        lcd.clear()

        # display the cleared screen
        lcd.show()

        print("Choose: \n 1- draw a Fighter jet \n 2- to draw a Pac Man")

        obj = int(input())

        # displays fighter object if option is 1
        if obj == 1:
            obj = f1

        # displays pacman if option is 2
        elif obj == 2:
            obj = pm

        else:
            print("Choose a valid option")
            print("Choose: \n 1- draw a Fighter jet \n 2- to draw a Pac Man")

        for y1 in obj:
            for x1 in y1:
                lengthX = len(y1)
                lengthY = len(obj)

        xPoint = int(input("Enter the x coordinate (0 to 127):"))

        yPoint = int(input("Enter the y coordinate (0 to 63):"))

        totalX = lengthX + xPoint
        totalY = lengthY + yPoint

        if totalX > 127:
            print("Please enter a smaller X coordinate")
            xPoint = int(input("Enter the x coordinate (0 to 127):"))
            displayObject(obj, xPoint, yPoint)

        elif totalY > 63:
            print("Please enter a smaller Y coordinate")
            yPoint = int(input("Enter the y coordinate (0 to 63):"))
            displayObject(obj, xPoint, yPoint)

        else:
            displayObject(obj, xPoint, yPoint)

        mainMenu()

    elif option == "3":

        lcd.clear()
        lcd.show()
        clearBacklight()
        exit


mainMenu()
