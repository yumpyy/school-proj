#!/usr/bin/env python3

import os
import time

from vosk import Model, KaldiRecognizer, SetLogLevel
import pyaudio


# --- Modules in directory
from myMods.scrappers import wttr, word, yt, gptRespond


def weatherWordCheck(text):
    weatherWords = ['weather', 'temprature', '']
    for word in text:
        if word in weatherWords:
            return True
    return False


# --- Variable Set
SetLogLevel(0)

# ----- Transc and TTS set
ttsModel="./models/model2.onnx"
transcModel="vosk-model"
model = Model("vosk-model")
endTime = time.time() + 10 

# ----- TTS 

def tts(tts):
    os.system(tts)

# ----- Audio Set
def micRecord():
    rec = KaldiRecognizer(model, 16000)
    rec.SetWords(True)
    rec.SetPartialWords(True)

# ----- Record Mic
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    tempAudio = []

    try:
        print('Speak Now..')
        while time.time() <= endTime:
            data = stream.read(4096)
            if rec.AcceptWaveform(data):
                print(rec.Result())
                tempAudio.append(rec.Result())
        text = rec.FinalResult().split('"')[-2]
        print(f"this is the final text {text}")

    except:
        text = 'You were quiet!'

    return text


# --- Command Checks

def commandChecks(text):

    command = text.split()[0]
    query = text.split()[1:]
    # print(query)
    

    if command == "wiki":
        query = "_".join(query).title()
        # print(query) 
        
        shell_exec = f"curl -sL 'https://en.wikipedia.org/wiki/{query}' | grep '<p>' | sed -e 's/<[^>]*>//g' -e 's/\&\#[0-9][0-9]//g' -e 's/\;[0-9][0-9]\;//g'  -e 's/\;//g' | head -1 > temp.txt"
        os.system(shell_exec)
        
        tts = f"cat temp.txt | piper --model {ttsModel} --output_raw | aplay -q -r 22050 -f S16_LE -t raw"
        os.system(tts)
        # os.system("rm ./temp.txt")

    elif command == "play":

        ttsquery = " ".join(query)
        response = f"Ok, Playing '{ttsquery}' now"
        tts = f'echo {response} | piper --model {ttsModel} --output_raw | aplay -q -r 22050 -f S16_LE -t raw & PIDTTS=$!'
        # print(tts)
        # os.system(tts)
        
        query = "+".join(query)
        # print(query)
        yt_command = yt(query) + '& PIDYT=$!'

        os.system(yt_command)
        os.system("wait $PIDTTS")
        os.system("wait $PIDYT")

        return response, tts

    elif command == "define":
        query = " ".join(query)
        definiton = word(query)

        tts = f'echo "The word {query} means {definiton}" | piper --model {ttsModel} --output_raw | aplay -q -r 22050 -f S16_LE -t raw &'
        # print(definiton)
        # print(tts)
        return definiton, tts
        # os.system("rm ./temp.txt")

    
    elif weatherWordCheck(str(text).split()):
        # print('----\nWORKINF')
        response = wttr()

        tts = f"echo {response} | piper --model {ttsModel} --output_raw | aplay -q -r 22050 -f S16_LE -t raw &"

        return response, tts
    
    else:
        query = str(command) + " " + " ".join(query)
        # query = str(text)
        print("query: ",query)
        response = os.popen(gptRespond(query)).read()
        response = response.rstrip()
        print("response : ", response)
        tts = f'echo "{response}" | piper --model {ttsModel} --output_raw | aplay -q -r 22050 -f S16_LE -t raw &'
        print("tts:", tts)

        return response, tts
