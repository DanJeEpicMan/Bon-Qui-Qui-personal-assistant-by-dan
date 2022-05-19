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

r = sr.Recognizer()

winsound.Beep(500,1000) # if you dont like how lowed it is change you system sound level

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
                if keyWord.lower() in text.lower():
                    winsound.Beep(1000,100)
                    print('Keyword detected in the speech.')
                    if google_var1 in text.lower():
                        print(text)
                        res = text.partition(google_split)[2]
                        for j in search(res, tld="co.in", num=1, stop=1, pause=2):
                            if google_var2 in text:
                                print("var2 active")
                                res = text.partition(google_var2)[2]
                                for j in search(res, tld="co.in", num=1, stop=1, pause=2):
                                    print(j)
                                    webbrowser.get('chrome').open(j)
                                    time.sleep(2)
                                    print(width2, width_tab, height)
                                    hwnd = win32gui.GetForegroundWindow()#          xpos ypos width hight importance
                                    win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,width2,0,width_tab,height,0)
                                    print("done")
                                    os.system('python main.py')
                            else:
                                print("opening ", j)
                                webbrowser.get('chrome').open(j)
                                os.system('python main.py')

                
                    if "bon qui qui close tab" in text:
                        print("closeing")
                        os.system('TASKKILL /IM chrome.exe /F')
                
                    if "bon qui qui type" in text:
                        print("typing")
                        typed = text.partition("type ")[2]
                        pyautogui.write(typed)
                        continue

                    if text == "bon qui qui open spotify":
                        os.system(r"start shortcuts\short_spotify.lnk")
                        continue

                    if text == "bon qui qui open discord":
                        os.system(r"start shortcuts\short_discord.lnk")
                        continue
    
                    if text == "bon qui qui open steam":
                        os.system(r"start shortcuts\short_steam.lnk")
                        continue

                    if text == "bon qui qui open csgo":
                        os.system(r"start shortcuts\short_csgo.url")
                        continue
                
                    if text == "bon qui qui open deep rock galactic":
                        os.system(r"start shortcuts\short_drg.url")
                        continue

                    if text == "bon qui qui open minecraft":
                        os.system(r"start shortcuts\short_minecraft.lnk")
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
