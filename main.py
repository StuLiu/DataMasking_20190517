'''
--------------------------------------------------------
@File    :   main.py.py    
@Contact :   1183862787@qq.com
@License :   (C)Copyright 2017-2018, CS, WHU

@Modify Time : 2019/5/18 1:01     
@Author      : Liu Wang    
@Version     : 1.0   
@Desciption  : 调用主窗口类启动程序。
--------------------------------------------------------  
''' 

import sys
import main_window
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = main_window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())