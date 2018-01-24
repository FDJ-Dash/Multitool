#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyQt5 Multitool

This program puts together multiple widgets
on a single application.

Version: 0.3.1 beta

Author: Fernando Daniel Jaime
Last edited: January 2018
"""

from PyQt5.QtWidgets import ( QAction, QApplication,
    QHBoxLayout, QMainWindow, QMenu, QMessageBox,
    QStackedWidget, QSystemTrayIcon, QWidget)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

from mouseclicker.mouseclicker import MouseClicker
from screenShot.screenshot import Screenshot


class Multitool(QMainWindow, QWidget):
    def __init__(self):
        super(Multitool, self).__init__()

        self.statusbar = self.statusBar()
        self.statusBar().showMessage('Ready')

        self.stack1 = QWidget() # Mouse Clicker
        self.stack2 = QWidget() # Screenshot

        self.stack1UI() # Mouse Clicker
        self.stack2UI() # Screenshot

        self.Stack = QStackedWidget (self)
        self.Stack.addWidget (self.stack1) # Mouse Clicker
        self.Stack.addWidget (self.stack2) # Screenshot

        # General actions starts -------------------------------------
        exitAction = QAction(QIcon('icons/exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QApplication.instance().quit)

        newMultitoolAction = QAction(QIcon('icons/new.png'), '&New Multitool', self)
        newMultitoolAction.setShortcut('Ctrl+N')
        newMultitoolAction.setStatusTip('New Multitool')
        newMultitoolAction.triggered.connect(self.newMultitoolWindow)

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
        # General actions ends ---------------------------------------

        # Widgets actions starts -------------------------------------
        mouseClickerAction = QAction(QIcon('icons/mouse.png'),'Mouse Clicker', self)
        mouseClickerAction.setStatusTip('Mouse Clicker')
        mouseClickerAction.triggered.connect(lambda: self.display(0))

        screeenShotAction = QAction(QIcon('icons/screenshot.png'),'ScreenShot', self)
        screeenShotAction.setStatusTip('ScreenShot')
        screeenShotAction.triggered.connect(lambda: self.display(1))
        # Widget actions ends ----------------------------------------

        # Menu bar creation starts -----------------------------------
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newMultitoolAction)
        fileMenu.addAction(exitAction)

        viewMenu = menubar.addMenu('View')
        viewMenu.addAction(viewStatAction)
        viewMenu.addAction(viewToolbarAction)

        viewMenuWidget = QMenu('List widget', self)
        viewMenuWidget.addAction(mouseClickerAction)
        viewMenuWidget.addAction(screeenShotAction)
        viewMenu.addMenu(viewMenuWidget)

        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(aboutAction)
        # Menu bar creation ends -------------------------------------

        # Toolbar creation starts -------------------------------------
        self.toolbar1 = self.addToolBar('File')
        self.toolbar1.addAction(newMultitoolAction)

        self.toolbar2 = self.addToolBar('Widgets')
        self.toolbar2.addAction(mouseClickerAction)
        self.toolbar2.addAction(screeenShotAction)

        self.toolbar3 = self.addToolBar('Exit')
        self.toolbar3.addAction(exitAction)
        # Toolbar creation ends -------------------------------------

        self.setCentralWidget(self.Stack)
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
            self.toolbar2.show()
            self.toolbar3.show()
        else:
            self.toolbar1.hide()
            self.toolbar2.hide()
            self.toolbar3.hide()


    def minimizeToTray(self, state):
        if state:
            self.hide()
            self.trayIcon.showMessage(
                "Tray Program",
                "Application was minimized to tray",
                QSystemTrayIcon.Information,
                2000)


    def newMultitoolWindow(self):
        self.__init__()
        self.setGeometry(350, 350, 700, 400)


    # Stacked widgets added to layout start----------------------
    def stack1UI(self):
        self.layout = QHBoxLayout()
        self.layout.addWidget(MouseClicker())
        self.stack1.setLayout(self.layout)


    def stack2UI(self):
        self.layout = QHBoxLayout()
        self.layout.addWidget(Screenshot())
        self.stack2.setLayout(self.layout)


    def display(self,i):
        self.Stack.setCurrentIndex(i)
    # Stacked widgets added to layout end------------------------


    def about(self):
        pixmap = QPixmap('icons/biohazard.svg')
        msg = QMessageBox(QMessageBox.Information, 'About Multitool',
            "<b>Aplication name:</b> Multitool" +
            "<br> <b>Version:</b> V0.3.1 beta" +
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

