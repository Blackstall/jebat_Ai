import speech_recognition as sr
import pyttsx3
from nlp_engine import NLPEngine

# Initialize GPT-Neo
try:
    nlp_engine = NLPEngine(model_type="gpt-neo")
except Exception as e:
    print(f"⚠️ Error initializing NLP engine: {e}")
    nlp_engine = None  # Prevent crashes

def get_female_voice(engine):
    """Find and set a female voice."""
    voices = engine.getProperty('voices')
    for voice in voices:
        if "female" in voice.name.lower() or "zira" in voice.name.lower():  # Common female voice names
            engine.setProperty('voice', voice.id)
            print(f"🎙️ Using Female Voice: {voice.name}")
            return
    print("⚠️ No female voice found. Using default voice.")

def speak(text):
    """Makes Jebat speak with a female voice."""
    engine = pyttsx3.init()
    get_female_voice(engine)  # Set female voice
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens to user input and returns the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"🗣️ {text}")  # Display recognized speech
            return text
        except sr.UnknownValueError:
            print("⚠️ Sorry, I didn't understand that.")
            return None

def listen_and_respond():
    """Listens to user input and responds using NLP."""
    text = listen()
    if text and nlp_engine:
        response = nlp_engine.generate_response(text)
        print(f"🤖 Jebat: {response}")
        speak(response)
