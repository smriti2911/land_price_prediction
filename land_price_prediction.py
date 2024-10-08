# -*- coding: utf-8 -*-
"""Land_price_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vSzoTTj7hriLs1vCOVDJ7HaCqBDshSEV
"""

import pandas as pd

from google.colab import files
uploaded = files.upload()

dataset = pd.read_csv('Dataset.csv')
datasetwithNaN = dataset
dataset

print(dataset.shape)
print(dataset.describe())

dataset.isna().any()

MeandatasetNotNan = dataset.price.fillna(dataset.price.mean())
MeandatasetNotNan

MediandatasetNotNan = dataset.price.fillna(dataset.price.median())
MediandatasetNotNan

dataset.describe()

percentile = dataset.price.quantile(1.0)
percentile

datasetNoOutlier = dataset[dataset.price<percentile]
datasetNoOutlier



###Permutation - with Length-2

from itertools import permutations
count=0
data = [1, 2, 3]
perm = permutations(data, 2)
for i in list(perm):
    print (i)
    count+=1

print("Permutation Count: ",count)

##Combination - with Length-2

from itertools import combinations
count=0
data = [1, 2, 3]
data2 = [2, 1, 3]
perm = combinations(data2, 2)
for i in list(perm):
    print (i)
    count+=1

print("Combination Count: ",count)

### Combination - with Length-2

from itertools import combinations_with_replacement as cr
count=0
data = [1, 2, 3]
data2 = [2, 1, 3]
perm = cr(data, 2)
for i in list(perm):
    print (i)
    count+=1

print("Combination with Element Count: ",count)