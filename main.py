import os
import speech_recognition as sr
from gtts import gTTS

AUDIO_FNAME = "hearing_aids.mp3"

r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)

try:
    print("You said : " + r.recognize(audio))
    tts = gTTS(text=r.recognize(audio), lang='en')
    tts.save(AUDIO_FNAME)
    os.system('afplay ./' + AUDIO_FNAME)
except LookupError:
    print("Could not understand audio")