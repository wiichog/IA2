from tkinter.filedialog import askopenfilename
from utils import *

filename = askopenfilename()
lines = open(filename).readlines()
operations = utils()
operations.analizer(lines)
operations.partitions()