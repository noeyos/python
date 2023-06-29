from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QLabel
from PyQt5.Qt import QPixmap
form_window = uic.loadUiType("omok01.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.resize(100,100)
        pixmap = QPixmap("1.png")
        self.lbl.setPixmap(QPixmap(pixmap))
        
        

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainWindow()
    sys.exit(app.exec_())

    