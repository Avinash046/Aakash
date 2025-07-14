import speech_recognition as sr
import pyttsx3
import sys
from modules import booking, messaging, media, vision

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen(language='en-IN'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Listening ({language})...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language=language)
        print(f"You said: {command}")
        return command
    except Exception as e:
        print("Sorry, I could not understand.")
        return ""

def main():
    print("\nWelcome to Aakash - Your AI Personal Assistant!")
    print("Type 'voice' to use voice commands, or type your command directly.")
    print("Type 'exit' to quit.\n")
    while True:
        user_input = input("Aakash > ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        elif user_input.lower() == 'voice':
            lang_choice = input("Choose language: 1) English 2) Hindi [1/2]: ")
            language = 'en-IN' if lang_choice.strip() == '1' else 'hi-IN'
            command = listen(language)
        else:
            command = user_input
        if not command:
            continue
        # Simple command routing
        if any(x in command.lower() for x in ["book", "ticket", "uber", "ola", "rapido", "flight", "bus", "train", "movie"]):
            booking.handle(command)
        elif any(x in command.lower() for x in ["message", "call", "text", "voice", "image", "video"]):
            messaging.handle(command)
        elif any(x in command.lower() for x in ["music", "song", "movie", "play"]):
            media.handle(command)
        elif any(x in command.lower() for x in ["face", "gesture", "recognize", "hand"]):
            vision.handle(command)
        else:
            print("Aakash: Sorry, I don't understand that command yet.")
            speak("Sorry, I don't understand that command yet.")

if __name__ == "__main__":
    main()