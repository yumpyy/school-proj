#!/usr/bin/env python3

import os

# --- Modules in directory
from myMods.weather import wttr
from myMods.gptSupport import gptRespond
from myMods.yt import yt 
from myMods.word import word


def weatherWordCheck(text):
    weatherWords = ['weather', 'temprature', '']
    for word in text:
        if word in weatherWords:
            return True
    return False


# ----- Transc and TTS set
ttsModel="./models/model.onnx"

def mainText(text):
# print(text.split())
    textSplit = text.split()
    command = text.split()[0]
    query = text.split()[1:]
# print(query)

# --- Command Checks

    if command == "wiki":

        query = "_".join(query).title()
        # print(query) 
        
        shellExec = f"curl -sL 'https://en.wikipedia.org/wiki/{query}' | grep '<p>' | sed -e 's/<[^>]*>//g' -e 's/\&\#[0-9][0-9]//g' -e 's/\;[0-9][0-9]\;//g'  -e 's/\;//g' | head -1 > temp.txt"
        os.system(shellExec)

        with open('temp.txt', 'r') as f:
            response = f.read()

        tts = f"cat temp.txt | piper --model {ttsModel} --output_raw | aplay -q -r 22050 -f S16_LE -t raw &"
        os.system(tts)

        return response
        # os.system("rm ./temp.txt")

    elif command == "play":
        ttsquery = " ".join(query)
        tts = f'echo Ok, Playing "{ttsquery}" now | piper --model {ttsModel} --output_raw | aplay -q -r 22050 -f S16_LE -t raw & PIDTTS=$!'
        # print(tts)
        os.system(tts)
        query = "+".join(query)
        # print(query)
        yt_command = yt(query) + '& PIDYT=$!'
        os.system(yt_command)
        os.system("wait $PIDTTS")
        os.system("wait $PIDYT")
        
        response = f'Ok, Playing {ttsquery} now..'
        return response


    elif command == "define":
        query = " ".join(query)
        definiton = word(query)
        tts = f'echo "The word {query} means {definiton}" | piper --model {ttsModel} --output_raw | aplay -q -r 22050 -f S16_LE -t raw & PIDTTS=$!'
        # print(definiton)
        # print(tts)
        os.system(tts)
        # os.system("rm ./temp.txt")

        response = f'The word {query} means {definiton}'
        return response

# elif text.split() in weatherCheck:
    elif weatherWordCheck(textSplit):
        # print('----\nWORKINF')
        response = wttr()

        tts = f"echo {response} | piper --model {ttsModel} --output_raw | aplay -q -r 22050 -f S16_LE -t raw &"
        os.system(tts)

        return response

    else:
        print(query)
        query = str(command) + " " + " ".join(query)
        print(query)
        response = gptRespond(query)
        tts = f'echo "{response}" | piper --model {ttsModel} --output_raw | aplay -q -r 22050 -f S16_LE -t raw &'
        os.system(tts)

        return response
