"""
-------------------------------------------------------
[Text to speech tool based on GTTS]
-------------------------------------------------------
Author:  Tristan Pham    
Email:   haitrung2375@gmail.com
__updated__ = "2025-01-16"
-------------------------------------------------------
"""
# imports
from gtts import gTTS
import os


def read_text_file(file_name):
    """
    Reads and returns the content of the provided text file.
    Handles file not found and other reading errors.

    Parameters:
        file_name (str): The name of the text file to read.
    Returns:
        str: The text content of the file, or None if an error occurred.
    """
    try:
        # Open the file and read its content
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        # Handle case when the file is not found
        print(f"Error: The file '{file_name}' was not found.")
        return None
    except Exception as e:
        # Catch any other exceptions and print the error message
        print(f"An error occurred: {e}")
        return None


def convert_text_to_speech(text, lang='en', slow=False, output='output.mp3'):
    """
    Converts the given text to speech and saves it as an MP3 file.

    Parameters:
        text (str): The text to be converted to speech.
        lang (str): The language of the text (default is English).
        slow (bool): Whether the speech should be slow (default is False).
        output (str): The name of the output MP3 file (default is 'output.mp3').
    """
    # Create a gTTS object with the provided parameters
    tts = gTTS(text=text, lang=lang, slow=slow)

    # Save the generated speech to an MP3 file
    tts.save(f"{output}.mp3")

    # Play the saved MP3 file (macOS specific, adjust for cross-platform usage if needed)
    os.system(f"afplay {output}.mp3")


def get_user_input():
    """
    Handles user input for the text file, speech speed, and output file name.

    Returns:
        tuple: A tuple containing text, slow flag, and output file name, or None if invalid input.
    """
    # Ask the user for the text file name
    file_name = input("Input the txt file name: ")
    # Read the content of the text file
    text = read_text_file(file_name)
    # If the file is empty or not found, return None
    if not text:
        return

    # Ask the user if they want the speech to be slower
    slow = input("Do you want it slower? (Y/N): ").strip().upper() == 'Y'

    # Ask the user for the output MP3 file name, defaulting to 'output'
    output = input("Name the output mp3 file: ").strip() or 'output'

    return text, slow, output


def main():
    """
    Main function to run the text-to-speech conversion process.
    It gets user input, reads the file, and converts the text to speech.
    """
    print("Txt file must be imported")

    user_input = get_user_input()

    # If valid input is received, unpack the tuple and call the conversion function
    if user_input:
        text, slow, output = user_input
        convert_text_to_speech(text, slow=slow, output=output)


# Ensure the script runs when executed directly
if __name__ == "__main__":
    main()
