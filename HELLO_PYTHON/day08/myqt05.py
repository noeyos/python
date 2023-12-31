from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QMessageBox
form_window = uic.loadUiType("myqt05.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        self.pb0.clicked.connect(self.myclick)
        self.pb_call.clicked.connect(self.mycall)

    def myclick(self):
        imsi = self.sender()
        str_old = self.le.text()
        str_new = imsi.text()
        self.le.setText(str_old + str_new)

        
    def mycall(self):
        QMessageBox.about(self, '전화기', '%s로 전화를 겁니다'%(self.le.text()))
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainWindow()
    sys.exit(app.exec_())

    