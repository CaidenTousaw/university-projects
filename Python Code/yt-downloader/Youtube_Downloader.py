import subprocess
import os
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, QLineEdit, QMessageBox, QCheckBox
from PyQt5.QtCore import pyqtSlot
import sys

#some vars

#----- QUALITY OPTIONS THAT WILL BE PRESENTED TO USER
#best: Select the best quality format represented by a single file with video and audio.
#worst: Select the worst quality format represented by a single file with video and audio.
#bestvideo: Select the best quality video-only format (e.g. DASH video). May not be available.
#worstvideo: Select the worst quality video-only format. May not be available.
#bestaudio: Select the best quality audio only-format. May not be available.
#worstaudio: Select the worst quality audio only-format. May not be available.

#definitions



def setVars():
    global location
    global name
    global link
    location = "blank"
    name = "blank"
    link = "blank"
    location = locationInput.text()
    name = nameInput.text()
    link = urlInput.text()
    download()

def changeQualityUp():
    global quality
    quality = "best"

def changeQualityDown():
    global quality
    quality = "worst"


def window():
    global locationInput
    global nameInput
    global urlInput
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 370, 220)
    win.setWindowTitle("Youtube Downloader in Python")
    win.setWindowIcon(QtGui.QIcon('icon.jpg'))

#url set
    label = QtWidgets.QLabel(win)
    label.setText("Set Download URL:")
    label.move(10, 5)
    label.resize(150, 50)

    urlInput = textbox = QLineEdit(win)
    urlInput.move(10, 40)
    urlInput.resize(350,25)

#location set
    label2 = QtWidgets.QLabel(win)
    label2.setText("Set Download Location:")
    label2.move(10,55)
    label2.resize(150, 50)


    locationInput = textbox = QLineEdit(win)
    locationInput.move(10, 90)
    locationInput.resize(350,25)


#filename set
    label3 = QtWidgets.QLabel(win)
    label3.setText("Set File Name:")
    label3.move(10, 105)
    label3.resize(150, 50)


    nameInput = textbox = QLineEdit(win)
    nameInput.move(10, 145)
    nameInput.resize(350,25)


    setAll_Download = QtWidgets.QPushButton(win)
    setAll_Download.setText("Download")
    setAll_Download.move(290, 185)
    setAll_Download.resize(70, 25)
    setAll_Download.clicked.connect(setVars)



#checkbox info
    label = QtWidgets.QLabel(win)
    label.setText("Quality Options:")
    label.move(10, 170)
    label.resize(150, 50)

    cb = QCheckBox(win)
    cb.setText("Best")
    cb.move(110, 182)
    cb.stateChanged.connect(changeQualityUp)

    cb2 = QCheckBox(win)
    cb2.setText("Worst")
    cb2.move(180, 182)
    cb2.stateChanged.connect(changeQualityDown)




    win.show()
    sys.exit(app.exec_())


def download():
        f = open("YT_DOWNLOADER.bat", "w")
        f.write("youtube-dl -o" + " " + location + name + ".mp4" + " " + "-f " + quality + " " + link)
        f = open("YT_DOWNLOADER.bat", "r")
        print(f.read())
        subprocess.call(['YT_DOWNLOADER.bat'])


#stuff that runs

window()
