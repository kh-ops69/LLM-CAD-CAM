import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver with Chrome in headless mode
chrome_options = Options()
# # chrome_options.add_argument("--headless")  # Run headless so the browser window doesn't open
# chrome_options.add_argument("--no-sandbox")  # Useful for running in CI environments
# chrome_options.add_argument("--disable-dev-shm-usage")  # Another useful flag for CI
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Disable automation detection
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Exclude automation flag
chrome_options.add_experimental_option("useAutomationExtension", False)  # Turn off automation extension

# Set up Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)
def human_delay():
    # Random delay between 1 to 3 seconds to mimic human behavior
    time.sleep(random.uniform(0.1, 0.7))

def input_text():
    # The URL of the website you want to interact with
    url = "https://chatgpt.com"  # Replace with the website you want to scrape
    driver.get(url)

    # Wait for the page to load
    time.sleep(random.uniform(2, 5))

    # Find the contenteditable div element where the text needs to be input
    editable_div = driver.find_element(By.ID, "prompt-textarea")  # The div with contenteditable="true"
    
    # Click on the div to focus it (this simulates a user clicking to focus the text area)
    editable_div.click()
    human_delay()

    # Clear existing content if any (you can skip this if you want to keep the content)
    driver.execute_script("arguments[0].innerHTML = '';", editable_div)

    # Text to input into the contenteditable div
    text_to_input = "This is a test input"
    
    # Simulate typing by sending keys one by one (using ActionChains to simulate human-like input)
    for char in text_to_input:
        editable_div.send_keys(char)
        
        human_delay()  # Mimic human typing speed
    editable_div.send_keys(Keys.BACKSPACE)

    # Wait for the content to be processed (adjust as necessary)
    human_delay()

    # After typing, you can extract the content or perform other actions as needed
    output = editable_div.get_attribute("innerHTML")  # Get the content inside the contenteditable div
    print("Output:", output)
    send_button = driver.find_element(By.XPATH, '//button[@aria-label="Send prompt"]')

    # Click the button
    send_button.click()

    # Wait to observe the result (optional)
    time.sleep(2)
    input("Press Enter to close the browser...")





# Run the input_text function
input_text()
