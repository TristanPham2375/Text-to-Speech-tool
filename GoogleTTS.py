"""
-------------------------------------------------------
[Text to speech tool based on GTTS]
-------------------------------------------------------
Author:  Tristan Pham    
Email:   haitrung2375@gmail.com
__updated__ = "2024-10-18"
-------------------------------------------------------
"""
# imports
from gtts import gTTS
import os


def text_to_speech_google(lang='en'):
    """
    Reads text from the provided text file and converts it to speech.
    The speech is saved to an MP3 file. 
    """
    # Ask user for file path
    print("Txt file must be imported")
    file_name = str(input("Input the txt file name: "))

    # Open and read the file
    file = open(file_name, 'r', encoding='utf-8')

    text = file.read()

    # Checks if the file is empty
    if text.strip():

        # Convert the text to speech
        slow = str(input("Do you to it slower?(Y/N): "))
        if slow == 'Y':
            slow = True
        else:
            slow = False
        tts = gTTS(text=text, lang=lang, slow=False)

        # save the file
        output = str(input("Name the ouput mp3 file: "))
        tts.save(f"{output}.mp3")
        os.system(f"afplay {output}.mp3")

    else:
        print("The input file is empty.")


text_to_speech_google()
