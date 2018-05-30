from cluster import *
import numpy as np 
import random
import math
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
import imageio

def init(noc,points,ite):
    images = []
    initMu(points)
    kList = [Cluster(initMu(points),initSigma(points),initPi(points),setPoints(points),[]) for _ in range(noc)]
    iteraciones= 0
    while(iteraciones<=ite):
        for point in points:
            point = np.matrix(point).T
            R = 0
            for cluster in kList:
                det = abs(np.linalg.det(cluster.sigma))
                if(det<=0):
                    det=0.00001
                inside = math.exp( -0.5 * (((point - cluster.mu.T).T).dot(np.linalg.inv(cluster.sigma)).dot(point - cluster.mu.T)))
                if inside<=0:
                    inside=0.00001
                e = cluster.pi * math.pow((2*math.pi),-1) * math.pow(det,-0.5) * inside
                R += e
                cluster.setE(e)
        for cluster in kList:
            cluster.normE(R)
            cluster.updatePi()
            cluster.updateMu()
            cluster.updateSigma()
            del cluster.e[:]
        images.append(imageio.imread(graph(points,kList,iteraciones)))
        iteraciones +=1
    imageio.mimsave('movie.gif', images)
    another(kList,len(points),points)


def graph(points,clusters,iter):
    x,y = points.T
    plt.scatter([x],[y],color=['black'])
    mus = np.array([cluster.mu for cluster in clusters])
    x1,y1 = mus.T
    plt.scatter([x1],[y1],color=['red'])
    plt.savefig('images/myfig'+str(iter)+'.png')
    return 'images/myfig'+str(iter)+'.png'

def another(clusters,n,points):
    fig, ax = plt.subplots()
    figures = []
    x,y = points.T
    plt.scatter([x],[y],color=['black'])
    colors = "bgrcmykw"
    for i in range(len(clusters)):
        gaussian = clusters[i]
        mu = np.squeeze(np.asarray(gaussian.mu))
        values, vectors = eigenso(gaussian.sigma)
        th = np.degrees(np.arctan2(*vectors[:, 0][::-1]))
        for j in range(0, 3):
            width, height = j * np.sqrt(values)
            elipse = Ellipse(xy=(mu[0], mu[1]), width=width, height=height, angle=th, color=colors[i])
            elipse.set_facecolor('none')
            ax.add_artist(elipse)
        ax.scatter(mu[0], mu[1], marker='^', color=colors[i])
        figures.append(np.random.multivariate_normal([mu[0], mu[1]], gaussian.sigma, n))
        for figure in figures:
            plt.scatter(figure[:,0],figure[:,1],c='b',s=20,edgecolors='none', alpha=0.5)
    plt.show()

def initMu(points):
    x,y = points.T
    maxX = np.amax(x)
    maxY = np.amax(y)
    minX = float(np.ndarray.min(x))
    minY = float(np.ndarray.min(y))
    pointx = random.uniform(minX,maxX)
    pointy = random.uniform(minY,maxY)
    return np.matrix([pointx,pointy])

def initSigma(points):
    return np.cov(points.T)

def initPi(points):
    return 1/float(len(points))

def setPoints(points):
   return [ np.matrix(point).T  for point in points]

def eigenso(covariance_):
    values_, vectors_ = np.linalg.eigh(covariance_)
    order = values_.argsort()[::-1]
    return values_[order], vectors_[:, order]


