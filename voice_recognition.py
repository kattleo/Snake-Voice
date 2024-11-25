import threading
import speech_recognition as sr
import requests

def send_command_to_server(command):
    try:
        # Replace with the actual endpoint of your Flask app
        url = "http://127.0.0.1:5000/command"
        data = {'command': command}
        response = requests.post(url, json=data)
        print(f"Sent '{command}' to server, response: {response.status_code}")
    except Exception as e:
        print(f"Failed to send command: {e}")

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
                send_command_to_server('left')
            elif "rechts" in text:  # "right" in German
                send_command_to_server('right')
            elif "oben" in text:  # "up" in German
                send_command_to_server('up')
            elif "unten" in text:  # "down" in German
                send_command_to_server('down')
        except sr.WaitTimeoutError:
            print("No speech detected. Retrying...")
        except sr.UnknownValueError:
            print("Could not understand audio. Skipping...")
        except Exception as e:
            print(f"Error: {e}")

# Run the speech recognition in a separate thread
if __name__ == "__main__":
    thread = threading.Thread(target=recognize_voice_and_send_command)
    thread.daemon = True
    thread.start()

    # Keep the main thread alive
    while True:
        pass
