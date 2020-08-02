from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QMessageBox, \
    QVBoxLayout, QSpinBox, QCheckBox

from sklearn.model_selection import cross_val_score as CVS, KFold

from ai.own.classification import NearestNeighborClassifier_, NearestNeighborClassifier

import numpy as np

from usingpackages.ctypesapi.cml import find_shell, find_noisy, find_standard, compactness


class Prediction(QWidget):

    def __init__(self, X, y):
        super().__init__()

        self.X = X
        self.y = y

        self.initUI()

    def initUI(self):

        self.Style("./css/Aqua.qss")

        # set icon
        self.setWindowIcon(QIcon('./images/icon.ico'))

        # centeral layout
        self.hbox = QVBoxLayout(self)

        self.hbox.setAlignment(Qt.AlignTop)

        self.hbsettings = QHBoxLayout()
        #self.hbsettings.addStretch(6)

        self.lbhidden_layer = QLabel("Kfold bo'laklar soni")
        self.spNumberOfKFold = QSpinBox()
        self.spNumberOfKFold.setValue(5)
        self.spNumberOfKFold.setRange(2, 10)
        self.hbsettings.addWidget(self.lbhidden_layer)
        self.hbsettings.addWidget(self.spNumberOfKFold)

        self.chbIsNormalize = QCheckBox("Normirovka")
        self.hbsettings.addWidget(self.chbIsNormalize)

        self.chbIsNoisy = QCheckBox("Shovqin obyektlarni olib tashlash")
        self.hbsettings.addWidget(self.chbIsNoisy)

        # Calculate
        btnBrowse = QPushButton("Hisoblash")
        btnBrowse.clicked.connect(self.CalculatePrediction)
        self.hbsettings.addWidget(btnBrowse)

        self.hbox.addLayout(self.hbsettings)

        self.hbresult = QHBoxLayout()

        self.lbTextOfResult = QLabel("Sirpanuvchi nazorat bahosi: ")
        self.hbresult.addWidget(self.lbTextOfResult)

        self.hbox.addLayout(self.hbresult)

        # set properteis of window
        self.setWindowTitle("Yaqin qo'shni usulida baholash")
        self.setGeometry(200, 200, 200, 200)

    def Style(self, path):
        # load css
        with open(path, "r") as fh:
            self.setStyleSheet(fh.read())

    def CalculatePrediction(self):
        try:
            X = self.X.copy()
            y = self.y.copy()

            # Normalize
            if self.chbIsNormalize.isChecked():
                m1 = X.max(axis=0)
                m2 = X.min(axis=0)
                X[:, m1 != m2] = (X[:, m1 != m2] - m2[m1 != m2]) / (m1[m1 != m2] - m2[m1 != m2])

            """
            # clear noisy objects
            if self.chbIsNoisy.isChecked():
                noisy = find_noisy(X, y)

                X = X[noisy == False]
                y = y[noisy == False]

            """

            # Cross Validation
            k = self.spNumberOfKFold.value()
            k_fold = KFold(n_splits=k, shuffle=True, random_state=None)
            
            nn = NearestNeighborClassifier_(noisy=self.chbIsNoisy.isChecked())

            result = CVS(nn, X, y, cv=k_fold, n_jobs=4, scoring='accuracy').mean()

            self.lbTextOfResult.setText("Sirpanuvchi nazorat bahosi: {:.4%}".format(result))

        except Exception as exc:
            QMessageBox.about(self, "Cross validationda xatolik  xatolik bor: ", str(exc))