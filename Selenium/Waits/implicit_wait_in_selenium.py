from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(10)

e_title = "Demo Guru99 Page"
a_title = ""

driver.get("http://demo.guru99.com/test/guru99home/")

a_title = driver.title

if e_title == a_title:
    print('Test Passed')
else:
    print('Test Failed')

driver.quit()