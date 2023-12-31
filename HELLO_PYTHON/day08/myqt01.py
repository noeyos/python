from PyQt5 import QtWidgets, uic
import sys
form_window = uic.loadUiType("myqt01.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        self.lbl.setText("Good Evening")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainWindow()
    sys.exit(app.exec_())

    