import numpy as np 
from numpy.linalg import inv,det
import random
from random import randint
import math
import copy
import matplotlib.pyplot as plt

def NNP(numberOfClusters,lines):
    mu = np.array([ np.matrix([randint(0, 500),randint(0, 500)]) for _ in range(numberOfClusters) ]).astype(float)
    points = {}
    sigma = [np.array([[randint(0, 500),randint(0, 500)],[randint(0, 500),randint(0, 500)]])
    for _ in range(numberOfClusters)
    ]
    for matrix in sigma:
        while(True):
            if(np.allclose(np.dot(matrix, inv(matrix)), np.eye(2)) and det(matrix)!=0): 
                break
            else:
                matrix = np.array([[randint(0, 500),randint(0, 500)],[randint(0, 500),randint(0, 500)]])
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
                invS = inv(sigma[i])
                minus = np.matrix(xj - mu[i]).transpose()
                tr = np.matrix(xj - mu[i])
                upNumber = pi[i] * np.exp(-0.5 * np.asscalar(tr.dot(invS).dot(minus)))
                DownNumber = (math.pow(2*math.pi,-1)) * (math.pow(abs(det(sigma[i])),-1/2))
                if(DownNumber==0):
                    DownNumber =DownNumber + 0.01
                elif upNumber==0:
                    upNumber= upNumber+0.01
                ej = upNumber / DownNumber
                e.append(ej)
                r += ej
            e = [p/float(r) for p in e]
            points[line.replace("\n","")] = e
            counter +=1
        for i in range(numberOfClusters):
            pi[i] = sum([e[i] for e in list(points.values())])/counter
            mu[i] = updateMu(i,points,firstMu)
            sigma[i] = updateSigma(i,points,mu,firstSigma)
        print("sigma before if ",sigma)
        if(equalsMu(mu,firstMu) and equalsSigma(sigma,firstSigma) and equalsPi(pi,firstPi)):break
    print(mu)
    
    #x = [item.split(",")[0] for item in list(points.keys())]
    #y = [item.split(",")[1] for item in list(points.keys())]
    #plt.scatter(x, y)
    #plt.show()

def updateSigma(position,points,mu,firstSigma):
    sigma1 = firstSigma[position]
    print("sigma1 ",sigma1)
    print("*********************")
    for point in points.keys():
        xj = np.matrix(point.split(",")).astype(float)
        print("xj ",xj)
        e = np.asscalar(points.get(point)[position])
        print("e ",e)
        tr = (xj - mu[position])
        print("tr ",tr)
        sub = (xj - mu[position]).transpose()
        print("sub ",sub)
        result = (e * sub.dot(tr))
        print("result ",result)
        sigma1 = sigma1 + result
        print(sigma1)
    print("*********************")
    print("e ", [e[position] for e in list(points.values())])
    sumE = sum([e[position] for e in list(points.values())])
    if(sumE==0):
        sumE = 0.01
    a = np.ma.log(sigma1)
    print("first ",a)
    print("In update ",sigma1)
    return sigma1/sum([e[position] for e in list(points.values())])

def updateMu(position,points,firstMu):
    mu1 = firstMu[position][0]
    for point in list(points.keys()):
        e = points.get(point)[position]
        x = np.array(point.split(",")).astype(float)
        newmu = e*x
        mu1 = [ newmu[i]+mu1[i] for i in range(len(newmu))]
    sumE = np.asscalar(sum([e[position] for e in list(points.values())]))
    if(sumE==0):
        sumE = 0.01
    c = np.array([item/sumE for item in mu1])
    return c

def equalsSigma(Matrix1,Matrix2):
    print(Matrix1)
    print(Matrix2)
    print(det[Matrix1])
    print(det[Matrix2])
    return True

def equalsPi(Array1,Array2):
    print(Array1)
    print(Array2)
    true = []
    for i in range(len(Array1)):
        a = Array1[i][0]
        b = Array2[i]
        true.append(math.isclose(a, b, abs_tol=0.01))
    return(all(item ==True for item in true))

def equalsMu(mu1,mu2):
    print("llega al if")
    return all([np.allclose(mu1[i][0], mu2[i][0],rtol=1e-03,) for i in range(len(mu1))])
    
    