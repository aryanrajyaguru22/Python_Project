# pip install pyttsx3 

'''
This Will Run Before Above Mention Libarary Install In You Machine 
After Installation Libarary Then Run The Code
'''

import pyttsx3

def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Set properties (optional)
    engine.setProperty('rate', 150)    # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
    
    # Convert text to speech
    engine.say(text)
    
    # Wait for the speech to finish
    engine.runAndWait()

# Example usage
if __name__ == "__main__":
    text = input("Enter the text you want to hear: ")
    text_to_speech(text)