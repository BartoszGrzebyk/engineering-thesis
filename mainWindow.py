from PySide6 import QtWidgets, QtCore
from dataset import Dataset
from helpWindow import Help
from resultWindow import Result


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Klasyfikator")
        self.layout = QtWidgets.QGridLayout(self)
        self.chooseFileWindow()

    def chooseFileWindow(self):
        self.clearLayout()

        text = QtWidgets.QLabel("Podaj nazwę pliku ze zbiorem danych:")
        text.setFixedWidth(200)
        text.setFixedHeight(20)
        file_name = QtWidgets.QLineEdit()
        file_name.setFixedHeight(20)

        test_set_size = QtWidgets.QLineEdit()
        test_set_size.setText("25%")
        test_set_size.setReadOnly(True)
        pass_test_set_size = QtWidgets.QLabel("Podaj jaka część zestawu danych ma być przeznaczona do testowania:")
        pass_test_set_size.setFixedHeight(20)
        test_set_size_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        test_set_size_slider.setMinimum(5)
        test_set_size_slider.setMaximum(50)
        test_set_size_slider.setValue(25)
        test_set_size_slider.setTickInterval(1)
        test_set_size_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        test_set_size_slider.valueChanged.connect(
            lambda: self.showSliderValue(str(test_set_size_slider.value()) + "%", test_set_size))

        load_file_button = QtWidgets.QPushButton("Wczytaj")
        load_file_button.setFixedHeight(50)
        load_file_button.clicked.connect(lambda: self.loadFile(file_name.text(), test_set_size_slider.value()/100))

        self.layout.addWidget(text, 0, 0, 1, 2, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(file_name, 0, 2, 1, 2, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(pass_test_set_size, 1, 0, 1, 4, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(test_set_size_slider, 2, 0, 1, 2, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(test_set_size, 2, 2, 1, 2, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(load_file_button, 3, 1, 1, 2, alignment=QtCore.Qt.AlignBottom)

    def showMainMenu(self):
        self.clearLayout()

        text = QtWidgets.QLabel("Wybierz metodę klasyfikacji:")
        text.setFixedWidth(200)
        text.setFixedHeight(20)

        choose_linear_regression = QtWidgets.QPushButton("Regresja logistyczna")
        choose_linear_regression.setFixedHeight(50)
        choose_linear_regression.clicked.connect(self.LogisticRegression)

        choose_KNN = QtWidgets.QPushButton("K-najbliższych sąsiadów")
        choose_KNN.setFixedHeight(50)
        choose_KNN.clicked.connect(self.KNearestNeighbours)

        choose_naive_bayes = QtWidgets.QPushButton("Naiwny klasyfikator Bayesa")
        choose_naive_bayes.setFixedHeight(50)
        choose_naive_bayes.clicked.connect(self.NaiveBayes)

        choose_SVM = QtWidgets.QPushButton("Maszyna wektorów nośnych")
        choose_SVM.setFixedHeight(50)
        choose_SVM.clicked.connect(self.SVM)

        choose_random_forest = QtWidgets.QPushButton("Las losowy")
        choose_random_forest.setFixedHeight(50)
        choose_random_forest.clicked.connect(self.RandomForest)

        return_button = QtWidgets.QPushButton("Cofnij")
        return_button.setFixedHeight(50)
        return_button.clicked.connect(self.chooseFileWindow)

        placeholder = QtWidgets.QLabel()
        placeholder.setFixedHeight(0)

        self.layout.addWidget(placeholder, 1, 0, 1, 4)
        self.layout.addWidget(text, 0, 1, 1, 2, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(choose_linear_regression, 2, 1, 1, 2, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(choose_KNN, 3, 1, 1, 2, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(choose_naive_bayes, 4, 1, 1, 2, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(choose_SVM, 5, 1, 1, 2, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(choose_random_forest, 6, 1, 1, 2, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(return_button, 7, 1, 1, 2, alignment=QtCore.Qt.AlignTop)

    def LogisticRegression(self):
        self.clearLayout()

        text = QtWidgets.QLabel("Podaj parametry dla modelu 'Regresja logistyczna':")

        help_button = QtWidgets.QPushButton("Pomoc")
        help_button.clicked.connect(lambda: self.showHelpWindow("LogisticRegression"))
        help_button.setFixedWidth(100)

        tol = QtWidgets.QLineEdit()
        tol.setText("1e-3")
        tol.setReadOnly(True)

        pass_tol = QtWidgets.QLabel("Parametr 'tol':")
        tol_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        tol_slider.setMinimum(1)
        tol_slider.setMaximum(5)
        tol_slider.setValue(3)
        tol_slider.setTickInterval(1)
        tol_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        tol_slider.valueChanged.connect(
            lambda: self.showSliderValue("1e-" + str(tol_slider.value()), tol))

        c_parameter = QtWidgets.QLineEdit()
        c_parameter.setText("1e0")
        c_parameter.setReadOnly(True)

        pass_c_parameter = QtWidgets.QLabel("Parametr 'C':")
        c_parameter_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        c_parameter_slider.setMinimum(-2)
        c_parameter_slider.setMaximum(3)
        c_parameter_slider.setValue(0)
        c_parameter_slider.setTickInterval(1)
        c_parameter_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        c_parameter_slider.valueChanged.connect(
            lambda: self.showSliderValue("1e" + str(c_parameter_slider.value()), c_parameter))

        fit_intercept = QtWidgets.QLabel("Parametr 'fit_intercept':")
        radio_box_1_fit_intercept = QtWidgets.QRadioButton("true")
        radio_box_2_fit_intercept = QtWidgets.QRadioButton("false")
        radio_group_fit_intercept = QtWidgets.QButtonGroup()
        radio_group_fit_intercept.addButton(radio_box_1_fit_intercept)
        radio_group_fit_intercept.addButton(radio_box_2_fit_intercept)
        radio_box_1_fit_intercept.setChecked(True)

        pass_solver = QtWidgets.QLabel("Parametr 'solver':")
        list_of_solvers = QtWidgets.QComboBox()
        list_of_solvers.addItem("lbfgs")
        list_of_solvers.addItem("newton-cg")
        list_of_solvers.addItem("liblinear")
        list_of_solvers.addItem("sag")
        list_of_solvers.addItem("saga")

        return_button = QtWidgets.QPushButton("Cofnij")
        return_button.clicked.connect(self.showMainMenu)

        continue_button = QtWidgets.QPushButton("Kontynuuj")
        continue_button.clicked.connect(lambda: self.createClassificationModel("LogisticRegression", [float("1e-" + str(tol_slider.value())),
                                                                                                      float("1e" + str(c_parameter_slider.value())),
                                                                                                      radio_box_1_fit_intercept.isChecked(),
                                                                                                      list_of_solvers.currentText()]))

        self.layout.addWidget(text, 0, 0)
        self.layout.addWidget(help_button, 0, 1, alignment=QtCore.Qt.AlignRight)
        self.layout.addWidget(pass_tol, 1, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(tol_slider, 2, 0)
        self.layout.addWidget(tol, 2, 1)
        self.layout.addWidget(pass_c_parameter, 3, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(c_parameter_slider, 4, 0)
        self.layout.addWidget(c_parameter, 4, 1)
        self.layout.addWidget(fit_intercept, 6, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(radio_box_1_fit_intercept, 7, 0)
        self.layout.addWidget(radio_box_2_fit_intercept, 8, 0)
        self.layout.addWidget(pass_solver, 9, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(list_of_solvers, 10, 0, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(return_button, 11, 0)
        self.layout.addWidget(continue_button, 11, 1)

    def KNearestNeighbours(self):
        def showPParameter(metrics, widgets):
            if metrics.currentText() == 'minkowski':
                for widget in widgets:
                    widget.setEnabled(True)
            else:
                for widget in widgets:
                    widget.setEnabled(False)

        self.clearLayout()

        text = QtWidgets.QLabel("Podaj parametry dla modelu 'K-najbliższych sąsiadów':")

        help_button = QtWidgets.QPushButton("Pomoc")
        help_button.clicked.connect(lambda: self.showHelpWindow("KNearestNeighbours"))
        help_button.setFixedWidth(100)

        n_neighbours = QtWidgets.QLineEdit()
        n_neighbours.setText("5")
        n_neighbours.setReadOnly(True)

        pass_n_neighbours = QtWidgets.QLabel("Liczba sąsiadów (parametr 'n_neighbors'):")
        n_neighbours_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        n_neighbours_slider.setMinimum(3)
        n_neighbours_slider.setMaximum(15)
        n_neighbours_slider.setValue(5)
        n_neighbours_slider.setTickInterval(1)
        n_neighbours_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        n_neighbours_slider.valueChanged.connect(lambda: self.showSliderValue(str(n_neighbours_slider.value()), n_neighbours))

        pass_weights = QtWidgets.QLabel("Wagi punktów (parametr 'weights'):")
        radio_box_weight_1 = QtWidgets.QRadioButton("uniform")
        radio_box_weight_2 = QtWidgets.QRadioButton("distance")
        radio_group_weight = QtWidgets.QButtonGroup()
        radio_group_weight.addButton(radio_box_weight_1)
        radio_group_weight.addButton(radio_box_weight_2)
        radio_box_weight_1.setChecked(True)

        pass_algorithm = QtWidgets.QLabel("Algorytm (parametr 'algorithm'):")
        list_of_algorithms = QtWidgets.QComboBox()
        list_of_algorithms.addItem("auto")
        list_of_algorithms.addItem("ball_tree")
        list_of_algorithms.addItem("kd_tree")
        list_of_algorithms.addItem("brute")

        pass_metric = QtWidgets.QLabel("Metryka (parametr 'metric'):")
        list_of_metrics = QtWidgets.QComboBox()
        list_of_metrics.addItem("minkowski")
        list_of_metrics.addItem("manhattan")
        list_of_metrics.addItem("chebyshev")
        list_of_metrics.addItem("euclidean")

        p_parameter = QtWidgets.QLineEdit()
        p_parameter.setText("2")
        p_parameter.setReadOnly(True)

        pass_p_parameter = QtWidgets.QLabel("Parametr 'p':")
        p_parameter_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        p_parameter_slider.setMinimum(1)
        p_parameter_slider.setMaximum(10)
        p_parameter_slider.setValue(2)
        p_parameter_slider.setTickInterval(1)
        p_parameter_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        p_parameter_slider.valueChanged.connect(
            lambda: self.showSliderValue(str(p_parameter_slider.value()), p_parameter))

        showPParameter(list_of_metrics, [p_parameter, pass_p_parameter, p_parameter_slider])
        list_of_metrics.currentTextChanged.connect(lambda: showPParameter(list_of_metrics, [p_parameter, pass_p_parameter, p_parameter_slider]))

        return_button = QtWidgets.QPushButton("Cofnij")
        return_button.clicked.connect(self.showMainMenu)

        continue_button = QtWidgets.QPushButton("Kontynuuj")
        continue_button.clicked.connect(lambda: self.createClassificationModel("KNearestNeighbours",
                                                                                   [n_neighbours_slider.value(),
                                                                                    "uniform" if radio_box_weight_1.isChecked() else "distance",
                                                                                    list_of_algorithms.currentText(),
                                                                                    list_of_metrics.currentText(),
                                                                                    p_parameter_slider.value()]))

        self.layout.addWidget(text, 0, 0)
        self.layout.addWidget(help_button, 0, 1, alignment=QtCore.Qt.AlignRight)
        self.layout.addWidget(pass_n_neighbours, 1, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(n_neighbours_slider, 2, 0)
        self.layout.addWidget(n_neighbours, 2, 1)
        self.layout.addWidget(pass_weights, 3, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(radio_box_weight_1, 4, 0)
        self.layout.addWidget(radio_box_weight_2, 5, 0)
        self.layout.addWidget(pass_algorithm, 6, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(list_of_algorithms, 7, 0)
        self.layout.addWidget(pass_metric, 10, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(list_of_metrics, 11, 0)
        self.layout.addWidget(pass_p_parameter, 12, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(p_parameter_slider, 13, 0, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(p_parameter, 13, 1, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(return_button, 14, 0)
        self.layout.addWidget(continue_button, 14, 1, 1, 2)

    def NaiveBayes(self):
        self.clearLayout()

        text = QtWidgets.QLabel("Podaj parametry dla modelu 'Naiwny Klasyfikator Bayesa':")
        text.setFixedWidth(320)
        text.setFixedHeight(20)

        help_button = QtWidgets.QPushButton("Pomoc")
        help_button.clicked.connect(lambda: self.showHelpWindow("NaiveBayes"))
        help_button.setFixedWidth(100)

        var_smoothing = QtWidgets.QLineEdit()
        var_smoothing.setText("1e-9")
        var_smoothing.setReadOnly(True)

        pass_var_smoothing = QtWidgets.QLabel("Parametr 'var_smoothing':")
        pass_var_smoothing.setFixedWidth(350)
        pass_var_smoothing.setFixedHeight(20)
        var_smoothing_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        var_smoothing_slider.setMinimum(1)
        var_smoothing_slider.setMaximum(15)
        var_smoothing_slider.setValue(9)
        var_smoothing_slider.setTickInterval(1)
        var_smoothing_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        var_smoothing_slider.valueChanged.connect(lambda: self.showSliderValue("1e-" + str(var_smoothing_slider.value()), var_smoothing))

        return_button = QtWidgets.QPushButton("Cofnij")
        return_button.clicked.connect(self.showMainMenu)

        continue_button = QtWidgets.QPushButton("Kontynuuj")
        continue_button.clicked.connect(
            lambda: self.createClassificationModel("NaiveBayes", [float("1e-" + str(var_smoothing_slider.value()))]))

        self.layout.addWidget(text, 0, 0, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(help_button, 0, 1, alignment=QtCore.Qt.AlignRight)
        self.layout.addWidget(pass_var_smoothing, 1, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(var_smoothing_slider, 2, 0, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(var_smoothing, 2, 1, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(return_button, 3, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(continue_button, 3, 1, alignment=QtCore.Qt.AlignBottom)

    def SVM(self):
        def showDegreeAndGammaParameters(kernels, degree_widgets, gamma_widgets):
            if (kernels.currentText() == "rbf" or kernels.currentText() == "sigmoid"):
                for widget in degree_widgets:
                    widget.setEnabled(False)
                for widget in gamma_widgets:
                    widget.setEnabled(True)
            elif (kernels.currentText() == "poly"):
                for widget in degree_widgets:
                    widget.setEnabled(True)
                for widget in gamma_widgets:
                    widget.setEnabled(True)
            else:
                for widget in degree_widgets:
                    widget.setEnabled(False)
                for widget in gamma_widgets:
                    widget.setEnabled(False)

        self.clearLayout()

        text = QtWidgets.QLabel("Podaj parametry dla modelu 'Maszyna wektorów nośnych':")

        help_button = QtWidgets.QPushButton("Pomoc")
        help_button.clicked.connect(lambda: self.showHelpWindow("SVM"))
        help_button.setFixedWidth(100)

        c_parameter = QtWidgets.QLineEdit()
        c_parameter.setText("1e0")
        c_parameter.setReadOnly(True)

        pass_c_parameter = QtWidgets.QLabel("Parametr 'C':")
        c_parameter_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        c_parameter_slider.setMinimum(-2)
        c_parameter_slider.setMaximum(3)
        c_parameter_slider.setValue(0)
        c_parameter_slider.setTickInterval(1)
        c_parameter_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        c_parameter_slider.valueChanged.connect(
            lambda: self.showSliderValue("1e" + str(c_parameter_slider.value()), c_parameter))

        pass_kernel = QtWidgets.QLabel("Jądro (parametr 'kernel'):")
        list_of_kernels = QtWidgets.QComboBox()
        list_of_kernels.addItem("rbf")
        list_of_kernels.addItem("linear")
        list_of_kernels.addItem("poly")
        list_of_kernels.addItem("sigmoid")

        degree = QtWidgets.QLineEdit()
        degree.setText("3")
        degree.setReadOnly(True)

        pass_degree = QtWidgets.QLabel("Parametr 'degree':")
        degree_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        degree_slider.setMinimum(1)
        degree_slider.setMaximum(6)
        degree_slider.setValue(3)
        degree_slider.setTickInterval(1)
        degree_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        degree_slider.valueChanged.connect(
            lambda: self.showSliderValue(str(degree_slider.value()), degree))

        pass_gamma = QtWidgets.QLabel("Parametr 'gamma':")
        radio_box_gamma_1 = QtWidgets.QRadioButton("scale")
        radio_box_gamma_2 = QtWidgets.QRadioButton("auto")
        radio_group_gamma = QtWidgets.QButtonGroup()
        radio_group_gamma.addButton(radio_box_gamma_1)
        radio_group_gamma.addButton(radio_box_gamma_2)
        radio_box_gamma_1.setChecked(True)

        showDegreeAndGammaParameters(list_of_kernels,
                                     [degree, pass_degree, degree_slider],
                                     [pass_gamma, radio_box_gamma_1, radio_box_gamma_2])

        list_of_kernels.currentTextChanged.connect(lambda: showDegreeAndGammaParameters(list_of_kernels,
                                                                                        [degree, pass_degree, degree_slider],
                                                                                        [pass_gamma, radio_box_gamma_1, radio_box_gamma_2]))

        tol = QtWidgets.QLineEdit()
        tol.setText("1e-3")
        tol.setReadOnly(True)

        pass_tol = QtWidgets.QLabel("Parametr 'tol':")
        tol_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        tol_slider.setMinimum(1)
        tol_slider.setMaximum(5)
        tol_slider.setValue(3)
        tol_slider.setTickInterval(1)
        tol_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        tol_slider.valueChanged.connect(
            lambda: self.showSliderValue("1e-" + str(tol_slider.value()), tol))

        return_button = QtWidgets.QPushButton("Cofnij")
        return_button.clicked.connect(self.showMainMenu)

        continue_button = QtWidgets.QPushButton("Kontynuuj")
        continue_button.clicked.connect(
            lambda: self.createClassificationModel("SVM", [float("1e" + str(c_parameter_slider.value())),
                                                           list_of_kernels.currentText(),
                                                           degree_slider.value(),
                                                           "scale" if radio_box_gamma_1.isChecked() else "auto",
                                                           float("1e-" + str(tol_slider.value()))]))

        self.layout.addWidget(text, 0, 0)
        self.layout.addWidget(help_button, 0, 1, alignment=QtCore.Qt.AlignRight)
        self.layout.addWidget(pass_c_parameter, 1, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(c_parameter_slider, 2, 0)
        self.layout.addWidget(c_parameter, 2, 1)
        self.layout.addWidget(pass_kernel, 3, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(list_of_kernels, 4, 0)
        self.layout.addWidget(pass_degree, 5, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(degree_slider, 6, 0)
        self.layout.addWidget(degree, 6, 1)
        self.layout.addWidget(pass_gamma, 7, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(radio_box_gamma_1, 8, 0)
        self.layout.addWidget(radio_box_gamma_2, 9, 0)
        self.layout.addWidget(pass_tol, 10, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(tol_slider, 11, 0, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(tol, 11, 1, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(return_button, 14, 0)
        self.layout.addWidget(continue_button, 14, 1)

    def RandomForest(self):
        self.clearLayout()

        text = QtWidgets.QLabel("Podaj parametry dla modelu 'Las losowy':")

        help_button = QtWidgets.QPushButton("Pomoc")
        help_button.clicked.connect(lambda: self.showHelpWindow("RandomForest"))
        help_button.setFixedWidth(100)

        n_estimators = QtWidgets.QLineEdit()
        n_estimators.setText("100")
        n_estimators.setReadOnly(True)

        pass_n_estimators = QtWidgets.QLabel("Parametr 'n_estimators':")
        n_estimators_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        n_estimators_slider.setMinimum(10)
        n_estimators_slider.setMaximum(500)
        n_estimators_slider.setValue(100)
        n_estimators_slider.setTickInterval(10)
        n_estimators_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        n_estimators_slider.valueChanged.connect(
            lambda: self.showSliderValue(str(n_estimators_slider.value()), n_estimators))

        pass_criterion = QtWidgets.QLabel("Parametr 'criterion':")
        radio_box_criterion_1 = QtWidgets.QRadioButton("gini")
        radio_box_criterion_2 = QtWidgets.QRadioButton("entropy")
        radio_group_criterion = QtWidgets.QButtonGroup()
        radio_group_criterion.addButton(radio_box_criterion_1)
        radio_group_criterion.addButton(radio_box_criterion_2)
        radio_box_criterion_1.setChecked(True)

        max_depth = QtWidgets.QLineEdit()
        max_depth.setText("None")
        max_depth.setReadOnly(True)

        pass_max_depth = QtWidgets.QLabel("Parametr 'max_depth':")
        max_depth_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        max_depth_slider.setMinimum(2)
        max_depth_slider.setMaximum(101)
        max_depth_slider.setValue(101)
        max_depth_slider.setTickInterval(5)
        max_depth_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        max_depth_slider.valueChanged.connect(
            lambda: self.showSliderValue("None" if max_depth_slider.value() == 101 else str(max_depth_slider.value()), max_depth))

        min_samples_split = QtWidgets.QLineEdit()
        min_samples_split.setText("2")
        min_samples_split.setReadOnly(True)

        pass_min_samples_split = QtWidgets.QLabel("Parametr 'min_samples_split':")
        min_samples_split_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        min_samples_split_slider.setMinimum(2)
        min_samples_split_slider.setMaximum(10)
        min_samples_split_slider.setValue(2)
        min_samples_split_slider.setTickInterval(1)
        min_samples_split_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        min_samples_split_slider.valueChanged.connect(
            lambda: self.showSliderValue(str(min_samples_split_slider.value()), min_samples_split))

        min_samples_leaf = QtWidgets.QLineEdit()
        min_samples_leaf.setText("1")
        min_samples_leaf.setReadOnly(True)

        pass_min_samples_leaf = QtWidgets.QLabel("Parametr 'min_samples_leaf':")
        min_samples_leaf_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        min_samples_leaf_slider.setMinimum(1)
        min_samples_leaf_slider.setMaximum(10)
        min_samples_leaf_slider.setValue(1)
        min_samples_leaf_slider.setTickInterval(1)
        min_samples_leaf_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        min_samples_leaf_slider.valueChanged.connect(
            lambda: self.showSliderValue(str(min_samples_leaf_slider.value()), min_samples_leaf))

        return_button = QtWidgets.QPushButton("Cofnij")
        return_button.clicked.connect(self.showMainMenu)

        continue_button = QtWidgets.QPushButton("Kontynuuj")
        continue_button.clicked.connect(
            lambda: self.createClassificationModel("RandomForest", [n_estimators_slider.value(),
                                                                    "gini" if radio_box_criterion_1.isChecked() else "entropy",
                                                                    None if max_depth_slider.value() == 101 else max_depth_slider.value(),
                                                                    min_samples_split_slider.value(),
                                                                    min_samples_leaf_slider.value()]))

        self.layout.addWidget(text, 0, 0)
        self.layout.addWidget(help_button, 0, 1, alignment=QtCore.Qt.AlignRight)
        self.layout.addWidget(pass_n_estimators, 1, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(n_estimators_slider, 2, 0)
        self.layout.addWidget(n_estimators, 2, 1)
        self.layout.addWidget(pass_criterion, 3, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(radio_box_criterion_1, 4, 0)
        self.layout.addWidget(radio_box_criterion_2, 5, 0)
        self.layout.addWidget(pass_max_depth, 6, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(max_depth_slider, 7, 0)
        self.layout.addWidget(max_depth, 7, 1)
        self.layout.addWidget(pass_min_samples_split, 8, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(min_samples_split_slider, 9, 0)
        self.layout.addWidget(min_samples_split, 9, 1)
        self.layout.addWidget(pass_min_samples_leaf, 10, 0, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(min_samples_leaf_slider, 11, 0, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(min_samples_leaf, 11, 1, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(return_button, 12, 0)
        self.layout.addWidget(continue_button, 12, 1)

    def loadFile(self, fileName, test_set_size):
        try:
            self.dataset = Dataset(fileName, test_set_size)
            self.showMainMenu()
        except FileNotFoundError:
            self.showError("Plik o podanej nazwie nie istnieje")
        except:
            self.showError("Nie udało się wczytać pliku.")

    def showSliderValue(self, string, lineEdit):
        lineEdit.setText(string)

    def createClassificationModel(self, classModel, parameters):
        self.result = Result(self.dataset, classModel, parameters)

    def showHelpWindow(self, method):
        self.help = Help(method)
        self.help.resize(400, 200)
        self.help.show()

    def showError(self, error_message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(error_message)
        msg.setWindowTitle("Błąd")
        msg.exec_()

    def clearLayout(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)
