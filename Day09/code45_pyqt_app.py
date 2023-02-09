# https://wikidocs.net/21920 참조
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # GUI 화면 설정
        self.setWindowTitle('Simple Window')
        # self.move(1440 // 2 - 200, 900 // 2 - 100) 정중앙 위치잡기 
        # 실행하면 기본 중앙인데 move 사용 위치 바꿈
        # 왼쪽상단기준 0,0 디스플레이 해상도에 따라 다른데 
        # 1440이면 -400인 1040까지가능(1440이 아예 끝)
        self.resize(400, 200)
        self.show() # self.show가 없으면 아무것도 안나옴. 핵심!!    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())