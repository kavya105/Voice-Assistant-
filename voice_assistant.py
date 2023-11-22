import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice' , voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
            speak("Good Morning")
    elif hour>=12 and hour<18:
            speak("Good afternoon") 
    else:
            speak("Good Evening")      

    speak("I'm Jarvis Mam please tell me how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"User said = {query}\n")

    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.ccom' , 'your_password')
    server.sendmail('youremail@gmail.com' , to , content)
    server.close()

def Whatsapp():
     speak("Tell me the name of the person")
     name = takeCommand()

     if 'khushi' in name:
          speak("Tell me the message")
          msg = takeCommand()
          speak("Tell me the time sir")
          speak("time in hour")
          hour = int(takeCommand())
          speak("Time in minute")
          min  =int(takeCommand())
          pywhatkit.sendWhatmsg("+91 70551 70841" , msg , hour , min , 10)
          speak("Sending WhatsApp Message.........")

     else:
          speak("Tell me the number")
          phone = int(takeCommand())
          ph = '+91'+ phone
          speak("Tell me the message")
          msg = takeCommand()
          speak("Tell me the time sir")
          speak("time in hour")
          hour = int(takeCommand())
          speak("Time in minute")
          min  =int(takeCommand())
          pywhatkit.sendWhatmsg("phone" , msg , hour , min , 10)
          speak("Sending WhatsApp Message.........")
             


if __name__ == "__main__":
    
    wishMe()
   
    if 1: 
     query = takeCommand().lower()
 
     if 'wikipedia' in query:
        speak("Searching Wikipedia....")
        query = query.replace("wikipedia" , "")
        results = wikipedia.summary(query , sentences = 2)
        speak("Accoring to the wikipedia")
        print(results)
        speak (results)

     elif 'open youtube' in query:
           webbrowser.open("youtube.com")

     elif 'open Google' in query:
           webbrowser.open("google.com") 

     elif 'website' in query:
                speak("Ok sir , Launching.....")
                query = query.replace("jarvis" , "")
                query = query.replace("website" , "")
                web1  = query.replace("open" , "")
                web2 = "https://www." + web1 +'.com' 
                webbrowser.open(web2)
                speak("Launched")
                


     elif 'launch' in query:
          speak('Tell me the name of the website')
          name = takeCommand()
          web = 'https://www.'  + name +'.com'
          webbrowser.open(web)
          speak("Done sir!")

     elif 'the time'  in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        print(strTime)  
        speak(f"The time is {strTime}")    

     elif 'open code' in query:
        codePath = "C:\\Users\\kavya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
        os.startfile(codePath)


     elif 'Whatsapp Message' in query:
      Whatsapp()    

     elif 'email to kavya' in query:
         try:
            speak("what should I say")
            content = takeCommand()
            to = "kavyarastogi910@gmail.com"
            sendEmail = (to , content)
            speak("Email has been sent")
         except Exception as e:
            print(e)
            speak("Sorry I'm not able to sent the email")
