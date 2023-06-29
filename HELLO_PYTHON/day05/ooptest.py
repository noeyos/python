class LeeJY:
    def __init__(self):
        self.cntCompany = 10
    def hit(self, punch):
        self.cntCompany += punch

class Biden:
    def __init__(self):
        self.headColor = "white"
    def dye(self):
        self.headColor = "red"

class Musk:
    def __init__(self):
        self.cntSat = 1000
    def launch(self):
        self.cntSat += 10
        
class EunBi(LeeJY, Biden, Musk):
    def __init__(self):
        LeeJY.__init__(self)
        Biden.__init__(self)
        Musk.__init__(self)

if __name__ == '__main__':
    e = EunBi()
    print(e.cntCompany)
    print(e.headColor)
    print(e.cntSat)
    e.hit(50)
    e.dye()
    e.launch()
    print(e.cntCompany)
    print(e.headColor)
    print(e.cntSat)