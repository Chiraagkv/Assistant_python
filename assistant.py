from __future__ import print_function
import subprocess
import wolframalpha
import playsound
from PyPDF2 import PdfFileReader
from googlesearch import search
import json
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
import requests
from gtts import gTTS
import cv2
from clint.textui import progress
from urllib.request import urlopen
import re
import urllib.parse
import pickle
import os.path
mname = "abc"
num = 0

name = "aunty"
def say(out_say):
    global num
    num += 1
    print(f"{name}: {out_say}")
    tosay = gTTS(text=out_say, lang='en-US', slow=False)
    file = str(num) + ".mp3"
    tosay.save(file)
    playsound.playsound(file, True)
    os.remove(file)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        say("Good Morning Sir !")
    elif hour >= 12 and hour < 18:
        say("Good Afternoon Sir !")

    else:
        say("Good Evening Sir !")

    say("I am your Assistant, " + name)

 
def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f'{query}')

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def suggest():
    f = open("project\\namelist.txt", "r")
    names = f.read()
    say("Is one of these you names?")
    say(names)
    uname = take_command()
    say("Welcome " + uname)
    f = open("project\\namelist.txt", "a+")
    fi = open("project\\namelist.txt", "r")
    names_check = fi.read()
    a = names_check.split(", ")
    if uname.title() in a:
        f.write("")
        f.close()
    else:
        f.write(", ")
        f.write(uname)
        f.close()


def usrname():
    say("What should I call you sir?")
    s_name = ""
    global uname
    uname = s_name
    uname += take_command()
    if uname == "None":
        suggest()
    else:
        say("Welcome " + uname)
        f = open("project\\namelist.txt", "a+")
        fi = open("project\\namelist.txt", "r")
        names_check = fi.read()
        a = names_check.split(", ")
        if uname.title() in a:
            f.write("")
            f.close()
        else:
            f.write(", ")
            f.write(uname)
            f.close()

    say("How can I Help you, Sir")


def send_email(to, content, sender_id, password_sender):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_id, password_sender)
    server.sendmail(sender_id, to, content)
    server.quit()





def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        # get the first page
        page = pdf.getPage(1)
        print(page)
        print('Page type: {}'.format(str(type(page))))
        text = page.extractText()
        return text

