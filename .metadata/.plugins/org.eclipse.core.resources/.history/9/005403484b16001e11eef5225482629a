from PyQt5 import QtWidgets, uic
import sys
form_window = uic.loadUiType("myqt07.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.drawStars)

    def drawStars(self):
        first = int(self.le_first.text())
        last = int(self.le_last.text())
        
        for i in range(last-first+1):
            star = ('*' * (i+first)) 
            print('*' * (i+first))
            self.te.append(star)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainWindow()
    sys.exit(app.exec_())

    