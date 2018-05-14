#Main file where we will combine all the pieces of the project together
# CST-205 Multimedia Design & Programming
# Authors: Blayne Suttonwills, Jacob Fahy, Andrea Amezcua Moreno
# May 14, 2018
# https://github.com/jakefahy/205project
# The code takes a message and encodes it into an image. The image represents the message. Then, with the
# decoding button, the the code returns the secret message stored in the image.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QFileDialog
import cv2
from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPixmap
from google_images_download import google_images_download
from PIL import Image
import glob
from keyword_search import keyword
from lsb_steganography import decoding
#Andrea Amezcua worked on this file

class gui(QWidget):
    def __init__(self):
        super().__init__()

#make buttons
        self.setWindowTitle('205 Project')
        self.btn1 = QPushButton('Decode')
        self.btn2 = QPushButton('Encode')

#layout the buttons
        hbox = QHBoxLayout()
        hbox.addWidget(self.btn2)
        hbox.addWidget(self.btn1)
        self.setLayout(hbox)

        self.btn2.clicked.connect(self.encode)
        self.btn1.clicked.connect(self.decode)
    @pyqtSlot()
    def encode(self):
        self.new_win = EncodeWindow()
        self.new_win.show()

    def decode(self):
        self.new_win = DecodeWindow()
        self.new_win.show()
#Encoding the message into the image
class EncodeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.line_edit = QLineEdit()
        self.line_edit.selectAll()
        self.line_edit.setFocus()
        self.btn = QPushButton('Search')

        vbox = QVBoxLayout()
        vbox.addWidget(self.line_edit)
        vbox.addWidget(self.btn)
        self.setLayout(vbox)

        self.btn.clicked.connect(self.getText)

    @pyqtSlot()
    def getText(self):
        text = self.line_edit.text()
        #print(text)
        keyword(text)

#Decoding the image and getting the message back
class DecodeWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.image=None
        self.btn0 = QPushButton('Get Image')

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn0)
        self.setLayout(vbox)

        self.btn0.clicked.connect(self.getImage)

    @pyqtSlot()
    def getImage(self):
        fname, filter = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "Image File (*.png)")
        decoding(fname)

app = QApplication(sys.argv)
main_win = gui()
main_win.show()
sys.exit(app.exec_())
