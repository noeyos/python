from PyQt5 import QtWidgets, uic, QtGui
import sys
from PyQt5.Qt import QPushButton, QSize, QIcon
from PyQt5.QtWidgets import QMessageBox

form_window = uic.loadUiType("omok04_20.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag_over = False
        self.flag = True
        
        self.arr2D = [[] for _ in range(20)]

        for i in range(20):
            for j in range(20):
                self.arr2D[i].append(0)
        
        self.pb2D = [
                                                                
        ]
        
        for i in range(20):
            line = []
            for j in range(20):
                btn = QPushButton("",self)
                btn.setIcon(QtGui.QIcon('0.png'))
                btn.setIconSize(QSize(40,40))
                btn.setToolTip("{},{}".format(i,j))
                btn.setGeometry(40 * j,40 * i,40,40)
                btn.clicked.connect(self.myclick)
                line.append(btn)
            self.pb2D.append(line)
                
        self.myrender()
        
        self.pb.clicked.connect(self.my_reset)
        self.show()
    
    def my_reset(self):
        self.flag_over = False
        self.flag = True
        for i in range(20):
            for j in range(20):
                self.arr2D[i][j]=0
        
        self.myrender()
    
    
    def checkUP(self, i,j,stone):
        cnt = 0
        try:
            while True :
                i -= 1
                
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
            
    def checkDW(self, i,j,stone):
        cnt = 0
        try:
            while True :
                i += 1
                
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkLE(self, i,j,stone):
        cnt = 0
        try:
            while True :
                j -= 1
                
                if j < 0:
                    return cnt
                
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
            
    def checkRI(self, i,j,stone):
        cnt = 0
        try:
            while True :
                j += 1
                
                if j < 0:
                    return cnt
                
                if i < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkUR(self, i,j,stone):
        cnt = 0
        try:
            while True :
                i += 1
                j += 1
                
                if j < 0:
                    return cnt
                
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkUL(self, i,j,stone):
        cnt = 0
        try:
            while True :
                i += 1
                j -= 1
                
                if j < 0:
                    return cnt
                
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkDR(self, i,j,stone):
        cnt = 0
        try:
            while True :
                i -= 1
                j += 1
                
                if j < 0:
                    return cnt
                
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkDL(self, i,j,stone):
        cnt = 0
        try:
            while True :
                i -= 1
                j -= 1
                
                if j < 0:
                    return cnt
                
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt

    
    def myclick(self):
        if self.flag_over == True:
            return
        
        a = self.sender().toolTip()
        text = a.split(",")
        i = int(text[0])
        j = int(text[1])
        
        if self.arr2D[i][j] > 0:
            return
        
        stone = -1

        if self.flag:
            self.arr2D[i][j] = 1
            stone = 1
        else :
            self.arr2D[i][j] = 2
            stone = 2
        
        up = self.checkUP(i,j,stone)
        dw = self.checkDW(i,j,stone)
        ri = self.checkRI(i, j, stone)
        le = self.checkLE(i, j, stone)
        
        ur = self.checkUR(i, j, stone)
        ul = self.checkUL(i, j, stone)
        dr = self.checkDR(i, j, stone)
        dl = self.checkDL(i, j, stone)
        print("----------------")
        print("up",up)
        print("dw",dw)
        print("ri",ri)
        print("le",le)
        print("ur",ur)
        print("le",le)
        print("ur",ur)
        print("----------------")
        
        d1 = le + ri + 1
        d2 = ul + dr + 1
        d3 = up + dw + 1
        d4 = ur + dl + 1    
        
        self.myrender()
        
        if (d1 == 5) or (d2 == 5) or (d3 == 5) or (d4 == 5):
            if self.flag:
                QMessageBox.about(self, '오목', '흑돌 승리!')
            else :
                QMessageBox.about(self, '오목', '백돌 승리!')
            self.flag_over = True

        self.flag = not self.flag
            

        
    def myrender(self):
        for i in range(20):
            for j in range(20):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
                
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainWindow()
    sys.exit(app.exec_())