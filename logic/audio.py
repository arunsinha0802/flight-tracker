import asyncio
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
    # Generate the speech file first so it's ready to play
    filename = "announcement.mp3"
    text = f"Good {get_time_of_day()} Mr. Ellis. Your flight tracker is online."
    asyncio.run(_generate_speech(text, filename))
    
    # Now play welcome sound — announcement is already ready
    playsound.playsound("assets/welcome.mp3")
    time.sleep(0.1)
    
    # Play immediately after welcome sound with no delay
    playsound.playsound(filename)
    time.sleep(0.5)
    os.remove(filename)

def announce(text):
    # Generate the speech file first so it's ready to play
    filename = "announcement.mp3"
    asyncio.run(_generate_speech(text, filename))
    
    # Now play bing bong — announcement is already ready
    playsound.playsound("assets/bingbong.mp3")
    time.sleep(0.1)
    
    # Play immediately after bing bong with no delay
    playsound.playsound(filename)
    time.sleep(0.5)
    os.remove(filename)

# Only runs when executing this file directly, not when imported
if __name__ == "__main__":
    announce("Flight BA436 from London Heathrow to New York is currently overhead")
