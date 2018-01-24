#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Mouse Clicker

Author: Fernando Daniel Jaime
Last edited: January 2018
"""

import sys, os, time
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QComboBox, QGridLayout, 
    QLabel, QLineEdit, QMessageBox, QWidget)
from PyQt5.QtGui import QCursor

class MouseClicker(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0
        self.counter = 0
        self.countEnd = 0

        self.text = "x: {0},  y: {1}".format(x, y)

        # Informative label -------------------------
        self.textlabel = QLabel(
            "This autoclicker only works on linux environments" +
            "<br>and requires xdotool installed in order to work." +
            "<br>Github xdotool:" +
            "<br>https://github.com/jordansissel/xdotool"
            "<br>Download xdotool:" +
            "<br>http://www.semicomplete.com/projects/xdotool/"
            "<br><br><b>Press F1 to start</b>" +
            "<br><b>Move mouse to stop</b>", self)
        grid.addWidget(self.textlabel, 0, 1, Qt.AlignTop)

        # Mouse tracker Label -----------------------
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 1, 1, Qt.AlignTop)

        # Click amount ------------------------------
        self.ClkAmnt = QLineEdit()
        self.ClkAmnt.setText("1000000")
        grid.addWidget(self.ClkAmnt, 2, 0, Qt.AlignTop)

        self.ClickAmountLabel = QLabel("<b>Amount of clicks desired</b>", self)
        grid.addWidget(self.ClickAmountLabel, 2, 1, Qt.AlignTop)
        # ------------------------------------------

        # Click delay ------------------------------
        self.clkDelay = QLineEdit()
        self.clkDelay.setText("0.01")
        grid.addWidget(self.clkDelay, 3, 0, Qt.AlignTop)

        self.DelayClkLabel = QLabel("<b>Seconds of delay " +
            "between clicks</b>" +
            "<br>You may use floating point to indicate less than a second" +
            "<br>For instance 0.1 or 0.01", self)
        grid.addWidget(self.DelayClkLabel, 3, 1, Qt.AlignTop)
        # ------------------------------------------

        self.setMouseTracking(True)

        self.setLayout(grid)
        self.setGeometry(300, 300, 500, 350)
        self.setWindowTitle("Mouse Clicker")
        self.show()


    def mouseMoveEvent(self, e):
        x = e.globalX()
        y = e.globalY()
        self.setFocus(True)
        self.activateWindow()

        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            cursorOldPos = str(QCursor().pos())
            self.counter = 1
            # sets amount of clicks desired
            self.countEnd = int(self.ClkAmnt.text())

            # os.popen("xdotool click --delay 90 --repeat 1000 1")
            while(self.counter <= self.countEnd):
                os.popen("xdotool click 1")
                print("the counter is: " + str(self.counter))
                if(cursorOldPos != str(QCursor().pos())):
                    print("Mouse moved - loop terminated")
                    break
                self.counter += 1
                # sets delay between clicks
                time.sleep(float(self.clkDelay.text()))
        elif event.key() == Qt.Key_Escape:
            reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.Cancel, QMessageBox.Cancel)

            if reply == QMessageBox.Yes:
                QApplication.instance().quit()
            else:
                event.accept()
        else:
            event.ignore()


    # def focusOutEvent(self, event):
    #     self.setFocus(True)
    #     self.focusWidget()
    #     self.focusPolicy()
    #     self.activateWindow()
    #     self.raise_()
    #     self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MouseClicker()
    sys.exit(app.exec_())
