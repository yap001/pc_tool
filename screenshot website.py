from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without opening a browser window)

# Provide the path to your ChromeDriver executable
driver_path = "path/to/chromedriver"

# Create a new Chrome WebDriver instance
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# Define the URL of the website to capture screenshots
website_url = "https://www.example.com"

# Navigate to the website
driver.get(website_url)

# Set the initial window size (optional)
driver.set_window_size(1366, 768)

# Capture a screenshot of the initial page
driver.save_screenshot("screenshot_1.png")

# Scroll to the bottom of the page to load additional content (optional)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Capture a screenshot of the scrolled page
driver.save_screenshot("screenshot_2.png")

# Repeat the scrolling and capturing process as needed to cover the entire page

# Close the WebDriver instance
driver.quit()
