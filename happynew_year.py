import time
import pyttsx3 
converter = pyttsx3.init() 
converter.setProperty('rate', 150) 
converter.setProperty('volume', 0.7) 
for i in range(10,0,-1):
    
    print(i)
    converter.say(i) 
    converter.runAndWait()  
    time.sleep(0.5)
z="happy new year"
print(z)
converter.say(z) 
converter.runAndWait() 