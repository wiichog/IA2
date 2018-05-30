from tkinter.filedialog import askopenfilename
from utils import init
import numpy as np 


#filename = askopenfilename()
lines = open("1.txt").readlines()
numberOfClusters = input("Ingrese el numero de clusters ")
ite = input("Ingrese el numero de iteraciones ")
points = np.matrix([np.array(point.replace("\n","").replace("[","").replace("]","").split(",")).astype(float) for point in lines])
init(int(numberOfClusters),points,int(ite))
