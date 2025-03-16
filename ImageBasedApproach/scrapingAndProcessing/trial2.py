import pyautogui
import time
import pyperclip
import logging
import os
import pyscreeze

# Open Spotlight Search (Command + Space)
# pyautogui.keyDown("command")
# time.sleep(0.1)  # Short delay for reliability
# pyautogui.press("space")
# time.sleep(0.1)  # Let Spotlight open
# pyautogui.keyUp("command")

# # Type "ChatGPT"
# time.sleep(0.5)  # Wait for Spotlight to fully appear
# pyautogui.write("ChatGPT", interval=0.1)

# # Press Enter to open it
# time.sleep(0.5)
# pyautogui.press("enter")


# print("Move your mouse to the message bar and wait for 5 seconds...")
# pyautogui.sleep(5)  # Gives you time to move the mouse
# print("Current mouse position:", pyautogui.position())  # Prints the X, Y coordinates

# pyautogui.sleep(5)
# print("Current mouse position:", pyautogui.position())  # Prints the X, Y coordinates



# # # Move the cursor to the bottom of the screen (adjust as needed)
# # pyautogui.moveTo(383, 822)  # X and Y coordinates (change based on your screen resolution)
# # pyautogui.click()  # Click to activate the message bar
# # pyautogui.write("Write python code to generate a freeCAD model of the following user query: A flat ring with outer radius of 25mm, inner radius of 15mm, with three evenly spaced square holes on the ring, each side of the square being 3mm.", interval=0.001)
# # pyautogui.press("enter")

# # time.sleep(2)
# # position = False
# # # try:
# # position = pyautogui.locateCenterOnScreen("/Users/krishhashia/Desktop/copy_button.png")
# position = (1268, 386)
# pyautogui.click(position)
# # except pyautogui.ImageNotFoundException or pyscreeze.ImageNotFoundException:
# secondPosition = pyautogui.locateCenterOnScreen("/Users/krishhashia/Desktop/copy_button2.png")

# if secondPosition:
#     pyautogui.click(secondPosition)
# elif position:
#     pyautogui.click(position)
# else:
#     print("Copy button not found!") 

# print(pyperclip.paste())

time.sleep(5)
import pyautogui
import pytesseract
from PIL import Image
import time

# copy_position = pyautogui.position()
# print(copy_position)
pyautogui.click((507,67))

for _ in range(12):
    pyautogui.hotkey('command', '-')

# time.sleep(3)

# # Take a screenshot
# screenshot = pyautogui.screenshot()

# # Use OCR to extract text
# text = pytesseract.image_to_string(screenshot)

# # Check if "Copy" appears
# if "Copy" in text:
#     print("Found Copy Button!")

#     # Locate all possible "Copy" positions
#     button_locations = pyautogui.locateAllOnScreen("/Users/krishhashia/Desktop/copy_button.png", confidence=0.8)
#     for loc in button_locations:
#         print(f"Top-left: ({loc.left}, {loc.top}), Width: {loc.width}, Height: {loc.height}")

#     for loc in button_locations:
#         x, y = pyautogui.center(loc)
#         pyautogui.click(x, y)
#         break  # Click the first match

# else:
#     print("Copy Button Not Found!")