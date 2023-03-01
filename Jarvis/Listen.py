# 1- Selenium Based Speech Recognition
#QC-Check
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_argument('--log-level=3')
#chrome_options.headless = True
PathofDriver = "Driver\\chromedriver.exe"
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic":1})
chrome_options.add_argument("--mute-audio")
driver = webdriver.Chrome(PathofDriver,options=chrome_options)
driver.maximize_window()
driver.get('https://www.google.com/')
def Listen():
    sleep(1)
    print(" Listening........ ")
    driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[2]').click()
    sleep(5)
    voice = driver.title
    query = str(voice).replace(" - Google Search","")
    query = str(query).replace("Google","")
    sleep(1)
    driver.get('https://www.google.com/')
    print(f" You Said : {query}.")
    return query


'''

# 2 - Web Based Speech Recognition (pip install SpeechRecognition)
#QC-Check
'''
import speech_recognition as sr

def Listen():
    r = sr.Recognizer()
    #print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,0,5)
    try:
        print("Recognizing....\n")
        query = r.recognize_google(audio,language="en-in")
        print(f" You : {query}")
    except:
        return " "
    query = str(query)
    return query.lower()
'''
# 3 - Offline Speech Recognition(pip install vosk,pyaudio)
#QC-Check
# https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip

from vosk import Model, KaldiRecognizer
import pyaudio
model = Model("DataBase\\vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
def Listen():
    print("")
    print("Listening...")
    print("")
    while True:
        data = stream.read(4096,exception_on_overflow = False)
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            p = text[14:-3]
            print(f"You Said : {p}")
            if len(p)>0:
                return p        
            else:
                break
