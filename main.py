#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Xu Haitao

from PyQt5 .QtCore import QTimer

from Login import *
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import b_curve
import bezier_curve


class LoginWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.PushButton_1.clicked.connect(self.b_curve)
        self.ui.PushButton_2.clicked.connect(self.bizare_curve)
        self.n = self.ui.lineEdit.text()
        self.GUI_MAIN()
        self.show()

    def GUI_MAIN(self):
        # 使用定时器进行实时刷新
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start(30)

    def refresh(self):
        self.n = self.ui.lineEdit.text()

    def b_curve(self):
        b_curve.main(int(self.n))

    def bizare_curve(self):
        bezier_curve.main()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() is False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindows()
    sys.exit(app.exec_())
