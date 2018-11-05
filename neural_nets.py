import numpy as np
from sklearn.model_selection import train_test_split
X = np.arange(18).reshape((6,3))
#print X
y =range (5)
Atom = X[0:3,:]
#print Atom


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
print X_train
