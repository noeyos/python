from PyQt5 import QtWidgets, uic, QtGui
import sys
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.Qt import QPixmap, QSize
form_window = uic.loadUiType("omok02.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        for i in range(10):
            for j in range(10):
                pb = QPushButton(self)
                pb.setIcon(QtGui.QIcon('0.png'))
                pb.setIconSize(QSize(40, 40))
                pb.setGeometry(j * 40, i * 40, 40, 40)
                pb.clicked.connect(self.myclick)
 
        self.show()

        
    def myclick(self):
        sender = self.sender()  # 이벤트를 발생시킨 버튼 가져오기        
        clicked = sender.property("clicked")
        
        if clicked:
            sender.setIcon(QtGui.QIcon('2.png'))
        else:
            sender.setIcon(QtGui.QIcon('1.png'))
            
        sender.setProperty("clicked", not clicked)
        sender.setIconSize(QSize(40, 40))
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainWindow()
    sys.exit(app.exec_())

    