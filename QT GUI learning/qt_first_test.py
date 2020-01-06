import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.setGeometry(50, 50, 500, 300)  # setGeometry(x_pos,y_pos,x_pixels,y_pixels)
window.setWindowTitle("PyQt First Try")

for x in range(1, 4):
    print(xy)

window.show()
