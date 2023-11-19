import sys
import io

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from random import randrange


class Interface:
    def __init__(self):
        self.template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>740</width>
    <height>408</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="btn">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>20</y>
      <width>201</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Нарисовать окружности</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>740</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
        """

    def get_design(self):
        return self.template


class Example(QMainWindow):
    def __init__(self, interface=Interface()):
        super().__init__()
        f = io.StringIO(interface.get_design())
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        for _ in range(randrange(1, 31)):
            r = randrange(0, 256)
            g = randrange(0, 256)
            b = randrange(0, 256)
            qp.setBrush(QColor(r, g, b))
            d = randrange(1, 351)
            x = randrange(0, 401)
            y = randrange(60, 351)
            qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
