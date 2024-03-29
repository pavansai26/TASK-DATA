# -*- coding: utf-8 -*-
"""newdata.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EL1PN5WP6qwyNMfN5Vb0MTK5kG7Z6gqB
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/gdrive')

data=pd.read_csv('/gdrive/My Drive/musk_csv.csv')

data

data.info()

data.describe()

data.count()

data.isnull().sum()

data.shape

sns.distplot(data['f3'])

sns.distplot(data['f1'])

sns.distplot(data['f4'])

sns.distplot(data['f5'])

sns.distplot(data['f6'])

sns.distplot(data['f7'])

sns.distplot(data['f8'])

sns.distplot(data['f9'])

sns.distplot(data['f10'])

sns.distplot(data['f11'])

sns.distplot(data['f12'])

sns.distplot(data['f13'])

sns.distplot(data['f14'])

sns.distplot(data['f15'])

sns.distplot(data['f16'])

sns.distplot(data['f17'])

sns.distplot(data['f18'])

sns.distplot(data['f19'])

sns.distplot(data['f20'])

sns.distplot(data['f21'])

sns.distplot(data['f22'])

sns.distplot(data['f23'])

sns.distplot(data['f24'])

sns.distplot(data['f25'])

sns.countplot(data['class'])

aa=data.iloc[:,4:169].corr()

plt.figure(figsize=(10,10))
ax = sns.heatmap(aa,cmap="RdYlGn",annot=True,annot_kws={"size": 7.5},linewidths=.5)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right");

to_drop = [column for column in aa.columns if any([aa[column] > 0.8 ] and aa[column] <0.3 )]

data.drop(data[to_drop], axis=1)

data

data['molecule_name'].unique().shape

data['conformation_name'].dtype

data.columns

data.shape

data['molecule_name'].unique()

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

encoded = data[['molecule_name','conformation_name']].apply(le.fit_transform)

encoded

data.keys()

new=data.drop(['molecule_name',	'conformation_name'],axis=1)

new

new[['molecule_name', 'conformation_name']]=encoded

new

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

new1=sc.fit_transform(new)

new2=pd.DataFrame(new1,columns=[data.keys()])

new2

y=new['class']

x=new2.drop('class',axis=1)

x.head(10)

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix,f1_score,roc_auc_score,roc_curve,precision_score,recall_score

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.2, stratify=y)

model=MLPClassifier( max_iter=100)

parameter_space = {
    'hidden_layer_sizes': [(50,50,50), (50,100,50), (100,)],
    'activation': ['tanh', 'relu'],
    'solver': ['sgd', 'adam'],
    'alpha': [0.0001, 0.05],
    'learning_rate': ['constant','adaptive'],
}

from sklearn.model_selection import GridSearchCV

model1= GridSearchCV(model, parameter_space, n_jobs=-1, cv=3)

print('Best parameters found:\n', model1.estimator)

model1=model1.estimator

model1.fit(x_train, y_train)
y_pred = model1.predict(x_test)

accuracy_score(y_test, y_pred)

cm = confusion_matrix(y_test, y_pred)
cm

sns.heatmap(cm, annot=True,center=True)
plt.show()

f1_score(y_test, y_pred)

roc_auc_score(y_test, y_pred)

roc_curve(y_test, y_pred)

precision_score(y_test, y_pred)

recall_score(y_test, y_pred)

from sklearn.metrics import classification_report
print('Results on the test set:')
print(classification_report(y_test, y_pred))

