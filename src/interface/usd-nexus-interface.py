from PySide2.QtWidgets import (
    QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QListWidget, QGroupBox, QScrollArea,
    QPushButton, QWidget, QSpacerItem, QSizePolicy )
from PySide2.QtCore import Qt 
from pxr import Usd, Sdf
import sys
import os
import stylesheets

"""
TODO

> add top label with usd logo and app name
> sort out stylesheets
> work on the config setup for assets / shots
> start working on interface from left to right
"""

class UsdNexus(QMainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUi()

    def initUi(self):

        self.setWindowTitle("USD Nexus")
        self.setGeometry(500, 200, 1400, 900)

        # ----- Top Bar Widget
        layoutTop = QHBoxLayout()
        topSpacer = QSpacerItem(1300, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.close    = QPushButton("X")
        self.minimise = QPushButton("-")
        layoutTop.addItem(topSpacer)
        layoutTop.addWidget(self.minimise)
        layoutTop.addWidget(self.close)

        for wgt in [self.close, self.minimise]:
            wgt.setFixedWidth(20)
            wgt.setFixedHeight(20)


        # ----- Departments Widget
        layoutDepartments    = QVBoxLayout()
        departmentsLabel     = QLabel("Departments : ")
        self.departmentsList = QListWidget()
        layoutDepartments.addWidget(departmentsLabel)
        layoutDepartments.addWidget(self.departmentsList)

        departmentsLabel.setStyleSheet(stylesheets.labelHeadingStyleSheet())
        self.departmentsList.setFixedWidth(250)


        # ----- Assets / Shots Widget
        layoutAssets = QVBoxLayout()
        assetsLabel  = QLabel("Assets / Shots : ")
        self.filterAssets = QLineEdit()
        self.assetsList   = QListWidget()
        layoutAssets.addWidget(assetsLabel)
        layoutAssets.addWidget(self.filterAssets)
        layoutAssets.addWidget(self.assetsList)



        # ----- Publishes Widget
        layoutPublishes = QVBoxLayout()
        publishesLabel  = QLabel("Publishes : ")
        self.publishesArea = QScrollArea()

        # TEMP TEMP TEMP
        contentWidget = QWidget()
        contentLayout = QVBoxLayout()

        for i in range(35):
            button = QPushButton("TEMP")
            contentLayout.addWidget(button)

        contentWidget.setLayout(contentLayout)
        self.publishesArea.setWidget(contentWidget)
        layoutPublishes.addWidget(self.publishesArea)

        

        
        layoutInterface = QVBoxLayout()
        layoutMain      = QHBoxLayout()

        layoutMain.addLayout(layoutDepartments)
        layoutMain.addLayout(layoutAssets)
        layoutMain.addLayout(layoutPublishes)
        
        layoutInterface.addLayout(layoutTop)
        layoutInterface.addLayout(layoutMain)

        centralWidget = QWidget()
        centralWidget.setLayout(layoutInterface) 
        self.setCentralWidget(centralWidget)
        
        self.setContentsMargins(8, 12, 8, 8)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("""QMainWindow { background-color: rgb(44, 49, 59); }""")
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv) if not QApplication.instance() else QApplication.instance()
    win = UsdNexus()
    win.show()
    sys.exit(app.exec_())