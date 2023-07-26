from PySide6 import QtWidgets, QtCore


class Help(QtWidgets.QWidget):
    def __init__(self, method, parent=None):
        super(Help, self).__init__(parent)

        self.setWindowTitle("Pomoc " + method)
        self.layout = QtWidgets.QVBoxLayout(self)

        if method == "LogisticRegression":
            self.LogisticRegression()
        elif method == "KNearestNeighbours":
            self.KNearestNeighbours()
        elif method == "NaiveBayes":
            self.NaiveBayes()
        elif method == "SVM":
            self.SVM()
        elif method == "RandomForest":
            self.RandomForest()

    def LogisticRegression(self):
        self.clearLayout()

        text = QtWidgets.QLabel("Objaśnienie parametrów modelu 'Regresja logistyczna':")
        tol = QtWidgets.QLabel("<b>Parametr 'tol'</b> - tolerancja, kryterium zatrzymania działania algorytmu.")
        c_parameter = QtWidgets.QLabel("<b>Parametr 'C'</b> - odwrotność parametru regularyzującego (C = 1/λ); regularyzacja stosowana jest w celu rozwiązania problemu"
                                       "<br>nadmiernego dopasowania danych, zmniejszając wpływ niektórych zmiennych niezależnych na wynik.")
        intercept = QtWidgets.QLabel("<b>Parametr 'intercept'</b> - parametr typu boole’owskiego określający, czy w modelu powinna być zastosowana pewna stała, będąca"
                                     "<br>w równaniu wyrazem wolnym, odpowiednio przesuwająca funkcję.")
        solver = QtWidgets.QLabel("<b>Parametr 'solver'</b> - metoda, jaka ma zostać użyta do znalezienia odpowiednich współczynników funkcji i tym samym"
                                  "<br>zminimalizowania błędu.")

        close_button = QtWidgets.QPushButton("Zamknij")
        close_button.setFixedWidth(100)
        close_button.clicked.connect(self.close)

        self.layout.addWidget(text)
        self.layout.addWidget(tol)
        self.layout.addWidget(c_parameter)
        self.layout.addWidget(intercept)
        self.layout.addWidget(solver)
        self.layout.addWidget(close_button, alignment=QtCore.Qt.AlignCenter)

    def KNearestNeighbours(self):
        self.clearLayout()

        text = QtWidgets.QLabel("Objaśnienie parametrów modelu 'K-najbliższych sąsiadów':")
        n_neighbors = QtWidgets.QLabel("<b>Parametr 'n_neighbors'</b> - liczba sąsiadów branych pod uwagę podczas obliczeń.")
        weights = QtWidgets.QLabel("<b>Parametr 'weights'</b> - określa, czy podczas obliczeń ma zostać zastosowana pewna waga dla sąsiadów. W przypadku 'uniform'"
                                   "<br>wszystkie punkty będą miały tę samą wagę, natomiast dla 'distance' punkty leżące bliżej będą miały większy wpływ na wynik.")
        algorithm = QtWidgets.QLabel("<b>Parametr 'algorithm'</b> - określa, jaki algorytm ma być użyty podczas poszukiwania najbliższych sąsiadów. Wybór 'auto'"
                                     "<br>oznacza automatyczny wybór algorytmu przez model, w zależności od danych wejściowych.")
        metric = QtWidgets.QLabel("<b>Parametr 'metric'</b> - określa metrykę, jaka ma być zastosowana podczas wyboru najbliższych sąsiadów:"
                                  "<br>- minkowski - sum(w * |x - y|^p)^(1/p)"
                                  "<br>- manhattan - sum(|x - y|)"
                                  "<br>- chebyshev - max(|x - y|)"
                                  "<br>- euclidean - sqrt(sum((x - y)^2))")
        p = QtWidgets.QLabel("<b>Parametr 'p'</b> - ustawiany jest w przypadku wyboru metryki 'minkowski.'")

        close_button = QtWidgets.QPushButton("Zamknij")
        close_button.setFixedWidth(100)
        close_button.clicked.connect(self.close)

        self.layout.addWidget(text)
        self.layout.addWidget(n_neighbors)
        self.layout.addWidget(weights)
        self.layout.addWidget(algorithm)
        self.layout.addWidget(metric)
        self.layout.addWidget(p)
        self.layout.addWidget(close_button, alignment=QtCore.Qt.AlignCenter)


    def NaiveBayes(self):
        self.clearLayout()

        text = QtWidgets.QLabel("Objaśnienie parametrów modelu 'Naiwny klasyfikator Bayesa':")
        var_smoothing = QtWidgets.QLabel("<b>Parametr 'var_smoothing'</b> - gaussowski naiwny klasyfikator Bayesa jest oparty o rozkład normalny."
                                         "<br>Ten parametr odpawiada za wypłaszczenie krzywej Gaussa powodując objęcie większęj ilości punktów,"
                                         "<br>które bardziej odbiegają od średniej.")

        close_button = QtWidgets.QPushButton("Zamknij")
        close_button.setFixedWidth(100)
        close_button.clicked.connect(self.close)

        self.layout.addWidget(text)
        self.layout.addWidget(var_smoothing)
        self.layout.addWidget(close_button, alignment=QtCore.Qt.AlignCenter)

    def SVM(self):
        self.clearLayout()

        text = QtWidgets.QLabel("Objaśnienie parametrów modelu 'Maszyna wektorów nośnych':")
        C = QtWidgets.QLabel("<b>Parametr 'C'</b> - parametr regularyzacyjny. W metodzie SVM poszukiwana jest hiperpłaszczyzna, która poprawnie rozdziela"
                             "<br>elementy klas oraz która ma jak najwięszky margines. Nie zawsze jest możliwe znalezienie hiperpłaszczyzny spełniającej"
                             "<br>oba te warunki. Parametr C określa jak bardzo model ma skupić się na poprawnym rozdzieleniu danych kosztem wielkości marginesu.")
        kernel = QtWidgets.QLabel("<b>Parametr 'kernel'</b> - odpowiada za wybór zastosowanego jądra.")
        degree = QtWidgets.QLabel("<b>Parametr 'degree'</b> - możliwy do ustawienia w przypadku jądra 'poly'. Określa stopień wielomianu użytego do znalezienia"
                                  "<br>hiperpłaszczyzny dzielącej dane.")
        gamma = QtWidgets.QLabel("<b>Parametr 'gamma'</b> - możliwy do ustawienia w przypadku jąder nieliniowych. Aplikacja oferuje wybór pomiędzy dwoma"
                                 "<br>wartościami tego parametru:"
                                 "<br>- scale - 1 / (n_features * X.var())"
                                 "<br>- auto - 1 / n_features")
        tol = QtWidgets.QLabel("<b>Parametr 'tol'</b> - tolerancja, kryterium zatrzymania działania algorytmu.")

        close_button = QtWidgets.QPushButton("Zamknij")
        close_button.setFixedWidth(100)
        close_button.clicked.connect(self.close)

        self.layout.addWidget(text)
        self.layout.addWidget(C)
        self.layout.addWidget(kernel)
        self.layout.addWidget(degree)
        self.layout.addWidget(gamma)
        self.layout.addWidget(tol)
        self.layout.addWidget(close_button, alignment=QtCore.Qt.AlignCenter)

    def RandomForest(self):
        self.clearLayout()

        text = QtWidgets.QLabel("Objaśnienie parametrów modelu 'Las losowy':")
        n_estimators = QtWidgets.QLabel("<b>Parametr 'n_estimators'</b> - liczba drzew w lesie.")
        criterion = QtWidgets.QLabel("<b>Parametr 'criterion'</b> - funkcja jaka ma zostać użyta do obliczenia jakości podziału zestawu danych.")
        max_depth = QtWidgets.QLabel("<b>Parametr 'max_depth'</b> - maksymalna głębokość drzewa pojedynczego drzewa decyzyjnego.")
        min_samples_split = QtWidgets.QLabel("<b>Parametr 'min_samples_split'</b> - minimalna liczba próbek koniecznych do dokonania kolejnego podziału.")
        min_samples_leaf = QtWidgets.QLabel("<b>Parametr 'min_samples_leaf'</b> - minimalna liczba próbek jakie muszą znajdować się w liściu.")

        close_button = QtWidgets.QPushButton("Zamknij")
        close_button.setFixedWidth(100)
        close_button.clicked.connect(self.close)

        self.layout.addWidget(text)
        self.layout.addWidget(n_estimators)
        self.layout.addWidget(criterion)
        self.layout.addWidget(max_depth)
        self.layout.addWidget(min_samples_split)
        self.layout.addWidget(min_samples_leaf)
        self.layout.addWidget(close_button, alignment=QtCore.Qt.AlignCenter)

    def clearLayout(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)
