# Untested, please refer trial.py for working code (without API integration)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64
import os
from typing import Optional
import random
import time
import pyautogui
import pyperclip
import logging
import glob
from ollama import chat
from ollama import ChatResponse

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    download_dir: str = "/Users/krishhashia/LAD-LAM/AutomatedApproach/3D_Downloads/"

class ResponseModel(BaseModel):
    code: str
    stl_content: str

@app.post("/get_response")
async def get_response(request: QueryRequest):
    try:
        # Store the original query and download directory
        user_query = request.query
        download_dir = request.download_dir
        
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
                pyautogui.click((507,67))
                time.sleep(2)

                # Set isometric view
                pyautogui.hotkey('v', 'f')
                pyautogui.hotkey('4')
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
        gui_sequence(f'/Users/krishhashia/LAD-LAM/ImageBasedApproach/results/{current_index}_final_output.png')
        
        # Find and read the generated STL file
        stl_files = glob.glob(os.path.join(download_dir, "*.stl"))
        stl_content = ""
        
        if stl_files:
            # Get the most recently created STL file
            latest_stl = max(stl_files, key=os.path.getctime)
            with open(latest_stl, 'rb') as stl_file:
                stl_binary = stl_file.read()
                stl_content = base64.b64encode(stl_binary).decode('utf-8')
        
        # Return the code and STL content
        return ResponseModel(
            code=temporary_storage,
            stl_content=stl_content
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

# For random query testing (if needed)
def get_random_query():
    with open('data/queries.txt', 'r') as file:
        query_lst = file.readlines()
    
    return query_lst[random.randint(0, len(query_lst)-1)]

# Run with: uvicorn main:app --reload