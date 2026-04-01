"""
Simple Text-To-Speech in Python
CC0
----
CoolGuy158-Git
"""
from gtts import gTTS as T
import pygame as P
from io import BytesIO as B

item = input(">>> ")

data = B()
t = T(text=item, lang="en", slow=False)
t.write_to_fp(data)

data.seek(0)

P.mixer.init()
P.mixer.music.load(data, "mp3")
P.mixer.music.play()

while P.mixer.music.get_busy():
    continue
