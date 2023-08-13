# GoalTracker
Be constantly reminded of your goals every time you open your laptop! In this project, I automatically update my screensaver to keep track of how many days I have achieved my goal in a row, how many days I have achieved my goal in total, how many days I have failed in a row, and how many days I have failed in total. In particular, my goal is to be working at my laptop by 11 AM. At 10 AM every day, launchd will run script.sh (if my laptop is off at 10 AM, the script will run upon wake), and a pop-up box will prompt me to check in. If the check-in is before 11 AM, the days succeeded in a row and total will increase. If the check-in comes after 11 AM, then the days failed will increase, and my screensaver will be automatically updated.

Here are steps to use this project for your own purposes (for Mac):

1. Create a .plist file in ~/Library/LaunchAgents (a sample has been provided). Update the Program Arguments field to point to script.sh and your Python installation. Update the StartCalendarInterval field to indicate at which time you want launchd to run the script.

2. Enter the command in command line: launchctl load ~/Library/LaunchAgents/<your_plist_file_name>.plist

3. Go to System Settings -> Privacy & Security -> Full Disk Access, and add bash so that it can access the necessary files.

4. Go to System Settings -> Screen Saver, and choose an option (I am using Classic) that allows you to choose your own source for the screensaver. Click on Options... and set the source as the ScreenSaver folder in the repo.

5. In wakeup.py, update PATH_TO_CURRENT_DIRECTORY.

6. In script.sh, update the command to be the absolute path of your Python installation and the repo.
