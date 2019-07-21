from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
import seaborn as sns
iris=load_iris()
print(iris)
print(iris.feature_names)
print(iris.target_names)

#print(iris.data[0])
#print(iris.target[0])
removed=[0,50,100]
newtarget=np.delete(iris.target,removed,axis=0)
clf=tree.DecisionTreeClassifier()
clf=clf.fit(newdata,newtarget)
#prediction=clf.predict(iris.data[removed])
predictin=clf.predict([[3,4,5.5]])
#print(iris.target[removed])
print(prediction)