if __name__ == "__main__":
    try:
        clear = lambda: os.system('cls')

        # This Function will clean any
        # command before execution of this python file
        clear()
        wishMe()
        usrname()

        while True:

            query = take_command().lower()

            # All the commands said by user will be
            # stored here in 'query' and will be
            # converted to lower case for easily
            # recognition of command
            if f"{name} wikipedia" in query:
                try:
                    say("what do you want to search?")
                    q1 = take_command()

                    say("I am searching for " + q1)
                    say(wikipedia.summary(q1, sentences=4))
                except wikipedia.exceptions.PageError:
                    say("no results found!")
            elif f"{name} plsy youtube" in query:
                query_string = urllib.parse.urlencode({"search_query" : take_command()})
                html_content = urlopen("http://www.youtube.com/results?"+query_string)
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                print("http://www.youtube.com/watch?v=" + search_results[0])
                webbrowser.open_new("http://www.youtube.com/watch?v={}".format(search_results[0]))

            elif f"{name} open youtube" in query:
                say("what do you want to see?")
                q = take_command()
                webbrowser.open_new("https://www.youtube.com/results?search_query="+q)

            elif f"{name} open google" in query:
                say("What should I search for")
                q = take_command()
                q = q.replace("my", uname)
                say("Here you go to Google\n")
                webbrowser.open("https://www.google.com/search?q=" + '+' + q)
            elif f"{name} open stackoverflow" in query:
                say("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("stackoverflow.com")
            elif f"{name} set alarm" in query:
                stop = False
                alarm_time = input("enter time(hh:mm:ss.msmsms): ")
                while not stop:
                    rn = str(datetime.datetime.now().time())
                    say(rn)
                    if rn == alarm_time:
                        stop = True
                        say("get up!")
            elif f"{name} search google" in query:
                say("what do you want to search?")
                q = take_command()
                n = int(input("enter the number of websites you want to open: "))
                for i in search(q, num=n, stop=1, pause=2):
                    print(search(q, num=n, stop=n, pause=2))
                    webbrowser.open_new(i)
            elif f"{name} code" in query:
                file = os.startfile(r"C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad")
                file.write(take_command)
            elif f"{name} calculator" in query:
                os.startfile(r"%windir%\system32\calc.exe")

            elif f"{name} play music" in query or "sharon play song" in query:
                say("Here you go with music")
                # music_dir = "G:\\Song"
                music_dir = "D:\movies\songs"
                songs = os.listdir(music_dir)
                say("what is the song number, Sir?")
                song = int(input("What is the song number, Sir? "))
                random = os.startfile(os.path.join(music_dir, songs[song + 1]))

            elif f"{name} read" in query:
                path = 'instructions.pdf'
                text = text_extractor(path)
                say(text)

            elif "None" in query:
                say("Do you wish to continue?")


            elif f"{name} date and time" in query:
                now = datetime.datetime.now()
                say("Current date and time")
                say(now.strftime("%Y-%m-%d %H:%M:%S"))

            elif f"{name} send a mail" in query:
                try:
                    say("What should I print?")
                    content = take_command()
                    say("whom should i send")
                    to = input("> ")
                    sender_id = input("> ")
                    password_sender = input("> ")
                    send_email(to, content, sender_id, password_sender)
                    say("Email has been sent !")
                except Exception as e:
                    say("I am not able to send this email")

            elif f"{name} how are you" in query:
                say("I am fine, Thank you")
                say("How are you, Sir")

            elif f"{name} fine" in query or f"{name} good" in query:
                say("It's good to know that your fine")

            elif f"{name} change my name to" in query:
                query = take_command()
                uname = query

            elif f"{name} change your name" in query:
                say("What would you like to call me, Sir ")
                name = take_command()
                say(f"Thanks for naming me as {name}")

            elif f"{name} what's your name" in query or f"{name} what is your name" in query:
                say("My friends call me")
                say(name)

            elif f"{name} exit" in query:
                say("Thanks for giving me your time")
                exit()
            elif f"{name} open website" in query:
                site = take_command()
                webbrowser.open("https://www." + site)

            elif f"{name} who made you" in query or f"{name} who created you" in query:
                say("I have been created by {mname}.")

            elif f"{name} joke" in query:
                say(pyjokes.get_joke())

            # elif "calculate" in query:
            # app_id= "K4X6YT-VRVY4VRE37"
            # client = wolframalpha.Client(app_id)

            # indx = input.split().index('calculate')
            # query = input.split()[indx + 1:]
            # res = client.query(' '.join(query))
            # answer = next(res.results).text
            # assistant_says("The answer is " + answer)

            elif f"{name} search" in query or f"{name} play" in query:

                query = query.replace("search", "")
                query = query.replace("play", "")
                webbrowser.open(query)

            elif f"{name} who i am" in query:
                say("If you talk then definately your human.")


            elif f"{name} why did you come to the world" in query:
                say("Serving humanity is my only goal")
            elif f"{name} excel" in query:
                os.startfile(
                    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Excel 2007.lnk")
            elif f"{name} word" in query:
                os.startfile(
                    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007.lnk")
            elif f"{name} ppt" in query:
                os.startfile(
                    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office PowerPoint 2007.lnk")
            elif f"{name} onenote" in query:
                os.startfile(
                    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office OneNote 2007.lnk")

            elif f"{name} is love" in query:
                say("It is 7th sense that destroys all other senses")

            elif f"{name} who are you" in query:
                say("I am a virtual assistant created by {mname}")

            elif f"{name} reason for your existence" in query:
                say("I was created as a project by {mname}, my boss ")

            elif f"{name} change background" in query:
                ctypes.windll.user32.SystemParametersInfoW(20,
                                                           0,
                                                           "Location of wallpaper",
                                                           0)
                say("Background changed succesfully")

            elif f"{name} open bluestack" in query:
                appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
                os.startfile(appli)
            elif f"{name} open pycharm" in query:
                os.startfile(
                    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2019.3.4.lnk")

            elif f"{name} news" in query:

                try:
                    jsonObj = urlopen(
                        '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                    data = json.load(jsonObj)
                    i = 1

                    say('here are some top news from the times of india')
                    print('''=============== TIMES OF INDIA ============''' + '\n')

                    for item in data['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        say(str(i) + '. ' + item['title'] + '\n')
                        i += 1
                except Exception as e:

                    print(str(e))


            elif f"{name} lock window" in query:
                say("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif f"{name} shutdown" in query:
                say("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

            elif f"{name} empty recycle bin" in query:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                say("Recycle Bin Recycled")

            elif f"{name} don't listen" in query or "stop listening" in query:
                say("for how much time you want to stop me from listening commands")
                a = int(input())
                time.sleep(a)

            elif f"{name} where is" in query:
                query = query.replace("where is", "")
                location = query
                say("User asked to Locate")
                say(location)
                webbrowser.open("https://www.google.com/maps/place/" + location + "")

            elif f"{name} camera" in query:
                camera = cv2.VideoCapture(1)
                i = 0
                while i < 10:
                    input('Press Enter to capture')
                    return_value, image = camera.read()
                    photo = cv2.imwrite('Photo ' + str(time.asctime(time.localtime(time.time()))) + '.jpg', image)
                    i += 1

                del (camera)

            elif f"{name} restart" in query:
                subprocess.call(["shutdown", "/r"])

            elif f"{name} hibernate" in query or "sharon sleep" in query:
                say("Hibernating")
                subprocess.call("shutdown / h")

            elif f"{name} log off" in query or "sharon sign out" in query:
                say("Make sure all the application are closed before sign-out")
                time.sleep(2)
                subprocess.call(["shutdown", "/l"])

            elif f"{name} write a note" in query:
                say("What should i write, sir")
                note = take_command()
                file = open('karen.txt', 'w')
                say("Sir, Should i include date and time")
                snfm = take_command()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                    say('noted')
                else:
                    file.write(note)
                    say('noted')

            elif f"{name} show note" in query:
                say("Showing Notes")
                file = open("karen.txt", "r")
                say(file.read(6))

            elif f"{name} update assistant" in query:
                say("After downloading file please replace this file with the downloaded one")
                url = '# url after uploading file'
                r = requests.get(url, stream=True)

                with open("Voice.py", "wb") as Pypdf:

                    total_length = int(r.headers.get('content-length'))

                    for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                           expected_size=(total_length / 1024) + 1):
                        if ch:
                            Pypdf.write(ch)

                            # NPPR9-FWDCX-D2C8J-H872K-2YT43

            elif f"{name} recive email" in query:
                # recieve()
                pass

            elif f"{name} weather" in query:

                # Google Open weather website
                # to get API of Open weather
                api_key = "Api key"
                base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
                say(" City name ")
                city_name = take_command()
                complete_url = base_url + "appid =" + api_key + "&q =" + city_name
                response = requests.get(complete_url)
                x = response.json()

                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    say(" Temperature (in kelvin unit) = " + str(
                        current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                        current_pressure) + "\n humidity (in percentage) = " + str(
                        current_humidiy) + "\n description = " + str(weather_description))

                else:
                    say(" City Not Found ")


            elif f"{name} good morning" in query:
                say("A warm morning. How are you Sir?")

            # most asked question from google Assistant

            elif f"{name} how are you" in query:
                say("I'm fine, glad you asked me that")

            elif f"{name} calculate" in query:
                app_id = "K4X6YT-VRVY4VRE37"
                client = wolframalpha.Client(app_id)

                indx = query.split().index('calculate')
                q = query.split()[indx + 1:]
                res = client.query(' '.join(q))
                answer = next(res.results).text
                say("The answer is " + answer)

            elif f"{name} what can you do" in query:
                say("""I can search in google, play a video on youtube, do your maths, get you answers from wikipedia and most
    importantly learn to do more as you improvise the code.""")

            elif f"{name} exit" in query:
                say("Farewell, Sir")
                exit()

            elif f"{name} open pypi" in query:
                say("which package do you wish to search for?")
                package = take_command()
                say("here you go to pypi\n")
                webbrowser.open("https://pypi.org/search/?q=" + package)
                # spell pypi as peepee while saying the above command

            # elif "what is ai" in query:
            # speak = [
            #   "Artificial Intelligence is the branch of engineering and science devoted to constructing machines that think.",
            #  "AI is the field of science which concerns itself with building hardware and software that replicates the functions of the human mind."]
            # out = random.choice(speak)
            # say(out)
            # elif "are you sentient?" in query:
            #   speak = ["sort of.", "By the strictest dictionary definition of the word 'sentience', I may be.",
            #           "Even though I'm a construct I do have a subjective experience of the universe, as simplistic as it may be."]
            # out = random.choice(speak)
            # say(out)
            elif f"hello {name}" in query:
                say("Hi sir. Do you have time for a chat?")
                response = take_command()
                if response.lower() == "yes":
                    try:
                        d = {}
                        with open("project\\chat.txt") as f:
                            for line in f:
                                key, val = line.split("=")
                                d[key] = val
                        say("how are you sir?")
                        while True:
                            spoken = take_command().lower()
                            if spoken == "bye":
                                say("do you want me to exit?")
                                if take_command().lower() == "yes":
                                    exit()
                                else:
                                    say("bye")
                                    break
                            else:
                                try:
                                    to_say = d.get(spoken)
                                    say(to_say)
                                except Exception:
                                    string = f"should I add {spoken} to my chat data?"
                                    say(string)
                                    reply = take_command().lower()
                                    if reply == "yes":
                                        say("what will be the suitable answer?")
                                        a = take_command()
                                        with open("project\chat.txt", "a") as file:
                                            file.write(spoken)
                                            file.write(":")
                                            file.write(a)
                    except Exception as e:
                        say(e)
    except Exception as error:
        say(error)
