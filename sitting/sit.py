import random
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
form = uic.loadUiType("untitled.ui")[0]

class window(QMainWindow,form):

    def __init__(self):

        self.doctorSaid = ["I'm genius", "Hello Doctor", "MR.Hwang", "dropping out of school", "Docotr said"]
        self.dic = {}
        super().__init__()
        self.setupUi(self)
        self.button_shuffle.clicked.connect(self.shuffle)
    
    def shuffle(self):
        
        i = 0
        while i != 19:
            self.sit = [x for x in range(1,20)]
            random.shuffle(self.sit)
            for i in range(1,20):
                a = random.choice(self.sit)
                if self.dic.get(i,0) == a:
                    break
                self.sit.remove(a)
                self.dic[i] = a

        self.label_1.setText(str(self.dic[1]))
        self.label_2.setText(str(self.dic[2]))
        self.label_3.setText(str(self.dic[3]))
        self.label_4.setText(str(self.dic[4]))
        self.label_5.setText(str(self.dic[5]))
        self.label_6.setText(str(self.dic[6]))
        self.label_7.setText(str(self.dic[7]))
        self.label_8.setText(str(self.dic[8]))
        self.label_9.setText(str(self.dic[9]))
        self.label_10.setText(str(self.dic[10]))
        self.label_11.setText(str(self.dic[11]))
        self.label_12.setText(str(self.dic[12]))
        self.label_13.setText(str(self.dic[13]))
        self.label_14.setText(str(self.dic[14]))
        self.label_15.setText(str(self.dic[15]))
        self.label_16.setText(str(self.dic[16]))
        self.label_17.setText(str(self.dic[17]))
        self.label_18.setText(str(self.dic[18]))
        self.label_19.setText(str(self.dic[19]))
        self.doctor.setText(random.choice(self.doctorSaid))
        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = window()
    win.show()
    app.exec_()