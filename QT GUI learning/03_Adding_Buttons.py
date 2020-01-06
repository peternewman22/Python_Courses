import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):  # every time we make a window object, init runs and sets itself up etc
        super(Window, self).__init__()  # super returns the parent object
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQt Tuts")
        self.setWindowIcon(QtGui.QIcon("favicon.png"))
        self.home()  # Note: home doesn't exist until below

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.resize(100, 100)
        btn.move(100, 100)
        self.show()


app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())
