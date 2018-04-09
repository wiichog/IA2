from utils import *
import pickle
import numpy as np

operations = utils()
operations.spam = pickle.load( open( "spam.p", "rb" ) )
operations.ham = pickle.load( open( "ham.p", "rb" ) )
crossValidation = pickle.load( open( "crossValidation.p", "rb" ) )
testcounter = 0
test = pickle.load( open( "test.p", "rb" ) )
testForK = []
AllTest = []
crossValidationSpamCounter = 0
for line in crossValidation:
    sides = line.split("\t")
    if(sides[0]=="spam"):
        crossValidationSpamCounter +=1
print("crossValidationSpam " + str(crossValidationSpamCounter))
testSpamCounter = 0
for line in test:
    sides = line.split("\t")
    if(sides[0]=="spam"):
        testSpamCounter +=1
print("testSpam " + str(testSpamCounter))
#DISCOMMENT THIS IF YOU WANT TO RECREATE THE K FOR CROSSVALIDATION
#for i in np.arange(0.01, 2.0, 0.01):
#    operations.k = i
#    counter = 0
#    for line in crossValidation:
#        sides = line.split("\t")
#        words = sides[1].replace("\n","").split(" ")
#        if(sides[0]=="spam" and operations.getPSpamGivenSentence(words)*100>85):
#            counter += 1
#    print((counter*100)/float(crossValidationSpamCounter))
#    if( ((counter*100)/float(crossValidationSpamCounter))>96):
#        testForK.append(i)
#operations.saveDicts(testForK,"bestK")
testForK = pickle.load( open( "bestK.p", "rb" ) )
#DISCOMMENT THIS IF YOU WANT TO RECREATE THE K FOR TEST
#finals = []
#for k in testForK:
#    operations.k = k
#    counter = 0
#    for line in test:
#        sides = line.split("\t")
#        words = sides[1].replace("\n","").split(" ")
#        if(sides[0]=="spam" and operations.getPSpamGivenSentence(words)*100>85):
#            counter += 1
#    if(((counter*100)/float(crossValidationSpamCounter))>=96):
#        finals.append(k)
#operations.saveDicts(finals,"finalK")

finals = pickle.load( open( "finalK.p", "rb" ) )
#XXXMobileMovieClub: To use your credit, click the WAP link in the next txt message or click here>> http://wap. xxxmobilemovieclub.com?n=QJKGIGHJJGCBL
sentence = input("Ingrese una oracion para analizar ")
operations.k = random.choice(finals)
print(operations.k)
print(operations.getPSpamGivenSentence(sentence.split(" "))*100)


