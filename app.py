from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import PyPDF2 

driver = webdriver.Chrome("PATH_TO_CHROMEDRIVER") #Replace your path of Chromedriver
driver.implicitly_wait(15)
driver.get("https://www.instagram.com/accounts/login/")

username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")

print(username)
print(password)

username.send_keys("*****") #Replace your username
password.send_keys("*****") #Replace your password

driver.find_element_by_xpath("//button[@type='submit']").click()

direct = driver.find_element_by_xpath("//a[@class='xWeGp']")

link = direct.get_attribute('href')

driver.get(link)

user = driver.find_element_by_xpath("//a[@class='-qQT3 rOtsg']")

driver.execute_script("arguments[0].click();", user)

pdfFileObj = open('*****', 'rb') #Replace your path to a pdf file
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

for i in range(0, pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    text = pageObj.extractText()
    print(text)
    messageBox = driver.find_element_by_xpath("//textarea")
    messageBox.send_keys(text)
