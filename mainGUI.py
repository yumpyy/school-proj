import sys
from PyQt6 import QtWidgets, QtCore, uic
from PyQt6.QtGui import QFont 
import qtawesome as qta

# --- My Modules
from mainFunctions import micRecord, commandChecks, tts
# from mainText import mainText
from myMods.dbManage import chatUpload

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
        self.micButton.setIconSize(QtCore.QSize(24, 24))
        
        self.sendButton = uiFile.findChild(QtWidgets.QPushButton, 'sendButton')
        self.sendButton.clicked.connect(self.messageBox)
        self.sendButton.setIcon(sendIcon)
        self.sendButton.setIconSize(QtCore.QSize(28, 28))
        
        self.chatBox.setStyleSheet("QListWidget::item {background-color: #5b6078;padding: 10px;margin: 5px 15px;border-radius: 10px;color:#cad3f5;}")
        self.chatBox.setWordWrap(True)
        self.chatBox.setAlternatingRowColors(True);

        self.font = QFont('Arial', 12)
        self.inputBox.setFont(self.font)
        self.chatBox.setFont(self.font)
        

    def messageBox(self):
        query = self.inputBox.text()
        if len(query) == 0:
            self.inputBox.setText('')

        else:
            result = commandChecks(query)
            response = result[0]
            print(response)
            self.chatBox.addItem(query)
            self.chatBox.addItem(response)
            tts(result[1])

            self.inputBox.setText('')

    def micClick(self):
        query = micRecord()
        result = commandChecks(query)
        response = result[0]

        if len(query) == 0:
            response = "Sorry, I could not hear you. Please try again"
            self.chatBox.addItem(response)

        else:
            self.chatBox.addItem(query)
            self.chatBox.addItem(response)
            tts(result[1])

            self.inputBox.setText('')
            

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec()
