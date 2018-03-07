from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
iris = datasets.load_iris()
xVal = iris.data[:, :2]
print("--------------X Value--------------------------- \n",xVal)
yVal = iris.target
print("\n ----------------Target Value--------------------- \n",yVal)
myClassifier =  LDA()
myClassifier.fit(xVal, yVal)
LDA(n_components=None, priors=None, shrinkage=None, solver='svd',
  store_covariance=False, tol=0.0001)
print("\n-----Prediction------------------------\n")
print(myClassifier.predict([[-0.6, -2]]))
