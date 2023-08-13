# import everything from tkinter module
from tkinter import *
from datetime import datetime, time
from PIL import Image, ImageDraw, ImageFont
import tkinter.messagebox

PATH_TO_CURRENT_DIRECTORY = '/Users/victorcai/Desktop/VictorCai/Goals/'
PATH_TO_SCREENSAVER = PATH_TO_CURRENT_DIRECTORY + 'ScreenSaver/screensaver.png'

img = Image.new(mode = "RGB", size = (600, 300))
fnt = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", 30)
i1 = ImageDraw.Draw(img)

# deadline to check in: 11 AM
deadline = time(11,0,0)
  
# create a tkinter root window
root = tkinter.Tk()
  
# root window title and dimension
root.title("Did you achieve your goal today?")
root.geometry('500x300')

def onClick():
    now = datetime.now().time()
    with open(PATH_TO_CURRENT_DIRECTORY + 'days.txt') as f:
        lines = f.readlines()
    daysSucceededInRow = int(lines[0])
    totalDaysSucceeded = int(lines[1])
    daysFailedInRow = int(lines[2])
    totalDaysFailed = int(lines[3])
    if now < deadline:
        daysSucceededInRow += 1
        daysFailedInRow = 0
        totalDaysSucceeded += 1
    else:
        daysSucceededInRow = 0
        daysFailedInRow += 1
        totalDaysFailed += 1
        
    with open(PATH_TO_CURRENT_DIRECTORY + 'days.txt', 'w') as f:
      f.write(str(daysSucceededInRow) + '\n')
      f.write(str(totalDaysSucceeded) + '\n')
      f.write(str(daysFailedInRow) + '\n')
      f.write(str(totalDaysFailed) + '\n')

    daySuccStr = "day" if daysSucceededInRow == 1 else "days"
    i1.text((20,20), "I achieved my goal for " + str(daysSucceededInRow) + " " + str(daySuccStr) + " in a row", font = fnt)
    totalSuccStr = "day" if totalDaysSucceeded == 1 else "days"
    i1.text((20,90), "I achieved my goal for " + str(totalDaysSucceeded) + " " + str(totalSuccStr) + " total", font = fnt)
    dayFailStr = "day" if daysFailedInRow == 1 else "days"
    i1.text((20,160), "I failed for " + str(daysFailedInRow) + " " + str(dayFailStr) + " in a row", font = fnt)
    totalFailStr = "day" if totalDaysFailed == 1 else "days"
    i1.text((20,230), "I failed for " + str(totalDaysFailed) + " " + str(totalFailStr) + " total", font = fnt)
    # img.show()
    img.save(PATH_TO_SCREENSAVER)
    root.destroy()
  
# Create a Button
button = Button(root, text="Check In", command=onClick, height=5, width=10)
  
# Set the position of button on the top of window.
button.pack(side='bottom')
root.mainloop()