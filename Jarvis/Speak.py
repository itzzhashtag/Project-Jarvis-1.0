# 1 - Selenium - Framework   (pip install selenium==4.1.3)
# Website - ttsmp3
#QC-Check
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
PathofDriver = "Driver\\chromedriver.exe"
driver = webdriver.Chrome(PathofDriver,options=chrome_options)
driver.maximize_window()
Website = f'https://ttsmp3.com/text-to-speech/British%20English/'
driver.get(Website)
ButtonSelection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')
def Speak(Text):
    print("")
    print(f" Jarvis : {Text}.")
    print("")
    Data = str(Text)
    xpathtec = '/html/body/div[4]/div[2]/form/textarea'
    driver.find_element(by=By.XPATH, value=xpathtec).send_keys(Data)
    driver.find_element(by=By.XPATH, value='//*[@id="vorlesenbutton"]').click()
    driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/form/textarea').clear()
    sleep(2)



# 2 - Webdriver - Framework
# Website - Natural Readers
#QC-Found issue in this Framework

'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
PathofDriver = "Driver\\chromedriver.exe"
driver = webdriver.Chrome(PathofDriver,options=chrome_options)
driver.maximize_window()

Website = 'https://www.naturalreaders.com/online/'

driver.get(Website)
sleep(2)
#driver.find_element(by=By.XPATH, value='//*[@class="nr-btn btn-flat-blue"]').click()
driver.find_element(by=By.XPATH, value='//*[@id="pw-reading-scroll"]/div[1]/button').click()
driver.find_element(by=By.XPATH, value='//*[@id="pw-reading-page"]/div[1]/div/div[2]/app-pw-reading-bar/div/div/button[1]').click()
sleep(2)
driver.find_element(by=By.XPATH, value='//*[@id="mat-dialog-0"]/app-pw-voices/mat-dialog-content/div/mat-selection-list/mat-list-option[4]/div/div[2]/div/div[1]').click()
driver.find_element(by=By.XPATH, value='//*[@id="mat-dialog-0"]/app-pw-voices/div/div/button').click()

def Speak(Text):
    try:
        driver.find_element(by=By.XPATH, value='//*[@id="pw-reading-scroll"]/div[1]/button').click()
        sleep(1)

    except:
        pass

    Data = str(Text)
    xpathtec = '//*[@id="inputDiv"]'
    driver.find_element(by=By.XPATH, value=xpathtec).click()
    driver.find_element(by=By.XPATH, value=xpathtec).send_keys(Data)
    driver.find_element(by=By.XPATH, value='//*[@id="pw-reading-page"]/div[1]/div/div[2]/app-pw-reading-bar/div/div/button[3]').click()
    sleep(2)

    try:
        driver.find_element(by=By.XPATH, value='//*[@id="pw-reading-scroll"]/div[1]/button').click()
        sleep(1)

    except:
        pass

    print("")
    print(f" AI : {Text}.")
    print("")
'''

# 3 - Pyttsx3 - Module(pip install pyttsx)
# Os Based Speaker
#QC-Check
'''
import pyttsx3 #pip install pyttsx3

def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')

    engine.setProperty('voices',voices[0].id)
    # lengthcode = len(Text)

    # if lengthcode>30:
    #     engine.setProperty('rate',200)

    # else:
    #     engine.setProperty('rate',170)
    engine.setProperty('rate',170)
    print("    ")
    print(f"A.I : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("    ")
'''