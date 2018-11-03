import numpy
# import pandas
import scipy.io as sio
'''from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipelinec'''

cat_dc = sio.loadmat('dataset_DC.mat')
cat_pto = sio.loadmat('dataset_PTO.mat')
print cat_dc
