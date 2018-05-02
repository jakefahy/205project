import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import pyqtSlot

class gui(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('205 Project')
        self.label = QLabel('Message: ')
        self.line_edit = QLineEdit()
        self.line_edit.selectAll()
        self.line_edit.setFocus()
        self.btn = QPushButton('Search')

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.line_edit)
        vbox.addWidget(self.btn)
        self.setLayout(vbox)

#        self.btn.clicked.connect(self.open_win)
'''
        @pyqtSlot()
        def open_win(self):
            choice = QtGui.QMessageBox.question(self, "Hey", "ok")

            text = self.line_edit.currentText()
            self.
            self.new_win.show()

'''

app = QApplication(sys.argv)
main_win = gui()
main_win.show()
sys.exit(app.exec_())
