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
        btn.clicked.connect(self.close_application)
        # btn.resize(100, 100)
        # btn.resize(btn.sizeHint())
        btn.resize(btn.minimumSizeHint())
        btn.move(100, 100)
        self.show()

    def close_application(self):
        print("Hey! I did it!")
        sys.exit()


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
