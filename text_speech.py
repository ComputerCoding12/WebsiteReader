import pyttsx3 as pyttsx

class Speak():
    """This class is used to convert the text provide the the method speak into audio output.
        Using the module pyttsx3"""
    def speak(self, text, y=1):
        """here the input variable text is converted to speech and y is the voice selected"""
        self.text = text
        eng = pyttsx.init()
        voices = eng.getProperty('voices')
        y = int(y)
        eng.setProperty('voice', voices[y].id)
        eng.runAndWait()
        eng.say(text)
        eng.runAndWait()
