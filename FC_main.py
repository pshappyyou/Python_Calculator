import sys, ui

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#from PyQt5 import uic

#MainUI = '../_uiFiles/calc.ui'

class MainDiaglog(QDialog, ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self, None)
        #uic.loadUi(MainUI, self)
        self.setupUi(self)

        self.pb_num_1.clicked.connect(lambda state, button = self.pb_num_1: self.NumClicked(state, button))
        self.pb_num_2.clicked.connect(lambda state, button = self.pb_num_2: self.NumClicked(state, button))
        self.pb_num_3.clicked.connect(lambda state, button = self.pb_num_3: self.NumClicked(state, button))
        self.pb_num_4.clicked.connect(lambda state, button = self.pb_num_4: self.NumClicked(state, button))
        self.pb_num_5.clicked.connect(lambda state, button = self.pb_num_5: self.NumClicked(state, button))
        self.pb_num_6.clicked.connect(lambda state, button = self.pb_num_6: self.NumClicked(state, button))
        self.pb_num_7.clicked.connect(lambda state, button = self.pb_num_7: self.NumClicked(state, button))
        self.pb_num_8.clicked.connect(lambda state, button = self.pb_num_8: self.NumClicked(state, button))
        self.pb_num_9.clicked.connect(lambda state, button = self.pb_num_9: self.NumClicked(state, button))
        self.pb_num_0.clicked.connect(lambda state, button = self.pb_num_0: self.NumClicked(state, button))

        self.pb_sign_1.clicked.connect(lambda state, button = self.pb_sign_1: self.NumClicked(state, button))
        self.pb_sign_2.clicked.connect(lambda state, button = self.pb_sign_2: self.NumClicked(state, button))
        self.pb_sign_3.clicked.connect(lambda state, button = self.pb_sign_3: self.NumClicked(state, button))
        self.pb_sign_4.clicked.connect(lambda state, button = self.pb_sign_4: self.NumClicked(state, button))

        self.pb_paren_1.clicked.connect(lambda state, button = self.pb_paren_1: self.NumClicked(state, button))
        self.pb_paren_2.clicked.connect(lambda state, button = self.pb_paren_2: self.NumClicked(state, button))
        self.pb_dot.clicked.connect(lambda state, button = self.pb_dot: self.NumClicked(state, button))
        self.pb_percent.clicked.connect(lambda state, button = self.pb_percent: self.NumClicked(state, button))

        self.pb_result.clicked.connect(self.MakeResult)
        self.pb_reset.clicked.connect(self.Reset)
        self.pb_del.clicked.connect(self.Del)


    def NumClicked(self, state, button):
        if button == self.pb_percent:
            new_txt = '*0.01'
        else:
            new_txt = button.text()

        orig_txt = self.le_q.text()

        self.le_q.setText(orig_txt + new_txt)

#    def NumClicked2(self):
#      orig_txt = self.le_q.text()
#        new_txt = self.pb_num_2.text()
#        self.le_q.setText(orig_txt + new_txt)

    def MakeResult(self):
        try:
            result = eval(self.le_q.text())
            #print(type(result))
            self.le_a.setText(str(result))
        except Exception as e:
            print(e)
            #pass

    def Reset(self):
        self.le_q.clear()
        self.le_a.setText('0')

    def Del(self):
        origtxt = self.le_q.text()
        self.le_q.setText(origtxt[:-1])

app=QApplication(sys.argv)
main_dialog = MainDiaglog()
main_dialog.show()
app.exec_()