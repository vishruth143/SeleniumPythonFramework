from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_confirm")

iframe = driver.find_element(By.XPATH, "//iframe[@id='iframeResult']")

driver.switch_to.frame(iframe)

driver.find_element(By.XPATH, "//button[@onclick='myFunction()']").click()

print(Alert(driver).text)

Alert(driver).dismiss()

driver.quit()