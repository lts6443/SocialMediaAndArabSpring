# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 04:36:44 2014

@author: Lou
"""
from sklearn import svm
from sklearn import preprocessing
from sklearn.cluster import KMeans
import numpy

data = numpy.loadtxt(fname="sampledata.csv", delimiter=",", skiprows=1)
with open('sampledata.csv', 'r') as f:
  first_line = f.readline()

X_scaled = preprocessing.scale(data)

X_scaled.mean(axis=0)
X_scaled.std(axis=0)
scaler = preprocessing.StandardScaler().fit(data)  


km = KMeans(3)
km.fit(data)


fig = pylab.figure(1, figsize=(8,6))
axes = Axes3D(fig, rect=[0, 0, 1, 1], elev=48, azim=134)
labels = km.labels_

axes.scatter(data[:, 194], data[:, 220], data[:, 223], c=labels)

axes.w_xaxis.set_ticklabels([])
axes.w_yaxis.set_ticklabels([])
axes.w_zaxis.set_ticklabels([])
axes.set_xlabel("Cairo")
axes.set_ylabel("Jan25")
axes.set_zlabel("Egypt")