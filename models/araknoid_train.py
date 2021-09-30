import sys
import pandas as pd
import numpy as np
''' plot '''
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

#import seaborn as sns
''' data preprocessing '''
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
''' model '''
from sklearn.preprocessing import FunctionTransformer, StandardScaler, MinMaxScaler, MaxAbsScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
''' evaluate '''
from sklearn.model_selection import cross_val_score
from sklearn import metrics
''' save model '''
import joblib


class DummyTransformer(FunctionTransformer):
    pass


def main():
    ''' concate all records
    '''
    log_files = sys.argv[1:]

    dfs = []
    for j in log_files:
        data = pd.read_json(j)
        dfs.append(data)

    dataset = pd.concat(dfs, ignore_index=True)

    print(dataset.shape)
    print(dataset.head())
    print(dataset.describe())

    print(dataset.columns)

    print(dataset)

    x = dataset[[
        'ball_x', 'ball_y', 'platform_x', 'dir_x', 'dir_y', 'dir_x2', 'dir_y2'
    ]]
    y = dataset['command']

    le = preprocessing.LabelEncoder()
    y_encoded = le.fit_transform(y)

    print(y_encoded)
    print(le.classes_)
    joblib.dump(le.classes_, 'araknoid_classes')

    #transformer = StandardScaler().fit(x)
    transformer = MinMaxScaler().fit(x)
    #transformer = MaxAbsScaler().fit(x)

    x_trans = transformer.transform(x)

    print(x_trans)
    '''
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.scatter3D(x['dir_x'], x['dir_y'], y_encoded)

    ax.set_xlabel('dir_x')
    ax.set_ylabel('dir_y')
    ax.set_zlabel('command')
    plt.show()

    return
    '''

    x_train, x_test, y_train, y_test = train_test_split(x_trans,
                                                        y_encoded,
                                                        test_size=0.3)
    '''
    model = KNeighborsClassifier(
        n_neighbors=3,
        weights='distance',
        algorithm='kd_tree',
        n_jobs=-1,
    )
    '''
    model = DecisionTreeClassifier(random_state=0)
    #model = LinearSVC()
    #model = RandomForestClassifier()
    print(model)

    model.fit(x_train, y_train)
    score = model.score(x_train, y_train)
    print("Score: ", score)

    #cv_scores = cross_val_score(model, x_train, y_train, cv=10)
    #print("CV average score: %.2f" % cv_scores.mean())

    y_pred = model.predict(x_test)

    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
    #cm = metrics.confusion_matrix(y_test, y_pred)
    #print(cm)
    #cr = metrics.classification_report(y_test, y_pred)
    #print(cr)

    joblib.dump(transformer, 'araknoid_scaler')
    joblib.dump(model, 'araknoid_model')


if __name__ == "__main__":
    main()
