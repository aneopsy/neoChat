from src.userpref import UserPref
from PyQt4 import QtCore, QtGui
import sys


app = QtGui.QApplication(sys.argv)
palette = QtGui.QPalette()
palette.setColor(QtGui.QPalette.Background, QtGui.QColor(33, 37, 43))
app.setPalette(palette)
sshFile = "resources/darkorange.stylesheet"
with open(sshFile, "r") as fh:
    app.setStyleSheet(fh.read())
usernameWindow = UserPref()
usernameWindow.show()

sys.exit(app.exec_())
