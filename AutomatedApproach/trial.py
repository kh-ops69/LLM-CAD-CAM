from ollama import chat
from ollama import ChatResponse
import random
import pyautogui
import time
import pyperclip
import logging
import os
import pytesseract
from PIL import Image

# uq = "A H-shaped beam with a height of 100mm, arm lengths of 50mm each, and a thickness of 10mm."

def return3DRenderingAndCode(user_query, download_dir):

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
    pyautogui.write(f"""Write python code to generate a freeCAD model of the following user query: {user_query.rstrip()}Return code on the side in the code interpreter and ensure model is downloaded in .stl format into the following directory: {download_dir}.""", interval=0.001)
    pyautogui.press("enter")

    # Wait and find the copy button
    time.sleep(30)
    pyautogui.moveTo(1280, 67)
    pyautogui.click()

    # Write copied text to a unique macro file
    current_index = 0
    while os.path.exists(f'Query_{current_index}.FCMacro'):
        current_index += 1

    macro_file_path = f'Query_{current_index}.FCMacro'
    temporary_storage = pyperclip.paste()
    # if isinstance(temporary_storage, str):
    #     additional_code = """stl_filename = "h_beam.stl"\nMesh.export([part], stl_filename)
    #     """
    #     temporary_storage += additional_code
    with open(macro_file_path, 'w') as macroFile:
        macroFile.write(temporary_storage)

    # Function to run FreeCAD macro
    def gui_sequence(img_path, platform='mac'):
        if platform == 'mac':
            pyautogui.hotkey('command', 'space')
            time.sleep(0.5)
            pyautogui.write('FreeCAD')  
            time.sleep(0.5)
            pyautogui.press('enter')  
            time.sleep(8)
            
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
    gui_sequence(f'/Users/krishhashia/LAD-LAM/ImageBasedApproach/results/{current_index}_final_output.png')

with open('data/queries.txt', 'r') as file:
    query_lst = file.readlines()

random_query = query_lst[random.randint(0, len(query_lst)-1)]
return3DRenderingAndCode(random_query, '/Users/krishhashia/LAD-LAM/AutomatedApproach/3D_Downloads/')