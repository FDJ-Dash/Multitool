#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyQt5 Multitool

This program puts together multiple widgets
on a single application.

Version: 0.1 alpha

Author: Fernando Daniel Jaime
Last edited: January 2018
"""

from PyQt5.QtWidgets import ( QAction, QApplication,
    QHBoxLayout, QMainWindow, QMenu, QMessageBox,
    QStackedWidget, QSystemTrayIcon, QWidget)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


class Multitool(QMainWindow, QWidget):
    def __init__(self):
        super(Multitool, self).__init__()

        self.statusbar = self.statusBar()
        self.statusBar().showMessage('Ready')

        # General actions starts -------------------------------------
        exitAction = QAction(QIcon('icons/exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QApplication.instance().quit)

        aboutAction=QAction(QIcon('icons/biohazard.svg'),'About',self)
        aboutAction.setStatusTip('About')
        aboutAction.triggered.connect(self.about)

        viewStatAction = QAction('View statusbar', self, checkable=True)
        viewStatAction.setStatusTip('View statusbar')
        viewStatAction.setChecked(True)
        viewStatAction.triggered.connect(self.toggleStatBar)

        viewToolbarAction = QAction('View toolbar', self, checkable=True)
        viewToolbarAction.setStatusTip('View toolbar')
        viewToolbarAction.setChecked(True)
        viewToolbarAction.triggered.connect(self.toggleToolBar)
        # General actions ends -------------------------------------


        # Menu bar creation starts -------------------------------------
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        viewMenu = menubar.addMenu('View')
        viewMenu.addAction(viewStatAction)
        viewMenu.addAction(viewToolbarAction)

        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(aboutAction)
        # Menu bar creation ends -------------------------------------

        # Toolbar creation starts -------------------------------------
        self.toolbar1 = self.addToolBar('Exit')
        self.toolbar1.addAction(exitAction)
        # Toolbar creation ends -------------------------------------

        self.setGeometry(300, 300, 700, 400)
        self.setWindowTitle('Multitool')
        self.setWindowIcon(QIcon('icons/biohazard.svg'))
        self.show()


    def toggleStatBar(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


    def toggleToolBar(self, state):
        if state:
            self.toolbar1.show()
        else:
            self.toolbar1.hide()


    def minimizeToTray(self, state):
        if state:
            self.hide()
            self.trayIcon.showMessage(
                "Tray Program",
                "Application was minimized to tray",
                QSystemTrayIcon.Information,
                2000)


    def about(self):
        pixmap = QPixmap('icons/biohazard.svg')
        msg = QMessageBox(QMessageBox.Information, 'About Multitool',
            "<b>Aplication name:</b> Multitool" +
            "<br> <b>Version:</b> V0.1 alpha" +
            "<br><b>Description:</b> This application puts together many" +
            "<br>widgets into a single application." +
            "<br><b>Details:</b> Programmed and designed with Python 3.5 and PyQt5." +
            "<br><b>Programmer & Designer:</b> Fernando Daniel Jaime" +
            "<br><b>License:</b> GNU General Public License V3.0")
        pixmap = pixmap.scaled(120, 110)
        msg.setIconPixmap(pixmap)
        msg.exec_()


def main():
    app = QApplication(sys.argv)

    ex = Multitool()
    sys.exit(app.exec_())


if __name__ == '__main__':
    import sys
    main()

