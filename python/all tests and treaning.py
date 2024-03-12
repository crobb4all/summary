from selenium import webdriver
from bs4 import BeautifulSoup

# URL of the web page you want to scrape
url = 'https://www.gismeteo.ru/weather-batumi-5275/'

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the web page
driver.get(url)

# Get the page source
page_source = driver.page_source

# Close the WebDriver
driver.quit()

# Parse the page source using BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Now you can use BeautifulSoup to navigate and extract data from the page
# For example, find all links on the page
specific_element = soup.find('div', class_='page-title').text

date = soup.find('div', class_='date').text

# sign = soup.find('span', class_='sign').text

temperature = soup.find('div', class_='weather-value').text
print(specific_element, date, temperature)
