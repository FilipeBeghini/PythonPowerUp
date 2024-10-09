# Header>
import pyautogui
import time
from config import get_database

# get position needed to click with the actual cursor position
time.sleep(3)
print(pyautogui.position())


database = get_database()
print (database)
