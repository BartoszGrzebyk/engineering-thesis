from sklearn.metrics import confusion_matrix, accuracy_score


class ClassificationModel():
    def __init__(self, dataset, classModel, parameters):
        self.dataset = dataset
        self.parameters = parameters

        if(classModel == "LogisticRegression"):
            self.LogisticRegression()
        elif(classModel == "KNearestNeighbours"):
            self.KNearestNeighbours()
        elif(classModel == "NaiveBayes"):
            self.NaiveBayes()
        elif(classModel == "SVM"):
            self.SVM()
        elif(classModel == "RandomForest"):
            self.RandomForest()

    def LogisticRegression(self):
        from sklearn.linear_model import LogisticRegression
        classifier = LogisticRegression(tol=self.parameters[0],
                                        C=self.parameters[1],
                                        fit_intercept=self.parameters[2],
                                        solver=self.parameters[3])
        classifier.fit(self.dataset.x_train, self.dataset.y_train)

        self.predict(classifier)

    def KNearestNeighbours(self):
        from sklearn.neighbors import KNeighborsClassifier
        classifier = KNeighborsClassifier(n_neighbors=self.parameters[0],
                                          weights=self.parameters[1],
                                          algorithm=self.parameters[2],
                                          metric=self.parameters[3],
                                          p=self.parameters[4])
        classifier.fit(self.dataset.x_train, self.dataset.y_train)

        self.predict(classifier)

    def NaiveBayes(self):
        from sklearn.naive_bayes import GaussianNB
        classifier = GaussianNB(var_smoothing=self.parameters[0])
        classifier.fit(self.dataset.x_train, self.dataset.y_train)

        self.predict(classifier)

    def SVM(self):
        from sklearn.svm import SVC
        classifier = SVC(C=self.parameters[0],
                         kernel=self.parameters[1],
                         degree=self.parameters[2],
                         gamma=self.parameters[3],
                         tol=self.parameters[4])
        classifier.fit(self.dataset.x_train, self.dataset.y_train)

        self.predict(classifier)

    def RandomForest(self):
        from sklearn.ensemble import RandomForestClassifier
        classifier = RandomForestClassifier(n_estimators=self.parameters[0],
                                            criterion=self.parameters[1],
                                            max_depth=self.parameters[2],
                                            min_samples_split=self.parameters[3],
                                            min_samples_leaf=self.parameters[4],
                                            random_state=0)
        classifier.fit(self.dataset.x_train, self.dataset.y_train)

        self.predict(classifier)

    def predict(self, classifier):
        self.dataset.y_predicted = classifier.predict(self.dataset.x_test)

        self.confusionMatrix = confusion_matrix(self.dataset.y_test, self.dataset.y_predicted)
        self.accuracyScore = accuracy_score(self.dataset.y_test, self.dataset.y_predicted)
