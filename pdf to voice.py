# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 23:15:41 2020

@author: thejunaidiqbal
"""


import PyPDF2 as pdf
import pyttsx3 as x


def audioBook(file):
    book = open(file,'rb')
    reader = pdf.PdfFileReader(book)
    speak = x.init();

    for a in range(12, reader.numPages):
        reader.getPage(a).extractText()
        speak.say(text)
        speak.runAndWait()
    
    
audioBook('C:\Users\thejunaidiqbal\Documents\Resume-Muhammad-Junaid-Iqbal.pdf')