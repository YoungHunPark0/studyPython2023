# 콤보박스
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class YourApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self): # initui 지역변수.  전역변수 - self.~ 내클래스로 만들게
        self.lblOption = QLabel('선택값 : ', self)
        self.lblOption.move(20, 20)

        cbOption = QComboBox(self)
        cbOption.addItem('Option1')
        cbOption.addItem('Option2')
        cbOption.addItem('Option3')
        cbOption.addItem('Option4')
        cbOption.addItem('Option5')
        cbOption.move(20, 40)   # 실행시 박스를 누를때 마다 시그널발생 시그널 함수- 슬롯함수(ex def.~)
        cbOption.activated[str].connect(self.onActivated) # connect 슬롯함수랑 연결

        # 필수 설정
        self.setWindowTitle('콤보박스')
        self.setGeometry(300, 300, 300, 300)
        self.show()
    
    def onActivated(self, text):
        self.lblOption.setText('선택값 :' + text)
        self.lblOption.adjustSize() # 글자수 만큼 라벨 넓이를 조정 - 다 표현됨 사이즈 안늘리면 글자잘림
        
    
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

