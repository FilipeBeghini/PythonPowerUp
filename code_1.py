# Imports>
import pyautogui
import time
import pandas
from config import get_database

#timer config
pyautogui.PAUSE = 0.5

# Register Products
#1. Open system to register the products (https://dlp.hashtagtreinamentos.com/python/intensivao/login)

pyautogui.press ("win")
pyautogui.write ("chrome")
pyautogui.press ("enter")
time.sleep(2)
pyautogui.write ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press ("enter")
time.sleep(2)

#2. sign in (user: user@system.com  PW: admin)
pyautogui.click (x=609, y=379)
pyautogui.write ("user@system.com")
pyautogui.press ("tab")
pyautogui.write ("filipe")
pyautogui.press ("tab")
pyautogui.press ("enter")
time.sleep(2)

#3. import data from database products.csv
database = get_database()
print (database)

# for loop
line = 0
pyautogui.PAUSE = 0.1
for line in database.index: # for each database index do the registration process.

        # 4. register a product
                # prod_code
        pyautogui.click (x=419, y=258)
        item_db = database.loc [line, "codigo"]
        pyautogui.write (str(item_db))
        pyautogui.press ("tab")
                # brand
        item_db = database.loc [line, "marca"]
        pyautogui.write (str(item_db))
        pyautogui.press ("tab")
                # kind
        item_db = database.loc [line, "tipo"]
        pyautogui.write (str(item_db))
        pyautogui.press ("tab")
                # category
        item_db = database.loc [line, "categoria"]
        pyautogui.write (str(item_db))
        pyautogui.press ("tab")
                # unit price
        item_db = database.loc [line, "preco_unitario"]
        pyautogui.write (str(item_db))
        pyautogui.press ("tab")
                # product cost 
        item_db = database.loc [line, "custo"]
        pyautogui.write (str(item_db))
        pyautogui.press ("tab")
                # Comments
        item_db = database.loc [line, "obs"]
        if not pandas.isna (item_db): # if item_db is not empty write it.
                pyautogui.write (str(item_db))
        pyautogui.press ("tab")
        pyautogui.press ("enter")

#5. Repeat the register process until all products has been registered
        pyautogui.scroll(1000)
        
pyautogui.PAUSE = 0.5
print ("success!")

#end
