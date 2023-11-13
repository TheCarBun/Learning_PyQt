from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setFixedSize(481,724)
        MainWindow.setStyleSheet("background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(68, 68, 68);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(129, 129, 129);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 461, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(4)
        self.outputLabel.setMidLineWidth(0)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("%"))
        self.percentButton.setGeometry(QtCore.QRect(10, 130, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentButton.setFont(font)
        self.percentButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.percentButton.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.percentButton.setObjectName("percentButton")
        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("C"))
        self.cButton.setGeometry(QtCore.QRect(130, 130, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cButton.setFont(font)
        self.cButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cButton.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.cButton.setObjectName("cButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.remove_it())
        self.arrowButton.setGeometry(QtCore.QRect(250, 130, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrowButton.setFont(font)
        self.arrowButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.arrowButton.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.arrowButton.setObjectName("arrowButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(370, 130, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.divideButton.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.divideButton.setObjectName("divideButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("x"))
        self.multiplyButton.setGeometry(QtCore.QRect(370, 240, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.multiplyButton.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.multiplyButton.setObjectName("multiplyButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(250, 240, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nineButton.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.nineButton.setObjectName("nineButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(130, 240, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eightButton.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.eightButton.setObjectName("eightButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 240, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sevenButton.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.sevenButton.setObjectName("sevenButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(370, 350, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minusButton.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.minusButton.setObjectName("minusButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(250, 350, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sixButton.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.sixButton.setObjectName("sixButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(130, 350, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fiveButton.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.fiveButton.setObjectName("fiveButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 350, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fourButton.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.fourButton.setObjectName("fourButton")
        self.plusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("+"))
        self.plusButton.setGeometry(QtCore.QRect(370, 460, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusButton.setFont(font)
        self.plusButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plusButton.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.plusButton.setObjectName("plusButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(250, 460, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.threeButton.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.threeButton.setObjectName("threeButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(130, 460, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.twoButton.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.twoButton.setObjectName("twoButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 460, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.oneButton.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.oneButton.setObjectName("oneButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.math_it())
        self.equalButton.setGeometry(QtCore.QRect(370, 570, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.equalButton.setStyleSheet("background-color: rgb(255, 155, 73);")
        self.equalButton.setObjectName("equalButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(250, 570, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalButton.setFont(font)
        self.decimalButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.decimalButton.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.decimalButton.setObjectName("decimalButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(130, 570, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zeroButton.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.zeroButton.setObjectName("zeroButton")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.plus_minus_it())
        self.plusminusButton.setGeometry(QtCore.QRect(10, 570, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plusminusButton.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.plusminusButton.setObjectName("plusminusButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def math_it(self):
        screen = self.outputLabel.text()
        if screen == "":
            screen = "0"
        elif "x" in screen:
            screen = screen.replace("x", "*")
        try:
            answer = eval(screen)
            self.outputLabel.setText(str(answer))
        except:
            self.outputLabel.setText('Error')

    def plus_minus_it(self):
        screen = self.outputLabel.text()
        if "-" in screen:
            self.outputLabel.setText(screen.replace("-",""))
        else:
            self.outputLabel.setText(f'-{screen}')

    def remove_it(self):
        screen = self.outputLabel.text()
        if screen == "0":
            pass
        elif screen == "":
            self.outputLabel.setText('0')
        elif len(screen) == 1:
            self.outputLabel.setText('0')
        else:
            screen = self.outputLabel.text()
            screen = screen[:-1]
            self.outputLabel.setText(f'{screen}')

    def dot_it(self):
        screen = self.outputLabel.text()
        if screen[-1] == ".":
            pass
        else:
            self.outputLabel.setText(f'{screen}.')

    def press_it(self, pressed):
        if pressed == "C":
            self.outputLabel.setText("0")
        else:
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())