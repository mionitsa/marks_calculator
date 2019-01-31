import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, \
      QLineEdit
from widget1 import Ui_MainWindow
from PyQt5 import uic

def sredball(marksstr, ballstr):
    try:
        marks = [int(i) for i in marksstr.split()]
        avg = float(ballstr)
        slov = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}  # Словарь с колличеством каждой оценки, которое нужно будет получить
        summa = sum(marks)  # Сумма оценок
        lenn = len(marks)  # Колличесвто оценок
        your_avg = float(str(summa / lenn)[:4])  # Подсчитываем нынешний средний балл
        marks = [5, 4, 3, 2, 1]
        vivod = []
        vivodstr = str(
            'Ваш средний балл: ' + str(your_avg) + '. Для достижения требуемого среднего балла вам нужно получить:')
        if avg > 5:
            return 'Введенный требуемый средний балл не коректен.'

        if your_avg >= avg:
            return str('Ваш средний балл: ' + str(
                your_avg) + '. Требуемый средний балл уже достигнут. Продолжайте получать хорошие оценки! ;)')

        if avg == 5 and your_avg != 5:
            return str(
                'Ваш средний балл: ' + str(your_avg) + ', к сожалению, вы не сможете достигнуть требуемого балла. :(')

        if avg == 0 and your_avg != 0:
            return str(
                'Ваш средний балл: ' + str(your_avg) + ', к сожалению, вы не сможете достигнуть требуемого балла. :(')

        for i in range(int(5 - avg // 1)):

            ocenka = marks[i]

            summa_plus = 0  # Сумма оценок, которые мы прибавим
            lenn_plus = 0  # Сколько оценок мы прибавим
            avgg = your_avg  # Средний балл, который будет изменяться для цикла

            while avgg <= avg:  # Прибавляем оценку и получаем новый средний балл,сравниваем с требуемым

                slov[ocenka] += 1
                summa_plus += ocenka
                lenn_plus += 1
                avgg = (summa + summa_plus) / (lenn + lenn_plus)

        for i in slov:
            if slov[i] != 0:
                vivod.append((i, slov[i]))

        for i in vivod:
            vivodstr += str('\n' + str(i[0]) + ' в колличестве ' + str(i[1]))

        return vivodstr

    except Exception:
        return 'Ввод не корректен. '

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):  
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add)
        self.pushButton.clicked.connect(self.start)

    def start(self):
        self.ex1 = MyDialog()
        self.close()
        
    def add(self):
        global marks1, avg1
        marks1 = self.lineEdit.text()
        avg1 = self.lineEdit_2.text()
        
    
    
        
class MyDialog(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('widget2.ui', self)
        self.run()
        self.show()
        
        
    def run(self):
        self.label.setText(sredball(str(marks1),str(avg1)))
    
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec())

