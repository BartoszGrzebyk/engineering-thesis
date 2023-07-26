from PySide6 import QtWidgets, QtCore, QtGui
from classificationModel import ClassificationModel


class Result(QtWidgets.QWidget):
    def __init__(self, dataset, classModel, parameters):
        super().__init__()

        self.setWindowTitle("Wynik")
        self.layout = QtWidgets.QGridLayout(self)
        self.resize(650, 400)
        self.show()

        self.classificationModel = ClassificationModel(dataset, classModel, parameters)

        text = QtWidgets.QLabel("Tablica pomyłek:")
        text.setFixedWidth(100)

        table = QtWidgets.QTableWidget()
        confusion_matrix = self.classificationModel.confusionMatrix
        size = len(self.classificationModel.confusionMatrix)
        table.setRowCount(size)
        table.setColumnCount(size)
        table.setHorizontalHeaderLabels(dataset.class_names)
        table.setVerticalHeaderLabels(dataset.class_names)
        for i in range(size):
            for j in range(size):
                table.setItem(i, j, QtWidgets.QTableWidgetItem(str(confusion_matrix[i][j])))
                if i == j:
                    table.item(i, j).setBackground(QtGui.QColor(0, 255, 0))
                else:
                    table.item(i, j).setBackground(QtGui.QColor(255, 0, 0))

        table.resizeColumnsToContents()

        accuracy_score_text = QtWidgets.QLabel("Dokładność: ")
        accuracy_score_text.setFixedHeight(50)
        accuracy_score = QtWidgets.QLabel(str(round(self.classificationModel.accuracyScore * 100, 2)) + "%")
        bold_font = QtGui.QFont()
        bold_font.setBold(True)
        bold_font.setPixelSize(20)
        accuracy_score.setFont(bold_font)

        self.layout.addWidget(text, 1, 0, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(table, 1, 1)
        self.layout.addWidget(accuracy_score_text, 2, 0)
        self.layout.addWidget(accuracy_score, 2, 1)
