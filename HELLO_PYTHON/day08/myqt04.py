from PyQt5 import QtWidgets, uic
import sys
form_window = uic.loadUiType("myqt04.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.gugudan)
    
    def gugudan(self):
        dan = (int)(self.le.text())
        
        for i in range(1,9+1):
            sum = dan * i
            self.te.append(f"{dan} * {i} = {sum}")
            
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainWindow()
    sys.exit(app.exec_())
    

    