import pyttsx3
import os

pyttsx3.speak("hi there you can chat with me as per your requirements")
print()

while True:
    pyttsx3.speak('what do you want me to do?')
    print("chat with me as per your requirements: ",end='')
    p=input()
    if (("run" in p) or ("launch" in p) or ("execute"in p) or ("open" in p)) and ("notepad"in p):
        pyttsx3.speak("opening notepad")
        os.system("notepad")
        
    elif(("run" in p)or("launch" in p)or("execute"in p)or("open" in p)) and ("wmplayer"in p):
        pyttsx3.speak("opening wmplayer")
        os.system("wmplayer")
        
    elif(("run" in p)or("launch" in p)or("execute"in p)or("open" in p)) and ("chrome"in p):
        pyttsx3.speak("opening chrome")
        os.system("chrome")
        
    elif(("run" in p)or("launch" in p)or("execute"in p)or("open" in p)) and ("BurpSuite"in p): 
        pyttsx3.speak("opening burpsuit")
        os.system("BurpSuiteCommunity")
        
    elif(("run" in p)or("launch" in p)or("execute"in p)or("open" in p)) and ("calculator" in p): 
        pyttsx3.speak("opening calculator")
        os.system("calc")
        
    elif(("run" in p)or("launch" in p)or("execute"in p)or("open" in p)) and ("prompt"in p): 
        pyttsx3.speak("opening command prompt")
        os.system("cmd")
        
    elif(("run" in p)or("launch" in p)or("execute"in p)or("open" in p)) and ("BurpSuite"in p): 
        pyttsx3.speak("opening burpsuit")
        os.system("BurpSuiteCommunity")
        
    elif("exit"in p)or("quit"in p):
        pyttsx3.speak("thank you i am sure developer will add more features later to me")
        break
    else:
        print("invalid request")
print()
