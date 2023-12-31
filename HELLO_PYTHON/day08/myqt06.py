from PyQt5 import QtWidgets, uic
import sys
from random import random
form_window = uic.loadUiType("myqt06.ui")[0]
    
    
class UiMainWindow(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.play)
        
    def play(self):
        mine = self.pte_mine.toPlainText()
        
        rnd = int(random()*3);
        print(rnd)
        com = ""
        if rnd == 0:
            com = "가위"
        elif rnd == 1:
            com ="바위"
        elif rnd ==2:
            com = "보"
        self.pte_com.setPlainText(com)
        
        if mine == com:
            self.pte_result.setPlainText("무승부")
        elif (mine == "바위" and com == "가위") or (mine == "가위" and com == "보") or (mine == "보" and com == "바위"):
            self.pte_result.setPlainText("승리")
        else:
            self.pte_result.setPlainText("패배")


        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainWindow()
    sys.exit(app.exec_())

    