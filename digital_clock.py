from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QLCDNumber
import sys,time


class Digital_clock(QMainWindow):
    def __init__(self):
        super().__init__()
        title = "Digital Clock -by Anirudh"
        top = 400
        left = 300
        width = 550
        height = 150

        icon = "clock.png"

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        self.setWindowIcon((QIcon(icon)))

        self.initUI()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)



    def initUI(self):
        self.clock_screen = QLCDNumber(self)
        self.clock_screen.setStyleSheet("color : black ; background-color: white")
        self.clock_screen.setDigitCount(8)
        self.clock_screen.setGeometry(QtCore.QRect(0 , 0 ,550 , 150))
        self.showTime()


    def showTime(self):
       showTime = time.strftime("%I:%M:%S")
       self.clock_screen.display(showTime)


app = QApplication(sys.argv)
clock = Digital_clock()
clock.show()
app.exec()
