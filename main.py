import os
import enum
import speech_recognition as sr
from gtts import gTTS

# Defined by User
AUDIO_FNAME = "hearing_aids.mp3"
MESSAGE = "hey granpa"

def recognizeAudioSource(*args):
    compare_flg = False
    r = args[0]
    if len(args) == 2:
        compare_flg = True
        keyword = args[1]

    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        print("You said : " + r.recognize(audio))
        if compare_flg:
            if r.recognize != keyword:
                return -1
        tts = gTTS(text=r.recognize(audio), lang='en')
        tts.save(AUDIO_FNAME)
        os.system('afplay ./' + AUDIO_FNAME)
        return 1
    except LookupError:
        print("Could not understand audio")
        return 0

if __name__ == "__main__":
    STATE = enum.Enum("STATE", "wait_for_input listening")
    r = sr.Recognizer()
    state_ = STATE.wait_for_input
    counter = 0
    while 1:
        if state_ is STATE.wait_for_input:
            if recognizeAudioSource(r, MESSAGE):
                state_ = STATE.listening
        if state_ is STATE.listening:
            counter = counter+1
            print("loop : " + str(counter))
            print(recognizeAudioSource(r))
