import numpy as np 
from numpy.linalg import inv,det
import random
import math
import copy
import matplotlib.pyplot as plt

def NNP(numberOfClusters,lines):
    mu = np.array([ [round(random.random()*100),round(random.random()*100)] for _ in range(numberOfClusters) ]).astype(float)
    points = {}
    sigma = [np.array([[round(random.random()*100),round(random.random()*100)],[round(random.random()*100),round(random.random()*100)]])
    for _ in range(numberOfClusters)
    ]
    for matrix in sigma:
        while(True):
            if(np.allclose(np.dot(matrix, inv(matrix)), np.eye(2))): 
                break
            else:
                matrix = np.array([[round(random.random()*100),round(random.random()*100)],[round(random.random()*100),round(random.random()*100)]])
    pi = np.random.dirichlet(np.ones(numberOfClusters),size=1)[0]
    counter = 0
    while(True):
        firstSigma = copy.copy(sigma)
        firstPi = copy.copy(pi)
        firstMu = copy.copy(mu)
        for line in lines:
            xj = np.array(line.replace("\n","").split(",")).astype(float)
            r = 0
            e = []
            for i in range(numberOfClusters):
                minus = np.matrix(xj - mu[i])
                tr = minus.transpose()
                print(abs(det(sigma[i]))**(-1/2))
                e.append(pi[i] * ((2*math.pi)**-1) * abs(det(sigma[i]))**(-1/float(2)) * np.exp(-0.5 * minus.dot(inv(sigma[i]).dot(tr))))
                r += e[-1]
            e = [p/float(r) for p in e]
            points[line.replace("\n","")] = e
            counter +=1
        for i in range(numberOfClusters):
            sume = sum([e[i] for e in list(points.values())])
            pi[i] = sume/float(counter)
            mu[i] = updateMu(i,points,counter,sume)
            print(sigma)
            sigma[i] = updateSigma(i,points,mu,counter,sume)
        if(equalsMu(mu,firstMu) and equalsSigma(sigma,firstSigma) and equalsPi(pi,firstPi)):break
    print(mu)
    
    #x = [item.split(",")[0] for item in list(points.keys())]
    #y = [item.split(",")[1] for item in list(points.keys())]
    #plt.scatter(x, y)
    #plt.show()

def updateSigma(position,points,mu,counter,sume):
    sigma1 = np.matrix([[0.0,0.0],[0.0,0.0]])
    for point in points.keys():
        e = points.get(point)[position]
        tr = (np.matrix(point.split(",")).astype(float) - mu[position])
        sub = (np.matrix(point.split(",")).astype(float) - mu[position]).transpose()
        result = (e * tr * sub)
        sigma1 = sigma1 + result
    
    return sigma1/sume

def updateMu(position,points,counter,sume):
    emu = [0.0,0.0]
    for point in list(points.keys()):
        e = points.get(point)[position]
        x = np.array(point.split(",")).astype(float)
        newmu = e*x
        emu = [x + y for x, y in zip(emu, newmu)]
    c = np.array([item/sume for item in emu])
    return c

def equalsSigma(Matrix1,Matrix2):
    true = []
    for i in range(len(Matrix1)):
        a = Matrix1[i]
        b = Matrix2[i]
        for g in range(len(a)):
            data1 = a[g]
            data2 = b[g]
            for h in range(len(data1)):
                true.append(math.isclose(data1[h], data2[h], abs_tol=0.01))
    return(all(item ==True for item in true))

def equalsPi(Array1,Array2):
    true = []
    for i in range(len(Array1)):
        a = Array1[i][0]
        b = Array2[i]
        true.append(math.isclose(a, b, abs_tol=0.01))
    return(all(item ==True for item in true))

def equalsMu(Matrix1,Matrix2):
    true = []
    for i in range(len(Matrix1)):
        a = Matrix1[i]
        b = Matrix2[i]
        for g in range(len(a)):
            data1 = a[g]
            data2 = b[g]
            true.append(math.isclose(data1, data2, abs_tol=0.01))
    return(all(item ==True for item in true))
    