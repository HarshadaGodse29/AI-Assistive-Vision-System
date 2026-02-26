import pyttsx3
import threading

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 160)
        self.engine.setProperty('volume', 1.0)

        # Select Windows voice properly
        voices = self.engine.getProperty('voices')
        if voices:
            self.engine.setProperty('voice', voices[0].id)

    def _speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def speak(self, text):
        print("Speaking:", text)
        thread = threading.Thread(target=self._speak, args=(text,))
        thread.start()