# 파일다이얼로그
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction('Open', self)
        openFile.setShortcut('Ctrl+0')
        openFile.setStatusTip('파일열기')
        openFile.triggered.connect(self.onClicked)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(openFile)

        # 필수설정
        self.setWindowTitle('파일다이얼로그 위젯')
        self.setGeometry(300, 300, 300, 300)
        self.show() # 실행시 종료 alt+f4

    def onClicked(self):
        fname = QFileDialog.getOpenFileName(self, '파일열기', './') # './'==현재위치

        if fname[0]:  # 파일을 선택했다면
            file = open(fname[0], 'rt', encoding='utf-8') # r하고 text를 읽는다
            with file:
                data = file.read()
                self.textEdit.setText(data)
            
            file.close()

        QMessageBox.about(self, '성공', '로드했습니다.') # 많이쓰니 알아두기
    
    def closeEvent(self, event): # closeEvent = 창에 종료(x) 누르면 자동발생하는 시그널이기때문에 재정의 하는 과정
        reply = QMessageBox.question(self, '종료', '정말 종료하시겠습까?', 
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept() # 프로그램 종료
        else:
            event.ignore() # 그대로 프로그램 계속

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())