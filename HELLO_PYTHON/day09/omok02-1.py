from PyQt5 import QtWidgets, uic, QtGui
import sys
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.Qt import QPixmap, QSize
form_window = uic.loadUiType("omok02.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag_bw = True
        
        for i in range(10):
            for j in range(10):
                pb = QPushButton(self)
                pb.setIcon(QtGui.QIcon('0.png'))
                pb.setIconSize(QSize(40, 40))
                pb.setGeometry(j * 40, i * 40, 40, 40)
                pb.clicked.connect(self.myclick)
 
        self.show()

        
    def myclick(self):
        if self.flag_bw:
            self.sender().setIcon(QtGui.QIcon('1.png'))
        else:
            self.sender().setIcon(QtGui.QIcon('2.png'))
            
        self.flag_bw = not self.flag_bw
                    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainWindow()
    sys.exit(app.exec_())

    