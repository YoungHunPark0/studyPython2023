# https://wikidocs.net/21920 참조
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime 

class MyApp(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # 메뉴바 - 액션
        actExit = QAction(QIcon('./Day09/exit.png'), 'Exit', self)
        actExit.setShortcut('Ctrl+Q') # 단축키 지정(setshortcut())
        actExit.setStatusTip('앱 종료')
        actExit.triggered.connect(qApp.quit)
        
        actSave = QAction(QIcon('./Day09/save.png'), 'Save', self)
        actSave.setShortcut('Ctrl+S')
        actSave.setStatusTip('저장')

        meunbar = self.menuBar()
        meunbar.setNativeMenuBar(False)
        filemenu = meunbar.addMenu('&File')
        filemenu.addAction(actExit)

        # 툴바
        toolbar = self.addToolBar('MainToolBar') 
        # 툴바타이틀(maintoolbar)은 없어도 됨
        toolbar.addAction(actSave)
        toolbar.addAction(actExit)

        # 상태바
        now = QDate.currentDate() # 현재 일자
        time = QTime.currentTime() # 현재 시간
        self.statusBar().showMessage(now.toString('yyyy-MM-dd') + ' ' + time.toString()) 
        self.setWindowIcon(QIcon('./Day09/iot.png'))
        #Qmainwindow 를 써야 stausbar가 나옴
        # GUI 화면 설정
        self.setWindowTitle('Bar Window')
        self.move(50, 50)
        self.resize(400, 200)
        self.setCenter()
        self.show() # self.show가 없으면 아무것도 안나옴. 핵심!!    

    # 화면 중심 셋팅
    def setCenter(self):
        qr = self.frameGeometry() # 창 자기자신의 위치값
        cp = QDesktopWidget().availableGeometry().center() # 모니터화면 중심
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())