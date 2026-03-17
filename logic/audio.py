""" import asyncio
import os
import edge_tts
import playsound
import time 
from logic.clock import get_time_of_day

# Voice selection - en-GB-SoniaNeural is a natural British female voice
# Alternative British male voice: en-GB-RyanNeural
VOICE = "en-GB-SoniaNeural"

async def _generate_speech(text, filename):
    # Generate the speech audio file using edge-tts
    communicate = edge_tts.Communicate(text, voice=VOICE)
    await communicate.save(filename)

def greeting():
    # Play welcome sound first
    playsound.playsound("assets/welcome.mp3")
    time.sleep(0.1)
    
    # Generate and play the greeting announcement
    filename = "announcement.mp3"
    text = f"Good {get_time_of_day()} Mr. Ellis. Your flight tracker is online."
    asyncio.run(_generate_speech(text, filename))
    playsound.playsound(filename)
    time.sleep(0.5)
    os.remove(filename)

def announce(text):
    # Play the bing bong chime first
    print("1")
    playsound.playsound("assets/bingbong.mp3")
    print("2")
    # Generate and play the announcement
    print("3")
    filename = "announcement.mp3"
    print("4")
    asyncio.run(_generate_speech(text, filename))
    print("5")
    playsound.playsound(filename)
    print("6")
    time.sleep(0.5)
    os.remove(filename)

# Only runs when executing this file directly, not when imported
if __name__ == "__main__":
    announce("Flight BA436 from London Heathrow to New York is currently overhead")
 """

import asyncio
import os
import edge_tts
import time
import pygame
from logic.clock import get_time_of_day

# Initialise pygame mixer once when the module loads
pygame.mixer.init()

VOICE = "en-GB-SoniaNeural"

async def _generate_speech(text, filename):
    communicate = edge_tts.Communicate(text, voice=VOICE)
    await communicate.save(filename)

def _play(filename):
    # Play a file and wait for it to finish
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.05)

def announce(text):
    _play("assets/bingbong.mp3")
    time.sleep(0.1)

    filename = "announcement.mp3"
    asyncio.run(_generate_speech(text, filename))
    _play(filename)
    time.sleep(0.5)
    pygame.mixer.music.unload()  # Release the file before deleting
    os.remove(filename)

def greeting():
    _play("assets/welcome.mp3")
    time.sleep(0.1)

    filename = "announcement.mp3"
    text = f"Good {get_time_of_day()} Mr. Ellis. Your flight tracker is online."
    asyncio.run(_generate_speech(text, filename))
    _play(filename)
    time.sleep(0.5)
    pygame.mixer.music.unload()  # Release the file before deleting
    os.remove(filename)


if __name__ == "__main__":
    announce("Flight BA436 from London Heathrow to New York is currently overhead")