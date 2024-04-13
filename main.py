#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com
Last edited: August 2017
"""
import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton
from PyQt5.uic import loadUi

class MyMainWindow(QDialog):
    def __init__(self):
        super().__init__()
        # 加载 .ui 文件
        loadUi('D:\\development\\python\\openpose\\ui\\untitled.ui', self)
        self.initUI()
        # 此处可以添加其他初始化代码

    def initUI(self):
        # 拍摄照片
        button = self.findChild(QPushButton, 'paishe')
        button.clicked.connect(self.onButtonClick)
        # self.setPixmap('C:\\Users\\26094\Pictures\\powershell_logo_icon_144968.png')

    def setPixmap(self, q_image):
        # 图片显示
        picture = self.findChild(QLabel, 'picture')
        pixmap = QPixmap.fromImage(q_image)  # 替换为你的图片路径
        scaled_pixmap = pixmap.scaled(picture.size(), aspectRatioMode=Qt.KeepAspectRatio)
        picture.setPixmap(scaled_pixmap)
        picture.adjustSize()

    def onButtonClick(self):
        self.video = cv2.VideoCapture(0)
        ret, self.image = self.video.read()
        if ret:
            image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            h, w, ch = image_rgb.shape
            bytes_per_line = ch * w
            q_image = QImage(image_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.setPixmap(q_image)

if __name__ == '__main__':
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()