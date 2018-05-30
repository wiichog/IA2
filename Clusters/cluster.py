import numpy as np

class Cluster(object):
    def __init__(self,mu,sigma,pi,points,e):
        self.mu = mu
        self.sigma = sigma
        self.pi = pi
        self.points = points
        self.e = e
    
    def setE(self,e):
        self.e.append(e)
    
    def normE(self,r):
        if(r>0):
            self.e = [number/float(r) for number in self.e] 

    def updateMu(self):
        number = [0,0]
        for i in range(len(self.points)):
            number += self.points[i].T * self.e[i]
        self.mu = number/sum(self.e)
    
    def updatePi(self):
        self.pi = sum(self.e)/float(len(self.points))

    def updateSigma(self):
        sigma = np.matrix([[0,0],[0,0]]).astype(float)
        number = 0
        for i in range(len(self.points)):
            nextSigma = self.e[i] * ((self.points[i] - self.mu.T).dot((self.points[i] - self.mu.T).T))
            sigma = sigma + nextSigma
        self.sigma = sigma/sum(self.e)