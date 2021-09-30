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
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
''' evaluate '''
from sklearn.model_selection import cross_val_score
from sklearn import metrics
''' save model '''
import joblib


def main():
    ''' concate all records
    '''
    log_files = sys.argv[1:]

    dfs = []
    for j in log_files:
        data = pd.read_json(j)
        dfs.append(data)

    dataset = pd.concat(dfs, ignore_index=True)

    df = dict()
    df['left'] = dataset.query('direction == "left"')
    df['right'] = dataset.query('direction == "right"')
    df['forward'] = dataset.query('direction == "forward"')
    df['back'] = dataset.query('direction == "back"')

    print(dataset.shape)
    print(dataset.head())
    print(dataset.describe())

    print(dataset.columns)

    print(dataset)

    x = dataset[['smooth_left', 'smooth_front', 'smooth_right']]
    #y = dataset[['left_PWM', 'right_PWM']]
    y = dataset['direction']

    le = preprocessing.LabelEncoder()
    y_encoded = le.fit_transform(y)

    print(le.classes_)
    joblib.dump(le.classes_, 'KNN_classes')

    #transformer = StandardScaler().fit(x)
    transformer = MinMaxScaler().fit(x)

    dataset[['smooth_left', 'smooth_front',
             'smooth_right']] = transformer.transform(x)
    x_normal = dataset[['smooth_left', 'smooth_front', 'smooth_right']]

    print(x_normal)
    '''
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.scatter3D(x_normal['L_sensor'], x_normal['F_sensor'], x_normal['R_sensor'], c=y_encoded)

    ax.set_xlabel('L_sensor')
    ax.set_ylabel('R_sensor')
    ax.set_zlabel('F_sensor')
    plt.show()

    return
    '''

    x_train, x_test, y_train, y_test = train_test_split(x_normal,
                                                        y_encoded,
                                                        test_size=0.2)

    #model = KNeighborsClassifier(n_neighbors=4)
    #model = DecisionTreeClassifier(random_state=0)
    model = LinearSVC()
    #model = RandomForestClassifier()
    print(model)

    model.fit(x_train, y_train)
    score = model.score(x_train, y_train)
    print("Score: ", score)

    cv_scores = cross_val_score(model, x_train, y_train, cv=10)
    print("CV average score: %.2f" % cv_scores.mean())

    y_pred = model.predict(x_test)

    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
    #cm = confusion_matrix(y_test, ypred)
    #print(cm)
    #cr = classification_report(y_test, ypred)
    #print(cr)

    joblib.dump(transformer, 'KNN_scaler')
    joblib.dump(model, 'KNN_model')


if __name__ == "__main__":
    main()
