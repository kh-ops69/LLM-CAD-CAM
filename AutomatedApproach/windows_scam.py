import os
import random
import subprocess
import tempfile
import pyautogui
import time
import pyperclip

# Directory to save exported 3D models
EXPORT_DIR = "C:\\Users\\harsh\\Documents\\LADLAM\\LAD-LAM\\AutomatedApproach\\3D_Downloads"
os.makedirs(EXPORT_DIR, exist_ok=True)

# Path to query file
query_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "queries.txt"))

# FreeCAD Python path
FREECAD_PYTHON = "C:\\Program Files\\FreeCAD 1.0\\bin\\python.exe"
with open(query_file_path, 'r') as file:
    query_lst = file.readlines()

user_query = query_lst[random.randint(0, len(query_lst)-1)]
# Read queries from file
with open(query_file_path, 'r') as file:
    query_lst = file.readlines()
random_query = random.choice(query_lst).strip()

# Ask GPT for a FreeCAD model generation script
def get_code_from_api(query):
    pyautogui.hotkey("win", "s")
    time.sleep(0.5)
    pyautogui.write("ChatGPT")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(5)  # Wait for ChatGPT to open

    # Move to the ChatGPT input box
    pyautogui.moveTo(1215, 879)
    pyautogui.click()
    
    # Create a more specific prompt to ensure STL export
    prompt = f"""
        Write python code to generate a freeCAD model of the following user query: {user_query.rstrip()}. Return code on the side in the code interpreter and save it in the stl format. 

    """
    
    pyautogui.write(prompt, interval=0.001)
    pyautogui.press("enter")

    # Wait and find the copy button
    time.sleep(30)
    pyautogui.moveTo(1679, 56)  # Copy button location in ChatGPT
    time.sleep(2)
    pyautogui.click()
    pyautogui.click()


    pyautogui.moveTo(1893, 12)  # Close button location in ChatGPT
    pyautogui.click()

    code = pyperclip.paste()
    
    print(code)
    return code

def enforce_stl_export(code):
    """Add code to ensure STL export happens even if the AI forgets"""
    
    # Timestamp for unique filenames
    timestamp = int(time.time())
    
    # Backup export code to append if needed
    backup_export = f"""
# Ensure STL export happens
try:
    # Get all objects in the document
    doc = FreeCAD.ActiveDocument
    if not doc:
        doc = FreeCAD.newDocument("BackupExport")
    
    mesh_objs = []
    for obj in doc.Objects:
        if hasattr(obj, "Shape"):
            mesh_obj = doc.addObject("Mesh::Feature", f"Mesh_{obj.Name}")
            mesh_obj.Mesh = Mesh.Mesh(obj.Shape.tessellate(0.1))
            mesh_objs.append(mesh_obj)
    
    # Export to STL
    import Mesh
    export_path = r"{EXPORT_DIR}\\model_{timestamp}_backup.stl"
    Mesh.export(mesh_objs, export_path)
    print(f"Backup STL export completed to {export_path}")
except Exception as e:
    print(f"Backup export failed: {{e}}")
"""
    
    # Check if code already includes STL export functionality
    if "Mesh.export" not in code and ".exportStl" not in code:
        code += backup_export
    
    # Add import for Mesh if not present
    if "import Mesh" not in code:
        code = "import Mesh\n" + code
        
    return code

def create_script_file(code):
    fd, script_path = tempfile.mkstemp(suffix='.py', text=True)
    with os.fdopen(fd, 'w') as f:
        f.write(code)
    return script_path

# Main execution
def main():
    print(f"Using query: {random_query}")
    
    # Get code from API
    freecad_code = get_code_from_api(random_query)
    
    # Create a temporary script file
    script_path = create_script_file(freecad_code)
    
    try:
        # Execute the script with FreeCAD's Python interpreter
        print("Executing FreeCAD script...")
        result = subprocess.run(
            [FREECAD_PYTHON, script_path],
            capture_output=True,
            text=True
        )
        
        # Print output
        print("Script output:")
        print(result.stdout)
        
        if result.stderr:
            print("Errors:")
            print(result.stderr)
            
    except Exception as e:
        print(f"Error executing script: {e}")
    finally:
        # Clean up the temporary file
        os.unlink(script_path)

if __name__ == "__main__":
    main()