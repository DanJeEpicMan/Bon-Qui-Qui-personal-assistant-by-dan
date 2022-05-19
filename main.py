#pip install pipwin
#pip install pyaudio #if that does not work do pipwin install pyaudio
#pip install SpeechRecognition
#pip install pyttsx3
#pip install google
#pip install beautifulsoup4
#pip install pyautogui
#pip install pydub
#pip install keyboard
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#| MUST CHANGE SHORTCUTS OR WILL NOT WORK    |
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
import speech_recognition as sr
from googlesearch import search
import webbrowser
import os
import win32gui
import win32con
import time
import keyboard
import pyautogui
import os
import winsound
import threading
import pyttsx3

r = sr.Recognizer()

print("Enable MicMuter (usfull becuase it will stop it from picking up more noise)")
A = input("[y/n]?")

if A == "y":
    os.system('start micmute/mic_mute.exe')
    print('press F8 for to mute mic')

engine = pyttsx3.init()
engine.say('Starting virtual assistant')
engine.runAndWait()

#winsound.Beep(500,1000) # if you dont like how lowed it is change you system sound level

webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe")) #Change this to where your google is located

width, height = pyautogui.size()
width2 = int(width*.66)
width_tab = int(width*.33)

keyWord = 'bon qui qui'
google_var1 = 'bon qui qui google'
google_var2 = 'bon qui qui google and pin'
google_split = 'google '

def mic_detect():
    with sr.Microphone() as source:
        print('Please start speaking..\n')
        while True: 
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                text = text.lower()
                print(text)
                if keyWord.lower() in text.lower():
                    print('Keyword detected in the speech.')
                    if google_var1 in text.lower(): #if google in request
                        if google_var2 in text.lower(): #if pin in google request
                            engine.say('opening and pinning tab')
                            engine.runAndWait()
                            res = text.partition(google_var2)[2] #formatting text
                            for j in search(res, tld="co.in", num=1, stop=1, pause=2): #get website
                                print(j)
                                webbrowser.get('chrome').open(j) #open website
                                time.sleep(1)
                                #pin the page
                                hwnd = win32gui.GetForegroundWindow()#          xpos ypos width hight importance
                                win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,width2,0,width_tab,height,0)
                        else:
                            engine.say('opening tab')
                            engine.runAndWait()
                            res = text.partition(google_var1)[2] #formating text
                            for j in search(res, tld="co.in", num=1, stop=1, pause=2): #getting website
                                webbrowser.get('chrome').open(j) #opening website
                        
                    if "bon qui qui close tab" in text:
                        os.system('TASKKILL /IM chrome.exe /F')
                        engine.say('closing tab')
                        engine.runAndWait()
                        continue
                
                    if "bon qui qui type" in text:
                        engine.say('typing')
                        engine.runAndWait()
                        typed = text.partition("type ")[2]
                        pyautogui.write(typed)
                        continue

                    if text == "bon qui qui open spotify":
                        engine.say('opening spotify')
                        engine.runAndWait()
                        os.system(r"start shortcuts\short_spotify.lnk")
                        continue

                    if text == "bon qui qui open discord":
                        os.system(r"start shortcuts\short_discord.lnk")
                        engine.say('opening discord')
                        engine.runAndWait()
                        continue
    
                    if text == "bon qui qui open steam":
                        os.system(r"start shortcuts\short_steam.lnk")
                        engine.say('opening steam')
                        engine.runAndWait()
                        continue

                    if text == "bon qui qui open csgo":
                        os.system(r"start shortcuts\short_csgo.url")
                        engine.say('opening C S GO')
                        engine.runAndWait()
                        continue
                
                    if text == "bon qui qui open deep rock galactic":
                        os.system(r"start shortcuts\short_drg.url")
                        engine.say('opening D R G')
                        engine.runAndWait()
                        continue

                    if text == "bon qui qui open minecraft":
                        os.system(r"start shortcuts\short_minecraft.lnk")
                        engine.say('opening Minecraft')
                        engine.runAndWait()
                        continue
        
            except Exception as e:
                print('Please speak again.')
#def restart_mic():
    on_var = 1
    while on_var == 1:
        time.sleep(0.4)
        if keyboard.is_pressed('q'):
            quit(mic_detect)

mic_detect()
#t1 = threading.Thread(target=mic_detect)
#t2 = threading.Thread(target=restart_mic)
#t1.start()
#t2.start()
