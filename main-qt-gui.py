import sys
from PyQt5 import QtWidgets, QtCore, uic
import PyQt5.QtGui as QtGui
import qtawesome as qta

import mainMic
import mainText

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # -- Fonts
        sendIcon = qta.icon('fa5s.arrow-up')
        micIcon = qta.icon('fa5s.microphone')

        uiFile = uic.loadUi('main.ui', self)

        self.inputBox = uiFile.findChild(QtWidgets.QLineEdit, 'inputBox')
        self.chatBox = uiFile.findChild(QtWidgets.QListWidget, 'chatBox')

        self.micButton = uiFile.findChild(QtWidgets.QPushButton, 'micButton')
        self.micButton.clicked.connect(self.micClick)
        self.micButton.setIcon(micIcon)
        self.micButton.setIconSize(QtCore.QSize(28, 28))
        
        self.sendButton = uiFile.findChild(QtWidgets.QPushButton, 'sendButton')
        self.sendButton.clicked.connect(self.messageBox)
        self.sendButton.setIcon(sendIcon)
        self.sendButton.setIconSize(QtCore.QSize(28, 28))
        
        self.chatBox.setStyleSheet("QListWidget::item {background-color: #5b6078;padding: 10px;margin: 5px 15px;border-radius: 10px;color:#cad3f5;}")
        self.chatBox.setWordWrap(True)
        # self.inputBox.setWordWrap(True)

        self.font = QtGui.QFont('Arial', 12)
        self.inputBox.setFont(self.font)
        self.chatBox.setFont(self.font)
        

    def messageBox(self):
        message = self.inputBox.text()
        if len(message) == 0:
            self.inputBox.setText('')

        else:
            reponse = mainText.mainText(message)
            print(reponse)
            self.chatBox.addItem(message)
            self.chatBox.addItem(reponse)
            self.inputBox.setText('')

    def micClick(self):
        print('gex')
        mainMic.micRecord()
        # 

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec()
