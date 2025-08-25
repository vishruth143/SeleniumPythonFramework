import time

from selenium import webdriver
import requests

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")  # target practice site

time.sleep(10)

# Collect all <a> elements
links = driver.find_elements("tag name", "a")

print(f"Total links found: {len(links)}")

# Iterate through links
for link in links:
    url = link.get_attribute("href")
    if url is None or url.strip() == "":
        continue  # skip empty hrefs

    try:
        response = requests.head(url, timeout=5)  # HEAD request is faster
        if response.status_code >= 400:
            print(f"❌ Broken Link: {url} --> Status Code: {response.status_code}")
        else:
            print(f"✅ Valid Link: {url} --> Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Could not check link: {url} --> Error: {e}")

driver.quit()