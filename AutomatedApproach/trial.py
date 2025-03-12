from ollama import chat
from ollama import ChatResponse
# from src import updatedUtils

# def retreive_entity():
#     response: ChatResponse = chat(model='llama3.2:1b', messages=[
#     {
#         'role': 'user',
#         # 'content': f"""Write python code to generate a solid sphere in freeCAD software.
#         'content': f"""What is photosynthesis?
#         """
#     },
#     ])
#     # print(response['message']['content'])
#     # or access fields directly from the response object
#     r = response.message.content
#     return r

# print(retreive_entity()+'some special thing')

# import pyautogui
# import time

# # Open Spotlight Search
# pyautogui.hotkey("command", "space")
# time.sleep(0.5)  # Wait for the search bar to appear

# # Type "ChatGPT"
# pyautogui.write("ChatGPT", interval=0.1)   ChatGPT
# time.sleep(0.5)  # Give it time to display results

# # Press Enter to open ChatGPT
# pyautogui.press("enter")

import pyautogui
import time
import pyperclip
import logging
import os
import pytesseract
from PIL import Image

user_query = "A H-shaped beam with a height of 100mm, arm lengths of 50mm each, and a thickness of 10mm."

# Open Spotlight Search (Command + Space)
pyautogui.keyDown("command")
time.sleep(0.1)  # Short delay for reliability
pyautogui.press("space")
time.sleep(0.1)  # Let Spotlight open
pyautogui.keyUp("command")

# Type "ChatGPT"
time.sleep(0.5)  # Wait for Spotlight to fully appear
pyautogui.write("ChatGPT", interval=0.1)

# Press Enter to open it
time.sleep(0.5)
pyautogui.press("enter")


print("Move your mouse to the message bar and wait for 5 seconds...")
pyautogui.sleep(5)  # Gives you time to move the mouse
print("Current mouse position:", pyautogui.position())  # Prints the X, Y coordinates

# Move the cursor to the bottom of the screen (adjust as needed)
pyautogui.moveTo(383, 822)  # X and Y coordinates (change based on your screen resolution)
pyautogui.click()  # Click to activate the message bar
pyautogui.write(f"Write python code to generate a freeCAD model of the following user query: {user_query} Return code on the side in the code interpreter", interval=0.001)
pyautogui.press("enter")

# pyautogui.sleep(10)  # Gives you time to move the mouse
# current_position = pyautogui.position()
# print("Current mouse position:", current_position)  # Prints the X, Y coordinates

# position = pyautogui.locateCenterOnScreen("/Users/krishhashia/Desktop/copy_button.png")  # Find center of the element

# if position:
#     print(f"Element found at: {position}")  # Prints (x, y)
#     pyautogui.click(position)  # Clicks on it
# else:
#     print("Element not found!")

# # find copy button and click on it. paste the contents into a new file

# current_index = 0
# macro_file_path = f'Query_{current_index}.FCMacro'
# with open(macro_file_path, 'w') as macroFile:
#     macroFile.write(pyperclip.paste())
# # pyautogui.press('command', 'v')


# # pyautogui.moveTo(current_position)
# # time.sleep(25)
# # pyautogui.click()

# # updatedUtils.gui_sequence(macro_file_path)

# def gui_sequence(macro_code_path, img_path, platform='mac'):
#     """
#     Runs the entire sequence -- opening FreeCAD, running generated code, capturing the isometric image,
#     returning the error code if there is any (macOS version).
#     """
#     if platform == 'mac':
#     # Open FreeCAD using Spotlight
#         pyautogui.hotkey('command', 'space')
#         time.sleep(0.5)
#         pyautogui.typewrite('FreeCAD')  
#         time.sleep(0.5)
#         pyautogui.press('enter')  
#         logging.info('Opened FreeCAD software')
#         time.sleep(8)
        
#         # Open the macro file
#         pyautogui.hotkey('command', 'o')  # macOS uses 'command' instead of 'ctrl'
#         time.sleep(3)
#         pyautogui.write(macro_code_path, interval=0.08)
#         time.sleep(3)
#         pyautogui.press('enter')
#         logging.info('Opened the macros')
#         time.sleep(1)
        
#         # Run the macro
#         pyautogui.hotkey('fn', 'f6')  # macOS may require 'fn' to access function keys
#         time.sleep(2)
        
#         # Set isometric view
#         pyautogui.hotkey('v', 'f')
#         time.sleep(1)
#         pyautogui.hotkey('0')
#         time.sleep(1)
        
#         # Capture a screenshot of the relevant region
#         screenshot = pyautogui.screenshot(region=(543, 147, 1050, 675))  # Adjust region for macOS
#         screenshot.save(img_path)
        
#         # Clear clipboard
#         pyperclip.copy('')
        
#         # Copy error messages from FreeCAD console (adjust coordinates if needed)
#         pyautogui.moveTo(1278, 929)
#         pyautogui.leftClick()
#         pyautogui.hotkey('command', 'a')
#         pyautogui.hotkey('command', 'c')
        
