#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PyQt5 Multitool

This program puts together multiple widgets
on a single application.

Version: 0.7 beta

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
from player.player import (VideoWidget, PlaylistModel, PlayerControls,
    FrameProcessor, HistogramWidget, Player)
from calculator.calculator import Button, Calculator
from camera.camera import Camera, ImageSettings, VideoSettings
from tetrix.tetrix import TetrixWindow, TetrixBoard, TetrixPiece


class Multitool(QMainWindow, QWidget):
    def __init__(self):
        super(Multitool, self).__init__()

        self.statusbar = self.statusBar()
        self.statusBar().showMessage('Ready')

        self.trayActions()
        self.trayMenu()
        self.trayIcon.setIcon(QIcon('icons/biohazard.svg'))
        self.trayIcon.show()

        self.stack1 = QWidget() # Mouse Clicker
        self.stack2 = QWidget() # Screenshot
        self.stack3 = QWidget() # Player
        self.stack4 = QWidget() # Calculator
        self.stack5 = QWidget() # Camera
        self.stack6 = QWidget() # Tetrix

        self.stack1UI() # Mouse Clicker
        self.stack2UI() # Screenshot
        self.stack3UI() # Player
        self.stack4UI() # Calculator
        self.stack5UI() # Camera
        self.stack6UI() # Tetrix

        self.Stack = QStackedWidget (self)
        self.Stack.addWidget (self.stack1) # Mouse Clicker
        self.Stack.addWidget (self.stack2) # Screenshot
        self.Stack.addWidget (self.stack3) # Player
        self.Stack.addWidget (self.stack4) # Calculator
        self.Stack.addWidget (self.stack5) # Camera
        self.Stack.addWidget (self.stack6) # Tetrix

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

        minimizeToTrayAction = QAction('Minimize to Tray', self, checkable=True)
        minimizeToTrayAction.setStatusTip('Minimize to Tray')
        minimizeToTrayAction.setChecked(False)
        minimizeToTrayAction.triggered.connect(self.minimizeToTray)
        # General actions ends ---------------------------------------

        # Widgets actions starts -------------------------------------
        mouseClickerAction = QAction(QIcon('icons/mouse.png'),'Mouse Clicker', self)
        mouseClickerAction.setStatusTip('Mouse Clicker')
        mouseClickerAction.triggered.connect(lambda: self.display(0))

        screeenShotAction = QAction(QIcon('icons/screenshot.png'),'ScreenShot', self)
        screeenShotAction.setStatusTip('ScreenShot')
        screeenShotAction.triggered.connect(lambda: self.display(1))

        playerAction = QAction(QIcon('icons/player.jpeg'),'Player', self)
        playerAction.setStatusTip('Player')
        playerAction.triggered.connect(lambda: self.display(2))

        calculatorAction = QAction(QIcon('icons/calc.ico'),'Calculator', self)
        calculatorAction.setStatusTip('Calculator')
        calculatorAction.triggered.connect(lambda: self.display(3))

        cameraAction = QAction(QIcon('icons/camera.jpeg'),'Camera', self)
        cameraAction.setStatusTip('Camera')
        cameraAction.triggered.connect(lambda: self.display(4))

        tetrixAction = QAction(QIcon('icons/tetrix.png'),'Tetrix', self)
        tetrixAction.setStatusTip('Tetrix')
        tetrixAction.triggered.connect(lambda: self.display(5))
        # Widget actions ends ----------------------------------------

        # Menu bar creation starts -----------------------------------
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newMultitoolAction)
        fileMenu.addAction(exitAction)

        viewMenu = menubar.addMenu('View')
        viewMenu.addAction(viewStatAction)
        viewMenu.addAction(viewToolbarAction)
        viewMenu.addAction(minimizeToTrayAction)

        viewMenuWidget = QMenu('List widget', self)
        viewMenuWidget.addAction(mouseClickerAction)
        viewMenuWidget.addAction(screeenShotAction)
        viewMenuWidget.addAction(playerAction)
        viewMenuWidget.addAction(calculatorAction)
        viewMenuWidget.addAction(cameraAction)
        viewMenu.addMenu(viewMenuWidget)

        gamesMenu = menubar.addMenu('&Games')
        gamesMenu.addAction(tetrixAction)

        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(aboutAction)
        # Menu bar creation ends -------------------------------------

        # Toolbar creation starts -------------------------------------
        self.toolbar1 = self.addToolBar('File')
        self.toolbar1.addAction(newMultitoolAction)

        self.toolbar2 = self.addToolBar('Widgets')
        self.toolbar2.addAction(mouseClickerAction)
        self.toolbar2.addAction(screeenShotAction)
        self.toolbar2.addAction(playerAction)
        self.toolbar2.addAction(calculatorAction)
        self.toolbar2.addAction(cameraAction)

        self.toolbar3 = self.addToolBar('Games')
        self.toolbar3.addAction(tetrixAction)

        self.toolbar4 = self.addToolBar('Exit')
        self.toolbar4.addAction(exitAction)
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
            self.toolbar4.show()
        else:
            self.toolbar1.hide()
            self.toolbar2.hide()
            self.toolbar3.hide()
            self.toolbar4.hide()


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


    def stack3UI(self):
        self.layout = QHBoxLayout()
        self.layout.addWidget(Player(sys.argv[1:]))
        self.stack3.setLayout(self.layout)


    def stack4UI(self):
        self.layout = QHBoxLayout()
        self.layout.addWidget(Calculator())
        self.stack4.setLayout(self.layout)


    def stack5UI(self):
        self.layout = QHBoxLayout()
        self.layout.addWidget(Camera())
        self.stack5.setLayout(self.layout)


    def stack6UI(self):
        self.layout = QHBoxLayout()
        self.layout.addWidget(TetrixWindow())
        self.stack6.setLayout(self.layout)


    def display(self,i):
        self.Stack.setCurrentIndex(i)
    # Stacked widgets added to layout end------------------------


    def trayActions(self):
        self.minimizeAction = QAction(QIcon('icons/minimize.png'), "Mi&nimize", self,
                triggered=self.hide)
        self.maximizeAction = QAction(QIcon('icons/maximize.jpeg'), "Ma&ximize", self,
                triggered=self.showMaximized)
        self.restoreAction = QAction(QIcon('icons/restore.png'), "&Restore", self,
                triggered=self.showNormal)
        self.quitAction = QAction(QIcon('icons/exit.png'), "&Quit", self,
                triggered=QApplication.instance().quit)


    def trayMenu(self):
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(self.minimizeAction)
        self.trayIconMenu.addAction(self.maximizeAction)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)

        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)


    # When closing from title bar close button, it will minimize to tray
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "This action will minimize to tray.", QMessageBox.Yes |
            QMessageBox.Cancel, QMessageBox.Cancel)

        if reply == QMessageBox.Yes:
            self.hide()
            self.trayIcon.showMessage(
                "Tray Program",
                "Application was minimized to tray",
                QSystemTrayIcon.Information,
                2000)
            event.accept()
        else:
            self.show()
            event.ignore()


    def about(self):
        pixmap = QPixmap('icons/biohazard.svg')
        msg = QMessageBox(QMessageBox.Information, 'About Multitool',
            "<b>Aplication name:</b> Multitool" +
            "<br> <b>Version:</b> V0.7 beta" +
            "<br><b>Description:</b> This application puts together many" +
            "<br>widgets into a single application." +
            "<br><b>Details:</b> Programmed and designed with Python 3.5 and PyQt5." +
            "<br><b>Programmer & Designer:</b> Fernando Daniel Jaime" +
            "<br><b>License:</b> GNU General Public License V3.0")
        pixmap = pixmap.scaled(120, 110)
        msg.setIconPixmap(pixmap)
        msg.exec_()


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.Cancel, QMessageBox.Cancel)

            if reply == QMessageBox.Yes:
                self.statusBar().showMessage('Quiting...')
                QApplication.instance().quit()
            else:
                event.ignore()


    # Multitool context menu
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        quitAct = cmenu.addAction(QIcon('icons/exit.png'), "Quit")
        cmenu.addSeparator()
        newMultitoolAction = cmenu.addAction(QIcon('icons/new.png'),
            "New Multitool")
        minimizeAction = cmenu.addAction(QIcon('icons/minimize.png'),
            "Minimize to tray")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            QApplication.instance().quit()
        if action == newMultitoolAction:
            self.__init__()
            self.setGeometry(350, 350, 700, 400)
        if action == minimizeAction:
            self.hide()
            self.trayIcon.showMessage(
                "Tray Program",
                "Application was minimized to tray",
                QSystemTrayIcon.Information,
                2000)


def main():
    app = QApplication(sys.argv)

    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "Systray",
                "I couldn't detect any system tray on this system.")
        sys.exit(1)

    QApplication.setQuitOnLastWindowClosed(False)

    ex = Multitool()
    sys.exit(app.exec_())


if __name__ == '__main__':
    import sys
    main()

