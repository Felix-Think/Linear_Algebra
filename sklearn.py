from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
type(load_breast_cancer())

data = load_breast_cancer()
pd.DataFrame(data['data'])
pd.DataFrame(data['target'])

X_train, X_test, Y_train, Y_test = train_test_split(data.data, data.target, random_state = 42)

model = DecisionTreeClassifier(criterion = 'entropy')
model.fit(X_train, Y_train)



