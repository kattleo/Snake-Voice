import speech_recognition as sr
import pydirectinput

def recognize_voice_and_send_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Listening for voice commands...")

    while True:
        try:
            with mic as source:
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
            text = recognizer.recognize_google(audio, language="de-DE").lower()

            print(f"Recognized: {text}")
            if "links" in text:  # "left" in German
                pydirectinput.press('left')
            elif "rechts" in text:  # "right" in German
                pydirectinput.press('right')
            elif "oben" in text:  # "up" in German
                print("up")
                pydirectinput.press('up')
            elif "unten" in text:  # "down" in German
                pydirectinput.press('down')
        except sr.WaitTimeoutError:
            print("No speech detected. Retrying...")
        except sr.UnknownValueError:
            print("Could not understand audio. Skipping...")
        except Exception as e:
            print(f"Error: {e}")

recognize_voice_and_send_command()