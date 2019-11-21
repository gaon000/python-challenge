import xlrd
import random
from tkinter import *

wb=xlrd.open_workbook("test.xls")
ws=wb.sheet_by_index(0)

a = [x for x in range(1,3001)]
random.shuffle(a)

class english:

    def __init__(self, indexList, ws):
        self.indexList = indexList
        self.ws = ws
        self.root = Tk()
        self.lbl = Label(self.root, text = """click the button "new word" """)
        self.lbl.grid(row = 0, column = 1)
        self.lbl2 = Label(self.root, text = "한글뜻: ")
        self.lbl2.grid(row = 1, column = 0)
        self.entry = Entry(self.root)
        self.entry.grid(row = 1, column = 1)
        self.ent = Button(self.root, text = "check", command = self.enter)
        self.ent.grid(row = 2, column = 1)
        self.new = Button(self.root, text = 'new word',command = self.newWord)
        self.new.grid(row = 3, column = 1)
        self.lbl3 = Label(self.root, text = "정답여부")
        self.lbl3.grid(row = 4, column = 1)
        self.root.mainloop()
    def newWord(self):
        self.index = self.indexList.pop()
        self.lbl.configure(text = ws.cell_value(self.index,1))
    def enter(self):
        if self.entry.get() == self.ws.cell_value(self.index,2):
            self.lbl3.configure(text = "정답")
        else:
            self.lbl3.configure(text = f"정답은 {ws.cell_value(self.index,2)}")
"""
while 1:
    index = a.pop()
    print(ws.cell_value(index,1))
    ans = input("한글 뜻:")
    if ans == ws.cell_value(index,2):
        print("정답")
    else:
        #print("정답은 %s"%ws.cell_value(index,2))
        print(f"{index}문제 정답은 {ws.cell_value(index,2)}")
"""
if __name__ == "__main__":
    english(a,ws)