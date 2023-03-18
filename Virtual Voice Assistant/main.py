import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import pywhatkit
import pyjokes


print("I'm your personal assistant - Alexa")


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        print("Hello,Good Morning")
        speak("Hello,Good Morning")
    elif hour>=12 and hour<18:
        print("Hello,Good Afternoon")
        speak("Hello,Good Afternoon")
    else:
        print("Hello,Good Evening")
        speak("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            print("Recognizing...")
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            print('Unable to Recognize your voice.')
            speak("Unable to Recognize your voice.")
            return "None"
        return statement
    
    

speak("I'm your personal assistant - Alexa")
wishMe()
print('Tell me how can I help you now?')
speak("Tell me how can I help you now?")


if __name__=='__main__':


    while True:
        
        statement = takeCommand().lower()
        

        if "goodbye" in statement or "bye" in statement or "shutdown" in statement or "okay bye" in statement or "stop" in statement:
            print('Your personal assistant Alexa is shutting down, Good bye')
            speak('Your personal assistant Alexa is shutting down, Good bye')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")
        
        elif 'play' in statement:
            song = statement.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)

        elif 'how are you' in statement:

            print("I am fine, Thank you")
            speak("I am fine, Thank you")
            print("How are you, Sir")
            speak("How are you, Sir")
 

        elif 'fine' in statement or "good" in statement:
            print("It's good to know that your fine")
            speak("It's good to know that your fine")

        elif "where is" in statement:

            statement = statement.replace("where is", "")

            location = statement

            speak("User asked to Locate")

            speak(location)

            webbrowser.open("https://www.google.nl / maps / place/" + location + "")


        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M %p")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            print('I am Alexa version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')
            speak('I am Alexa version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            print("I was built by Aaditya, Vishnu And Prachiti")
            speak("I was built by Aaditya, Vishnu And Prachiti")

        elif 'for date' in statement:   
            speak('Sorry, I have a headache. Ask to Siri, she might come with you')
    
        elif 'are you single' in statement:
            print("yes baby, just like you")
            speak("yes baby, just like you")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'joke' in statement:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            speak(answer)


        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(5)
