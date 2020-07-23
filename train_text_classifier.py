import pandas
import cv2
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from joblib import dump, load

if not os.path.exists('dataframe.csv'):
    metadata = pandas.read_csv('imgs/labels.txt')
    im0 = cv2.imread(f'imgs/168.jpg', cv2.IMREAD_UNCHANGED)

    images = []
    for x in list(metadata.iterrows()):
        images.append(cv2.imread(f'imgs/{x[0]}.jpg', cv2.IMREAD_UNCHANGED))

    print(f'{len(images)} images being added to dataset')
    columns = [i for i in range(images[0].shape[0] * images[0].shape[1])]
    df = pandas.DataFrame(columns=columns)
    rows = 0
    i = 0
    for image in images:
        if image.shape != images[0].shape:
            app = np.zeros(image.shape[1])
            image = np.append(image, [app], axis=0)
        i += 1
        df.loc[rows] = np.concatenate(image).ravel()
        rows += 1

    df = df.assign(label=metadata['label'])
    df.to_csv('dataframe.csv')
else:
    df = pandas.read_csv('dataframe.csv')

clf = RandomForestClassifier()
y = df['label']
df = df.drop(columns='label')
df = df.drop(['Unnamed: 0'], axis=1)
X = df
print(X.head())
print(y.head())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)
clf.fit(X_train, y_train)
preds = clf.predict(X_test)
print([f'{pred}={true}' for (pred, true) in zip(preds, y_test)])
print(confusion_matrix(y_test, preds))

dump(clf, 'model.joblib')
