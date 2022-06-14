import sys
# 시스템 불러오기
from PyQt5 import uic
# 디자인 만든거 불러와야됨
from PyQt5.QtWidgets import *
#큐티위젯 불러오고
from PyQt5.QtGui import *
#gui 불러오기
import googletrans
#구글 트랜스불러오고


form_class = uic.loadUiType('ui/ui.ui')[0]
#ui안에 있는 유아이 불러오기 무조건 첫줄에서 유아이부터 불러와줘야함


class MyWindow(QMainWindow, form_class):
    def __init__(self):
    #q메인윈도우 상속받기 그 후 폼클래스를 상속받아야 쓸 수 있는 것임
        super().__init__() #부모 초기화자 호출 안하면 에러
        self.setupUi(self) #제작해놓은 ui.ui를 연결함
        self.setWindowTitle('구글한줄번역기') #윈도우타이틀
        self.setWindowIcon(QIcon('icons/google.png')) #아이콘 넣기
        self.statusBar().showMessage('Google Trans App v 1.0.0')

        self.p1.clicked.connect(self.trans_operation) # p1연결
        self.p2.clicked.connect(self.reset_operation) # p2연결
        
    def trans_operation(self): # 번역하기 버튼
        trans = googletrans.Translator()
        trans_str = self.ko.text() #한국어에 인풋을 받은걸 가져오는거임

        result_eng = trans.translate(trans_str, dest = 'en') #영어번역
        result_jap = trans.translate(trans_str, dest = 'ja') #일본번역
        result_chi = trans.translate(trans_str, dest = 'zh-cn') #중국번역

        self.en.append(result_eng.text) #영어번역 보이게
        self.ja.append(result_jap.text) #일본번역 보이게
        self.ch.append(result_chi.text) #중국번역 보이게
        
    def reset_operation(self): # 리셋버튼 만들어주기
        self.ko.clear()
        self.en.clear()
        self.ja.clear()
        self.ch.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())