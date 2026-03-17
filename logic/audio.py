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