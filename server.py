import os
import random
import subprocess
import tempfile
import time
import pyautogui
import pyperclip
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for local frontend dev or all origins (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directory to save exported 3D models
EXPORT_DIR = os.path.join(os.getcwd(), "3D_Downloads")
os.makedirs(EXPORT_DIR, exist_ok=True)

# FreeCAD Python path replace dependent on your pc
FREECAD_PYTHON = "C:\\Program Files\\FreeCAD 1.0\\bin\\python.exe"

def get_code_from_api(query, export_path):
    pyautogui.hotkey("win", "s")
    time.sleep(0.5)
    pyautogui.write("ChatGPT")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(5)  # Wait for ChatGPT to open

    # Move to the ChatGPT input box
    pyautogui.moveTo(838, 556)
    pyautogui.click()
    time.sleep(0.5)

    pyautogui.hotkey("ctrl"+"a")
    pyautogui.press("backspace")
    
    # Create a specific prompt with explicit STL export path
    prompt = f"""
        Write a Python script for FreeCAD to generate a 3D model based on the user query: {query}.\
        Save the model as an STL file at this exact path: {export_path}.\
        Do NOT use GUI-dependent code. Return the python file in the side view editor so i can run it and test.
        Also points to note, the module 'Mesh' has no attribute 'write' so generate the code keeping this in mind"""
 
    
    pyperclip.copy(prompt)
    pyautogui.hotkey("ctrl", "v")    
    time.sleep(6)
    pyautogui.press("enter")

    # Wait and find the copy button
    time.sleep(30)
    pyautogui.moveTo(1143, 414)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.hotkey("ctrl","a")
    time.sleep(1)
    pyautogui.hotkey("ctrl","c")
    time.sleep(1)

    subprocess.run(["taskkill", "/IM", "ChatGPT.exe", "/F"], shell=True)


    code = pyperclip.paste()
    return code
class QueryModel(BaseModel):
    query: str
def create_script_file(code):
    fd, script_path = tempfile.mkstemp(suffix='.py', text=True)
    with os.fdopen(fd, 'w') as f:
        f.write(code)
    return script_path
@app.post("/3dobj")
def generate_stl(query: QueryModel):
    print(f"Processing query: {query.query}")
    
    timestamp = int(time.time())
    export_path = os.path.join(EXPORT_DIR, f"model_{timestamp}.stl")
    
    freecad_code = get_code_from_api(query.query, export_path)  # Pass export path to the function
    
    script_path = create_script_file(freecad_code)
    
    try:
        result = subprocess.run([FREECAD_PYTHON, script_path], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
            raise HTTPException(status_code=500, detail="Error executing FreeCAD script")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.unlink(script_path)
    time.sleep(5)
    print(export_path)
    if not os.path.exists(export_path):
        raise HTTPException(status_code=500, detail="STL file was not generated")
    
    return FileResponse(export_path, filename=os.path.basename(export_path))
