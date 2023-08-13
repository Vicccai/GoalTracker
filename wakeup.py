# import everything from tkinter module
from tkinter import *
from datetime import datetime, time
from PIL import Image, ImageDraw, ImageFont
  
# import messagebox from tkinter module
import tkinter.messagebox

img = Image.new(mode = "RGB", size = (600, 300))
fnt = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", 30)

i1 = ImageDraw.Draw(img)

i2 = ImageDraw.Draw(img)

img.save("/Users/victorcai/Desktop/ScreenSaver/screensaver.png")

d = datetime.now().time()
end = time(11,0,0)
  
# create a tkinter root window
root = tkinter.Tk()
  
# root window title and dimension
root.title("Did you achieve your goal today?")
root.geometry('500x300')

def onClick():
    now = datetime.now().time()
    with open('/Users/victorcai/Desktop/VictorCai/Goals/daysSucceeded.txt') as f:
        lines = f.readlines()
    daysSucceeded = int(lines[0])

    with open('/Users/victorcai/Desktop/VictorCai/Goals/daysFailed.txt') as f:
        lines = f.readlines()
    daysFailed = int(lines[0])
    if now < end:
        daysSucceeded += 1
        daysFailed = 0
    else:
        daysSucceeded = 0
        daysFailed += 1
    with open('/Users/victorcai/Desktop/VictorCai/Goals/daysSucceeded.txt', 'w') as f:
      f.write(str(daysSucceeded))
    with open('/Users/victorcai/Desktop/VictorCai/Goals/daysFailed.txt', 'w') as f:
      f.write(str(daysFailed))
    daySuccStr = "day" if daysSucceeded == 1 else "days"
    i1.text((10,50), "I achieved my goal for " + str(daysSucceeded) + " " + str(daySuccStr) + " in a row", font = fnt)
    dayFailStr = "day" if daysFailed == 1 else "days"
    i2.text((10,180), "I failed for " + str(daysFailed) + " " + str(dayFailStr) + " in a row", font = fnt)
    # img.show()
    img.save("/Users/victorcai/Desktop/ScreenSaver/screensaver.png")
    root.destroy()
  
# Create a Button
button = Button(root, text="Check In", command=onClick, height=5, width=10)
  
# Set the position of button on the top of window.
button.pack(side='bottom')
root.mainloop()