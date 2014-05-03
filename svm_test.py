#! /usr/bin/env python

# modified version of sample code found: http://www.ajbradley.com/blog/20130622

import csv
import numpy as np
from sklearn import svm, datasets, cross_validation
from sklearn.grid_search import GridSearchCV

trainTargetArray = []
trainDataArray = []
max = 8
for i in range(1,max):
    with open('./data' + str(i) + '.csv', 'r') as trainFile:
        trainReader = csv.reader(trainFile, delimiter = ',')
        for row in trainReader:
            trainTargetArray.append(row[0])
            trainDataArray.append(row[1:])

trainData = np.array(trainDataArray)
trainTarget = np.array(trainTargetArray)

testTargetArray = []
testDataArray = []
with open('./data' + str(max) + '.csv', 'r') as testFile:
    testReader = csv.reader(testFile, delimiter = ',')
    for row in testReader:
        testTargetArray.append(row[0])
        testDataArray.append(row[1:])

testTarget = np.array(testTargetArray)
testData = np.array(testDataArray)

#Set up classification and fit the model data
svc = svm.SVC(gamma=0.128, C=1)
svc.fit(trainData, trainTarget)

#Predict/Determine Value of New Images
prediction = svc.predict(testData)

#Save output to file
output = open('./output.csv', 'w')
total = 0 
correct = 0
for x, value in np.ndenumerate(prediction):
    if(testTarget[x] == value):
        correct +=1
    output.write(str(int(value)))
    output.write("\n")
    total += 1
output.close()

print("%.3f%% Correct" % (100*correct/total))
