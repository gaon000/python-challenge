import xlrd
import random

wb=xlrd.open_workbook("test.xls")
ws=wb.sheet_by_index(0)

a = [x for x in range(1,3001)]
random.shuffle(a)
while 1:
    index = a.pop()
    print(ws.cell_value(index,1))
    ans = input("한글 뜻:")
    if ans == ws.cell_value(index,2):
        print("정답")
    else:
        #print("정답은 %s"%ws.cell_value(index,2))
        print(f"{index}문제 정답은 {ws.cell_value(index,2)}")

        



