import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics

irisData = datasets.load_iris()
x = irisData.data[:,:2]
y = irisData.target

c=0.2
minX, maxX = x[:, 0].min() - 1, x[:, 0].max() + 1
minY, maxY = x[:, 1].min() - 1, x[:, 1].max() + 1
x1, y1 = np.meshgrid(np.arange(minX, maxX, c),
                     np.arange(minY, maxY, c))

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.15)
model = svm.SVC()



predictions_linear = model.set_params(kernel='linear').fit(x_train, y_train).predict(x_test)

predictions_rbf = model.set_params(kernel='rbf').fit(x_train, y_train).predict(x_test)

accuracy_linear = metrics.accuracy_score(y_test,predictions_linear)
accuracy_rbf = metrics.accuracy_score(y_test,predictions_rbf)

print("Accuracy with kernel=linear:",accuracy_linear)
print("Accuracy with kernel=rbf:",accuracy_rbf)