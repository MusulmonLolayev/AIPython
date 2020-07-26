# systems and PyQt5
# Get os directories
import os

# AI libraries
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, QMessageBox, QFileDialog, QVBoxLayout, QWidget, QTableWidgetItem, \
    QTableWidget, QSplitter, QHeaderView

from projects.magdiss_fris.func.methods import Normalizing_Estmation, Fris, ToFormNumpy
from projects.magdiss_fris.windows.Prediction import Prediction
from usingpackages.ctypesapi.cml import find_shell, find_noisy, find_standard, compactness

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

class MainWindow(QMainWindow):

    def __init__(self, fpath=None):
        super().__init__()
        self.initUI()

        self.cal = 0

        self.fpath = fpath

        if self.fpath:
            self.FillTable()

    def FillTable(self):
        try:
            # Fill the objects table with data
            self.X, self.types, self.y = ToFormNumpy(self.fpath)

            self.y -= 1

            #self.y[self.y == 2] = 0

            self.table.setRowCount(self.X.shape[0])
            self.table.setColumnCount(self.X.shape[1])

            for i in range(self.X.shape[0]):
                for j in range(self.X.shape[1]):
                    self.table.setItem(i, j, QTableWidgetItem("{:0.4f}".format(self.X[i, j])))

            # Set names of columns of result table
            names = ['1-sinf qobiq obyketlari', '2-sinf qobiq obyketlari',
                     '1-sinf shovqin obyketlari', '2-sinf shovqin obyketlari',
                     '1-sinf etalon obyketlari', '2-sinf etalon obyketlari',
                     '1-sinf kompaktligi', '2-sinf kompaktligi',
                     'Tanlanmaning kompaktligi'
                     ]
            self.result.setColumnCount(len(names))
            self.result.setHorizontalHeaderLabels(names)
            for i in range(len(names)):
                self.result.setColumnWidth(i, 150)

        except Exception as exc:
            self.close()
            QMessageBox.about(self, "Hisoblashda xatolik bor: ", str(exc))

    def initUI(self):
        # set icon
        self.setWindowIcon(QIcon('./images/icon.ico'))

        # load css
        sshFile = "./css/Aqua.qss"
        with open(sshFile, "r") as fh:
            self.setStyleSheet(fh.read())

        # Actions
        # Close window Action
        self.actExit = QAction(QIcon(BASE_PATH + '/images/quit.ico'), "Chiqish", self)
        self.actExit.setShortcut("Ctrl+Q")
        self.actExit.triggered.connect(self.close)
        # Open Data from Excel Action
        self.actOpen = QAction(QIcon(BASE_PATH + '/images/open.ico'), "Ochish", self)
        self.actOpen.setIconText("Ochish")
        self.actOpen.setShortcut("Ctrl+O")
        self.actOpen.triggered.connect(self.openFile)
        # Calculate
        self.actCalculate = QAction(QIcon(BASE_PATH + '/images/calculate.ico'), "Hisoblash", self)
        self.actCalculate.setShortcut("Ctrl+R")
        self.actCalculate.setIconText("Hisoblash")
        self.actCalculate.triggered.connect(self.calculate)
        # Show in graphic objects
        self.actShowGraph = QAction(QIcon(BASE_PATH + '/images/showgraphic.ico'), "Normirovka max min", self)
        self.actShowGraph.setShortcut("Ctrl+G")
        self.actShowGraph.setIconText("Normirovka")
        self.actShowGraph.triggered.connect(self.NormirovkaMM)

        # Normalize
        self.actShowPrediction = QAction(QIcon(BASE_PATH + '/images/prediction.ico'), "Normirovka w",
                                    self)
        self.actShowPrediction.setShortcut("Ctrl+P")
        self.actShowPrediction.setIconText("Normirovka w")
        #self.actShowPrediction.triggered.connect(self.NormirovkaW)

        # cross validation window
        self.actShowCrossValidation = QAction(QIcon(BASE_PATH + '/images/cross.ico'), "Cross Validation", self)
        self.actShowCrossValidation.setShortcut("Ctrl+C")
        self.actShowCrossValidation.setIconText("Cross Validation")
        self.actShowCrossValidation.triggered.connect(self.ShowCrossValidation)
        # menu
        self.mnuBar = self.menuBar();
        self.mnuFile = self.mnuBar.addMenu('&File')
        self.mnuFile.addAction(self.actOpen)
        self.mnuFile.addSeparator()
        self.mnuFile.addAction(self.actExit)
        # Servces
        self.mnuServce = self.mnuBar.addMenu('&Xizmatlar')
        self.mnuServce.addAction(self.actCalculate)
        self.mnuServce.addAction(self.actShowGraph)
        self.mnuServce.addAction(self.actShowPrediction)
        self.mnuServce.addAction(self.actShowCrossValidation)

        main_widget = QWidget()

        # Splitters
        self.splitter1 = QSplitter()
        self.splitter1.setOrientation(Qt.Horizontal)

        # centeral layout
        self.vbox = QVBoxLayout(main_widget)
        self.setCentralWidget(main_widget)

        # Table view
        self.table = QTableWidget()
        #self.table.clicked.connect(self.tblClicked)
        self.result = QTableWidget()
        self.vbox.addWidget(self.table)
        self.vbox.addWidget(self.splitter1)
        self.vbox.addWidget(self.result)

        # set status ber ready
        self.statusBar().showMessage('Ready')

        # set properteis of window
        self.setWindowTitle("Yaqin qo‘shni usuli algortimi asosida o‘rgatuvchi tanlamani saralash")
        self.setGeometry(300, 300, 0, 0)

    def NormirovkaMM(self):
        try:
            m1 = self.X.max(axis=0)
            m2 = self.X.min(axis=0)
            self.X[:, m1 != m2] = (self.X[:, m1 != m2] - m2[m1 != m2]) / (m1[m1 != m2] - m2[m1 != m2])

            for i in range(self.X.shape[0]):
                for j in range(self.X.shape[1]):
                    self.table.setItem(i, j, QTableWidgetItem("{:0.4f}".format(self.X[i, j])))

        except Exception as exc:
            QMessageBox.about(self, "Hisoblashda xatolik bor: ", str(exc))

    def NormirovkaW(self):
        try:
            Normalizing_Estmation(self.X, self.y)
            for i in range(self.X.shape[0]):
                for j in range(self.X.shape[1]):
                    self.table.setItem(i, j, QTableWidgetItem("{:0.4f}".format(self.X[i, j])))

        except Exception as exc:
            QMessageBox.about(self, "Hisoblashda xatolik bor: ", str(exc))

    def calculate(self):
        try:
            noisy_indx = find_noisy(self.X, self.y)
            noisies = self.count(noisy_indx, self.y)

            if self.cal > 0:
                X = self.X[noisy_indx == False]
                y = self.y[noisy_indx== False]
            else:
                X = self.X
                y = self.y

            shells = self.count(find_shell(X, y), y)
            etalons = self.count(find_standard(X, y), y)
            comp = compactness(X, y)


            self.result.setRowCount(self.cal + 1)

            self.result.setItem(self.cal, 0, QTableWidgetItem(str(shells[0])))
            self.result.setItem(self.cal, 1, QTableWidgetItem(str(shells[1])))


            self.result.setItem(self.cal, 2, QTableWidgetItem(str(noisies[0])))
            self.result.setItem(self.cal, 3, QTableWidgetItem(str(noisies[1])))


            self.result.setItem(self.cal, 4, QTableWidgetItem(str(etalons[0])))
            self.result.setItem(self.cal, 5, QTableWidgetItem(str(etalons[1])))

            self.result.setItem(self.cal, 6, QTableWidgetItem(str(comp[0])))
            self.result.setItem(self.cal, 7, QTableWidgetItem(str(comp[1])))
            self.result.setItem(self.cal, 8, QTableWidgetItem(str(comp[2])))
            self.cal += 1

        except Exception as exc:
            QMessageBox.about(self, "Hisoblashda xatolik bor: ", str(exc))

    def count(self, data, y):
        res = [0, 0]

        for i in range(y.shape[0]):
            if data[i] == True:
                res[y[i]] += 1
        return res

    def openFile(self):
        try:
            # open file dialog
            fnames = QFileDialog().getOpenFileName(self, 'Fayl ochish', '/Home')
            if len(fnames[0]) == 0:
                return
            self.fpath = fnames[0]

            self.FillTable()
        except Exception as exc:
            print(exc)
            QMessageBox.about(self, "Fayl ochishda xatolik bor", str(exc))

    def ShowCrossValidation(self):
        try:
            self.window = Prediction(self.X, self.y)
            self.window.show()
        except Exception as exc:
            QMessageBox.about(self, "Hisoblashda xatolik bor: ", str(exc))
