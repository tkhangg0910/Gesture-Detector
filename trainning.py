import pickle
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np


data_dict2 = pickle.load(open('./twohand.pickle', 'rb'))
data_two = np.asarray(data_dict2['data'])
labels2 = np.asarray(data_dict2['labels'])


x_train2, x_test2, y_train2, y_test2, = train_test_split(data_two, labels2, test_size=0.3, shuffle=True, stratify=labels2)

model2 = RandomForestClassifier()

model2.fit(x_train2, y_train2)

y_predict2 = model2.predict(x_test2)

score2= accuracy_score(y_predict2, y_test2)

print('{}% of samples were classified correctly for model2 !'.format(score2 * 100))

f = open('model2.p', 'wb')
pickle.dump({'model2': model2}, f)
f.close()
