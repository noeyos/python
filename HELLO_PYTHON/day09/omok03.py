from PyQt5 import QtWidgets, uic, QtGui
import sys
from PyQt5.Qt import QPushButton, QSize, QIcon

form_window = uic.loadUiType("omok02.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag_bw = True
        
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,2,1,2,0, 0,0,0,0,0],
            [0,1,0,0,0, 0,0,0,0,0],
            [0,0,1,2,0, 0,0,0,0,0],
            [0,0,1,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
        ]
        
        self.pb2D = [
                                                                
        ]
        for i in range(10):
            line = []
            for j in range(10):
                btn = QPushButton("",self)
                btn.setIcon(QtGui.QIcon('0.png'))
                btn.setIconSize(QSize(40,40))
                btn.setGeometry(40 * j,40 * i,40,40)
                btn.setToolTip("{},{}".format(i,j))
                btn.clicked.connect(self.myclick)
                line.append(btn)
            self.pb2D.append(line)
                
        self.myrender()
        self.show()
        
    def checkDownRight(self, i,j,stone):
        pass
    
    def checkDownLeft(self, i,j,stone):
        pass
    
    def checkUpRight(self, i,j,stone):
        pass
    
    def checkUpLeft(self, i,j,stone):
        pass
    
    def checkRight(self, i,j,stone):
        cnt = 0
        
        while(True):
            j+=1
            if j > 0:
                return cnt
                
            if(self.arr2D[i][j] == stone):
                cnt+=1
            else:
                return cnt
    
    def checkLeft(self, i,j,stone):
        cnt = 0
        
        while(True):
            j-=1
            if j < 0:
                return cnt
                
            if(self.arr2D[i][j] == stone):
                cnt+=1
            else:
                return cnt
    
        
    def checkDown(self, i, j, stone):
        cnt = 0
        try:
            while(True):
                i+=1
                
                if i < 0:
                    return cnt
                    
                if(self.arr2D[i][j] == stone):
                    cnt+=1
                else:
                    return cnt
        except:
            return cnt
            
    def checkUp(self, i, j, stone):
        cnt = 0
        
        while(True):
            i-=1
            if i < 0:
                return cnt
                
            if(self.arr2D[i][j] == stone):
                cnt+=1
            else:
                return cnt
        
        
    def myclick(self):
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2D[i][j] != 0:
            return
        
        stone = -1
        
        if self.flag_bw:
            self.arr2D[i][j] = 1
            stone = 1
        else:
            self.arr2D[i][j] = 2
            stone = 2
        
        up = self.checkUp(i,j,stone)
        dw = self.checkDown(i,j,stone)
        le = self.checkLeft(i,j,stone)
        ri = self.checkRight(i,j,stone)
        ul = self.checkUpLeft(i,j,stone)
        ur = self.checkUpRight(i,j,stone)
        dl = self.checkDownLeft(i,j,stone)
        dr = self.checkDownRight(i,j,stone)
        print(le)         
            
        self.myrender()
        
        self.flag_bw = not self.flag_bw
        
        # GPT 방식
        # tooltip = self.sender().toolTip()
        # x, y = map(int, tooltip.split(','))
        # if self.arr2D[x][y] == 0:
        #     self.arr2D[x][y] = 1
        # elif self.arr2D[x][y] == 1:
        #     self.arr2D[x][y] = 2
        # elif self.arr2D[x][y] == 2:
        #     self.arr2D[x][y] = 0
        # self.myrender()
        # print(self.pb2D)
    
    def myrender(self):
        for i in range(10):
            for j in range(10):
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