#         error_msg = pyperclip.paste()
#         time.sleep(2)
        
#         # Kill FreeCAD application
#         pyautogui.hotkey('command', 'space')
#         time.sleep(0.5)
#         pyautogui.typewrite('Terminal')
#         pyautogui.press('enter')
#         time.sleep(1)
#         pyautogui.write("pkill FreeCAD", interval=0.08)
#         pyautogui.press("enter")
#         time.sleep(1)
#         pyautogui.hotkey('command', 'q')  # Close Terminal

# gui_sequence(macro_file_path, f'/Users/krishhashia/LAD-LAM/ImageBasedApproach/results/{current_index}_final_output.png')

# import pyautogui
# import time
# import pyperclip
# import os
# import logging

# # Open Spotlight Search (Command + Space)
# pyautogui.hotkey("command", "space")
# time.sleep(0.5)

# # Type "ChatGPT"
# pyautogui.write("ChatGPT", interval=0.1)
# time.sleep(0.5)
# pyautogui.press("enter")

# # Wait for user to move mouse to message bar
# print("Move your mouse to the message bar and wait for 5 seconds...")
# time.sleep(5)
# print("Current mouse position:", pyautogui.position())

# # Move and click on message bar
# pyautogui.moveTo(383, 822)  # Adjust based on your screen
# pyautogui.click()
# pyautogui.write("Write python code to generate a freeCAD model of a ring with three square holes.", interval=0.01)
# pyautogui.press("enter")

# Wait and find the copy button
time.sleep(25)
pyautogui.moveTo(1280, 67)
pyautogui.click()

# Take a screenshot
# screenshot = pyautogui.screenshot()

# # Extract text from image
# text = pytesseract.image_to_string(screenshot)

# # Find location of the text
# if "Copy" in text:
#     x, y = pyautogui.locateCenterOnScreen("/Users/krishhashia/Desktop/copy_button.png")
#     pyautogui.click(x, y)
# pyautogui.click()
# position = False
# try:

#     position = pyautogui.locateCenterOnScreen("/Users/krishhashia/Desktop/copy_button.png")
# except pyautogui.ImageNotFoundException:
#     secondPosition = pyautogui.locateCenterOnScreen("/Users/krishhashia/Desktop/copy_button2.png")

# if secondPosition:
#     pyautogui.click(position)
# elif position:
#     pyautogui.click(secondPosition)
# else:
#     print("Copy button not found!")

# Write copied text to a unique macro file
current_index = 0
while os.path.exists(f'Query_{current_index}.FCMacro'):
    current_index += 1

macro_file_path = f'Query_{current_index}.FCMacro'
temporary_storage = pyperclip.paste()
with open(macro_file_path, 'w') as macroFile:
    macroFile.write(temporary_storage)

# Function to run FreeCAD macro
def gui_sequence(macro_code_path, img_path, platform='mac'):
    if platform == 'mac':
        pyautogui.hotkey('command', 'space')
        time.sleep(0.5)
        pyautogui.write('FreeCAD')  
        time.sleep(0.5)
        pyautogui.press('enter')  
        time.sleep(8)
        
        # Open the macro file
        # pyautogui.hotkey('command', 'o')  
        # pyautogui.moveTo(600,216)
        # pyautogui.click()
        # # time.sleep(3)
        # # pyautogui.write(macro_code_path, interval=0.08)
        # # time.sleep(3)
        # pyautogui.press('enter')
        
        
        pyautogui.moveTo(487,86)
        pyautogui.click()
        pyautogui.moveTo(977,333)
        pyautogui.click()
        pyautogui.write(f'executableMacro{current_index}')
        pyautogui.press('enter')

        time.sleep(2)

        pyautogui.write(temporary_storage)
        # pyperclip.paste()
        pyautogui.click((507,67))
        # pyautogui.hotkey('fn', 'f6')  
        time.sleep(2)

        # pyautogui.hotkey('command', '-')

        # Set isometric view
        pyautogui.hotkey('v', 'f')
        # time.sleep(1)
        pyautogui.hotkey('4')
        # pyautogui.hotkey('0')
        time.sleep(1)
        
        # Capture a screenshot
        screenshot = pyautogui.screenshot(region=(543, 147, 1050, 675))
        screenshot.save(img_path)
        
        # Copy error messages from FreeCAD console
        pyautogui.moveTo(1278, 929)
        pyautogui.click()
        pyautogui.hotkey('command', 'a')
        pyautogui.hotkey('command', 'c')
        error_msg = pyperclip.paste()
        
        # Kill FreeCAD
        os.system("pkill FreeCAD &")

        print(error_msg if error_msg is not None else 0)

# Run the sequence
full_macro_file_path = '/Users/krishhashia/LAD-LAM/'+macro_file_path
time.sleep(1)
# /Users/krishhashia/LAD-LAM/Query_2.FCMacro
gui_sequence(full_macro_file_path, f'/Users/krishhashia/LAD-LAM/ImageBasedApproach/results/{current_index}_final_output.png')