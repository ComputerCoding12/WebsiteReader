
#Basic Required Imports for the program to work
import requests
import threading
from bs4 import BeautifulSoup
import os
import text_speech as ts

class WebScr:
    """This class to scrape webpage based on the requirement of the function and classes present.
        The output of this class can be tailered according to your needs"""
    def __init__(self, url=None):
        if url != None:
            if url[0]=='h' and url[1]=='t' and url[2]=='t'and url[3]=='p':
                self.setUrl(url)
            elif url[-1]=='l' and url[-2]=='m' and url[-3]=='t' and url[-4]=='h':
                self.setHtml(url)
    def setHtml(self, path):
        with open(path, 'r') as f:
            a = f.read()
        self.sitetext = a
        self.soup = BeautifulSoup(self.sitetext, 'lxml')
        self.sitetext = None
    def setUrl(self, url):
        self.site = requests.get(url)
        self.sitetext = self.site.text
        self.soup = BeautifulSoup(self.sitetext, 'lxml')
        self.site = None
    def Prettify(self):
        return self.soup.prettify()
    def savehtml(self, path=None):
        path = os.getcwd()
        file = path + "\\File.html"
        with open(file, 'w') as f:
            f.write(self.Prettify())
    def getText(self, tag='p'):
        text = ''
        for i in self.soup.find_all(tag):
            text += i.text + '\n'
        self.text = text
        return text

class TextPlayer(threading.Thread):
    """This plays the text that is provided to it with a parallel extinction of control over the play
        Using the Threading inbuild module"""
    def __init__(self, text=None):
        threading.Thread.__init__(self)
        if text != None:
            self.setText(text)
        self.pause = False
        self.stop = False
        self.sp = ts.Speak()
    def setText(self, text):
        self.text = text
        self.Editor()
        self.text = None
    def Editor(self):
        edited = self.text.replace('\n', ' ')
        Text_array = edited.split('.')
        array = []
        for i in Text_array:
            if i != '':
                array.append(i)
        edited = None
        Text_array = None
        self.Text_array = array
        self.size = len(array)
        self.runner = 0
    def play(self):
        while not self.stop:
            while not self.pause:
                if self.runner < self.size:
                    print(self.Text_array[self.runner])
                    self.sp.speak(self.Text_array[self.runner])
                    os.system('cls')

                else:
                    self.pause = True
                    self.stop = True
                self.runner += 1
    def run(self):
        while not self.stop:
            fn = input()
            os.system('cls')
            if fn == 'p':
                self.pause ^= True
            elif fn == 's':
                self.stop = True
            else:
                pass
        print("Controller stopped")

class podcast:
    """This is the main class used to preform the reading of a certain website using WebSrc, TextPlayer"""
    def __init__(self, data=None):
        if data != None:
            self.setData(data)
        self.pi = TextPlayer()
    def setData(self, data):
        self.xi = WebScr(data)
    def savehtml(self, path):
        self.xi.savehtml(path)
    def play(self):
        self.pi.setText(self.xi.getText())
        self.pi.start()
        self.pi.play()
        self.pi.join()

#def Player(text):
#    delta = TextPlayer(text)
#    delta.start()
#    delta.play()
#
if (__name__ == '__main__'):
    a = input(": ")
    pc = podcast(a)
    pc.play()
