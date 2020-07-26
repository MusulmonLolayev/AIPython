import sys

from PyQt5.QtWidgets import QApplication

from projects.magdiss_fris.windows.Introduction import Introduction

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Introduction()
    window.show()
    sys.exit(app.exec_())