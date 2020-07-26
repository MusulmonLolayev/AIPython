from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMessageBox, QFileDialog, QVBoxLayout, QHBoxLayout, \
    QWidget, QLabel, QComboBox, \
    QLineEdit, QPushButton

from windows.Economy import MainWindow


class Introduction(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def Style(self, path):
        # load css
        with open(path, "r") as fh:
            self.setStyleSheet(fh.read())

    def initUI(self):
        self.Style("./css/Aqua.qss")
        # set icon
        self.setWindowIcon(QIcon('./images/icon.ico'))

        # Actions
        # Open Data from Excel Action
        self.actOpen = QAction(QIcon('./images/open.ico'), "Ochish", self)
        self.actOpen.setShortcut("Ctrl+O")
        self.actOpen.triggered.connect(self.openFile)

        # centeral layout
        self.vbox = QVBoxLayout(self)

        self.vbox.setAlignment(Qt.AlignTop)

        # Name of app
        lbl = QLabel(
            'Yaqin qo‘shni usuli algortimi asosida o‘rgatuvchi tanlamani saralash')
        lbl.setWordWrap(True)
        from PyQt5.QtWidgets import QStyle
        #lbl.setStyle(QStyle=QStyle("font-size: 28px;"))

        self.vbox.addChildWidget(lbl)

        # Select file
        hbox = QHBoxLayout()
        self.edit = QLineEdit()
        self.edit.setEnabled(False)
        hbox.addWidget(self.edit)

        # Browise button
        btnBrowse = QPushButton("Fayl")
        btnBrowse.clicked.connect(self.openFile)
        hbox.addWidget(btnBrowse)
        self.vbox.addLayout(hbox)

        btnOpenMain = QPushButton("Ochish")
        btnOpenMain.clicked.connect(self.openMain)
        self.vbox.addWidget(btnOpenMain)
        self.vbox.addStretch(4)

        # set properteis of window
        self.setWindowTitle("Yaqin qo‘shni usuli")
        self.setGeometry(300, 300, 640, 400)

    def colnum_string(self, n):
        string = ""
        while n > 0:
            n, remainder = divmod(n - 1, 26)
            string = chr(65 + remainder) + string
        return string

    def openMain(self):
        try:
            self.window = MainWindow(fpath=self.fnames[0]);
            self.window.showMaximized()
        except Exception as exc:
            QMessageBox.about(self, "Hisoblashda xatolik bor: ", str(exc))

    def openFile(self):
        try:
            # open file dialog
            self.fnames = QFileDialog().getOpenFileName(self, 'Fayl ochish', '/Home')
            if len(self.fnames[0]) == 0:
                return
            self.edit.setText(self.fnames[0])
        except Exception as exc:
            print(exc)
            QMessageBox.about(self, "Fayl ochishda xatolik bor", str(exc))