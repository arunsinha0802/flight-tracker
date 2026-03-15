import asyncio
import os
import edge_tts
import playsound

# Voice selection - en-GB-SoniaNeural is a natural British female voice
# Alternative British male voice: en-GB-RyanNeural
VOICE = "en-GB-SoniaNeural"

async def _generate_speech(text, filename):
    # Generate the speech audio file using edge-tts
    communicate = edge_tts.Communicate(text, voice=VOICE)
    await communicate.save(filename)

def announce(text):
    # Generate the audio file
    filename = "announcement.mp3"
    asyncio.run(_generate_speech(text, filename))
    
    # Play the audio file
    playsound.playsound(filename)
    
    # Delete the file after playing
    os.remove(filename)


# Only runs when executing this file directly, not when imported
if __name__ == "__main__":
    announce("Flight BA436 from London Heathrow to New York is currently overhead")
