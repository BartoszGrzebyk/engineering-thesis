import sys
from PySide6 import QtWidgets
from mainWindow import MainWindow

app = QtWidgets.QApplication([])

window = MainWindow()
window.resize(650, 400)
window.show()

sys.exit(app.exec())
