import requests
import zipfile
import os

def download_chromedriver():
    version = requests.get('https://chromedriver.storage.googleapis.com/LATEST_RELEASE').text.strip()
    url = f'https://chromedriver.storage.googleapis.com/{version}/chromedriver_win32.zip'
    response = requests.get(url)
    with open('chromedriver_win32.zip', 'wb') as f:
        f.write(response.content)
    with zipfile.ZipFile('chromedriver_win32.zip', 'r') as zip_ref:
        zip_ref.extractall('chromedriver')

if __name__ == "__main__":
    download_chromedriver()
