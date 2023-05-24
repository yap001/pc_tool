import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode without a visible browser window
driver = webdriver.Chrome(options=chrome_options)
def capture_screenshot():
    pyautogui.screenshot("screenshot.png")  # Capture the screenshot and save it as "screenshot.png"
while True:
    driver.get("https://example.com")  # Replace with the URL of the webpage you want to monitor
    time.sleep(5)  # Wait for 5 seconds (adjust as needed)
    capture_screenshot()
