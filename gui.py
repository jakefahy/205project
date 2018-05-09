# CST-205 Multimedia Design & Programming
#
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

class gui(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('205 Project')
        self.btn1 = QPushButton('Decode')
        self.btn2 = QPushButton('Encode')

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

class DecodeWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.image=None
        self.btn0 = QPushButton('Get Image')
        self.boton = QPushButton('Get Message')

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn0)
        vbox.addWidget(self.boton)
        self.setLayout(vbox)

        self.btn0.clicked.connect(self.getImage)
        #self.button.clicked.connect(self.)

    @pyqtSlot()
    def getImage(self):
        fname, filter = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "Image File (*.jpeg)")
        if fname:
            self.loadImage(fname)
        else:
            print('Invalid Image')

    def loadImage(self, fname):
        self.image = cv2.imread(fname)

app = QApplication(sys.argv)
main_win = gui()
main_win.show()
sys.exit(app.exec_())
