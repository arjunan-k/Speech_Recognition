import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()
is_on = True
while is_on:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f"{text}")
            if text == "stop":
                print("Hello Sir closing the program.")
                is_on = False
            if text == "refresh":
                print("Hello sir starting fresh!!!")
                is_on = True

    except speech_recognition.UnknownValueError():
        recognizer = speech_recognition.Recognizer()
        continue