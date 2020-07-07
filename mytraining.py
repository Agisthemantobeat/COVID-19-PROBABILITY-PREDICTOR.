import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
import pickle


def data_split(data, ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data) * ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


if __name__ == "__main__":
    df=pd.read_csv('tested_personTable(1) - Copy.csv').dropna()
    train, test = data_split(df, 0.2)
    X_train=train[['fever','head_ache','sore_throat','age_60_and_above','cough','shortness_of_breath','test_indication']].to_numpy()
    X_test=test[['fever','head_ache','sore_throat','age_60_and_above','cough','shortness_of_breath','test_indication']].to_numpy()
    Y_train=train[['corona_result']].to_numpy().reshape(46571,)
    Y_test=test[['corona_result']].to_numpy().reshape(11642,)
    lab_enc = preprocessing.LabelEncoder()
    Y_train = lab_enc.fit_transform(Y_train)
    clf=LogisticRegression()
    clf.fit(X_train,Y_train)
    outfile = open('models.pkl', 'wb')
    pickle.dump(clf, outfile)
    outfile.close()
