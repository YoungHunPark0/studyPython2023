# 체크박스, 라디오버튼
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class YourApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cbShowTitle = QCheckBox('Show Title', self)
        cbShowTitle.move(20, 20) # 절대배치
        cbShowTitle.toggle()
       # signal 종류 stateChanged
       # connect() 매개변수 -> 슬롯함수
        cbShowTitle.stateChanged.connect(self.changeTitle)

        cbKorea = QCheckBox('한국', self)
        cbKorea.move(20, 40)
        cbKorea.stateChanged.connect(self.checkKorea)
    
        rbMale = QRadioButton('남성', self)
        rbMale.move(150, 20)
        rbMale.setChecked(True)
        rbFemale = QRadioButton('여성', self)
        rbFemale.move(150, 40)

        # 필수 설정
        self.setWindowTitle('버튼')
        self.setGeometry(300, 300, 300, 300)
        self.show()
    
    def checkKorea(self, state):
        if state == Qt.CheckState.Checked:
            self.setWindowTitle('나는 한국인')
        else:
            self.setWindowTitle('나는 머지?')


    def changeTitle(self, state):
        if state == Qt.CheckState.Checked: # Qt.Checked도 사용가능, checkstate 생략가능
            self.setWindowTitle('체크박스 체크') # 제목표시줄에 넣음
        else:
            self.setWindowTitle('체크박스 체크해제')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YourApp()
    sys.exit(app.exec_())

