import asyncio
import os
import edge_tts
import playsound
import time 

# Voice selection - en-GB-SoniaNeural is a natural British female voice
# Alternative British male voice: en-GB-RyanNeural
VOICE = "en-GB-SoniaNeural"

async def _generate_speech(text, filename):
    # Generate the speech audio file using edge-tts
    communicate = edge_tts.Communicate(text, voice=VOICE)
    await communicate.save(filename)

def announce(text):
    # Play the bing bong chime first
    playsound.playsound("assets/bingbong.wav")
    time.sleep(0.1)
    
    # Then generate and play the announcement
    filename = "announcement.mp3"
    asyncio.run(_generate_speech(text, filename))
    playsound.playsound(filename)
    time.sleep(0.5)
    os.remove(filename)


# Only runs when executing this file directly, not when imported
if __name__ == "__main__":
    announce("Flight BA436 from London Heathrow to New York is currently overhead")
