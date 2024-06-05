from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import logging

# Set up the logger

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Set up Selenium WebDriver with Chrome

chrome_options = Options()

# Run headless Chrome to avoid opening a browser window

chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Path to the ChromeDriver, which is now in /usr/local/bin/

chrome_driver_path = "/usr/local/bin/chromedriver"
try:
    # Set up the service with the ChromeDriver

    service = ChromeService(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
except Exception as e:
    logger.error(f"Error setting up ChromeDriver: {e}")
    raise

# Access the website

logger.info("Scraping data from Brewers Association website")
driver.get(
    '''https://www.brewersassociation.org/resources/
    brewers-association-beer-style-guidelines/'''
)

# Give time for JavaScript to load if necessary

driver.implicitly_wait(10)

# Get the page source after JavaScript has rendered

soup = BeautifulSoup(driver.page_source, "html.parser")

# Find the beer styles

beer_styles = soup.findAll("ul", attrs={"class": "beer-style-origin-toc"})
styles_data = []
if not beer_styles:
    logger.error(
        '''No beer styles found. The website structure 
        may have changed or content is dynamically loaded.'''
    )
else:
    for beer_style in beer_styles:
        origin = beer_style.find("li", class_="origin").text.strip()
        styles = [
            li.text.strip() for li in beer_style.findAll("li",
                                                         class_="style")
        ]
        styles_data.append({"origin": origin, "styles": styles})

# Close the browser

driver.quit()

# Print the extracted data

print(styles_data)
