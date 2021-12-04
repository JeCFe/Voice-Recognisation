import speech_recognition as sr
import webbrowser as web

if __name__=="__main__":
    path = "C://Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Speak Command")
        audio = r.listen(source)
        print("Recogising...")

        try:
            dest=r.recognize_google(audio)
            destArray = dest.split()
            webDest = destArray[0];
            print(destArray)
            if(destArray[0] == "open"):
                webDest = "www."+destArray[1]+".com"
                web.get(path).open(webDest)
            if(destArray[0] == "Google"):
                fullWord = ""
                destArray.pop(0)
                for x in range(len(destArray)):
                     fullWord += destArray[x] + "+"
                print(fullWord)
                web.get(path).open("www.google.com/search?q="+fullWord)
        except Exception as e:
            print("ERROR: " + str(e))