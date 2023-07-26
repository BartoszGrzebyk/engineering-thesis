import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class Dataset():
    def __init__(self, fileName, testSetSize):
        try:
            self.dataset = pd.read_csv(fileName)
        except FileNotFoundError:
            raise FileNotFoundError
        except:
            raise Exception()

        self.x = self.dataset.iloc[:, 0:-1].values
        # self.x = self.dataset.iloc[:, 1:].values
        self.y = self.dataset.iloc[:, -1].values
        # self.y = self.dataset.iloc[:, 0].values

        self.class_names = set(self.y)
        self.class_names = list(self.class_names)
        self.class_names.sort()
        self.class_names = [str(i) for i in self.class_names]

        le = LabelEncoder()
        self.y = le.fit_transform(self.y)

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=testSetSize)

        sc = StandardScaler()
        self.x_train = sc.fit_transform(self.x_train)
        self.x_test = sc.fit_transform(self.x_test)
