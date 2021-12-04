import speech_recognition as sr
import threading
import time
import tkinter as tk
import os
from tkinter import filedialog
from pydub import AudioSegment
from pydub.silence import split_on_silence

root = tk.Tk()
root.withdraw()
    
def SpeechTimer(delay ):
    intDelay = int(delay)-1
    while intDelay >0:
        print(intDelay)
        intDelay -= 1
        time.sleep(1)
    print("Finished...")
def AudioFileSelector():
    file = filedialog.askopenfilename(filetypes=[("Wav Files", "*.wav")])
    print(file)
    return file;
        
def MicRecogniser(delay):
    intDelay = int(delay)
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            
            print("Assessing Ambient Noises...")
            r.adjust_for_ambient_noise(source)
            
            print("Listening...")
            TimerThread = threading.Thread(target=SpeechTimer, args=(delay, ))
            TimerThread.start()

            
            audio_data = r.record(source, duration=intDelay)
            print("Transcribing Audio...")
            text = r.recognize_google(audio_data)
            print("Transcribing Completed...")
            print(text)
    except sr.UnknownValueError:
        print("ERROR: Unable to recognise speech")
    except r.UnknownValueError:
        print("ERROR: API unavailable")
    
if __name__ == "__main__":
    delay = input("How many seconds should we record you for?: ")

    MicRecogniser(delay)
    
    