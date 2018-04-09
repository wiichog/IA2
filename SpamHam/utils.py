import random
from functools import reduce
from collections import Counter
import pickle

class utils:

    def __init__(self):
        self.spam = {}
        self.ham = {}
        self.spamWords = []
        self.hamWords = []
        self.training = []
        self.crossValidation = []
        self.test = []
        self.k = 1

    def analizer(self,lines,g,f,word):
        for line in lines:
            cleanLine = line.split("\t")[0].lower() + '\t' + ''.join([c.lower() for c in line.split("\t")[1] if(ord(c.lower())>=97 and ord(c.lower())<=122 or ord(c.lower())==32)])
            if(line.split("\t")[0].lower()==word):
                g(cleanLine)
            else:
                f(cleanLine)

    def addDictionary(self,dictionary,words):
        words = words.split("\t")[1].split(" ")
        for word in words:
            if((word.lower() not in dictionary) and len(word)>1):
                dictionary[word.lower()] = 1
            elif((word.lower() in dictionary) and len(word)>1):
                dictionary[word.lower()] += 1

    def partitions(self):
        random.shuffle(self.spamWords)
        random.shuffle(self.hamWords)
        #self.training.extend(self.spamWords)
        #self.training.extend(self.hamWords)
        self.training.extend(self.spamWords[:int(len(self.spamWords)*0.8)])
        self.training.extend(self.hamWords[:int(len(self.hamWords)*0.8)])
        self.crossValidation.extend(self.spamWords[int(len(self.spamWords)*0.8):int(len(self.spamWords)*0.9)])
        self.crossValidation.extend(self.hamWords[int(len(self.hamWords)*0.8):int(len(self.hamWords)*0.9)])
        self.test.extend(self.spamWords[int(len(self.spamWords)*0.9):])
        self.test.extend(self.hamWords[int(len(self.hamWords)*0.9):])
        
    def saveDicts(self,dic,tag):
        pickle.dump( dic, open( ""+tag+".p", "wb" ) )

    def getPSpamGivenSentence(self,sentence):
        ulist = []
        [ulist.append(x) for x in sentence if x not in ulist]
        #print([self.getPOfWordGivenSpam(word,self.spam)**sentence.count(word) for word in ulist])
        #print([self.getPOfWordGivenSpam(word,self.ham)**sentence.count(word) for word in ulist])
        a = (reduce((lambda x, y: x * y), [self.getPOfWordGivenSpam(word.lower(),self.spam)**sentence.count(word) for word in ulist]) * self.getPOfDict("spam"))
        b = (reduce((lambda x, y: x * y), [self.getPOfWordGivenSpam(word.lower(),self.ham)**sentence.count(word) for word in ulist]) * self.getPOfDict("ham"))
        return a/float(a+b)
        
    def getPOfWordGivenSpam(self,word,dict):
        a = set(self.spam.keys()).symmetric_difference(self.ham.keys())
        try:
            return (dict.get(str(word))+self.k)/float(sum(dict.values())+self.k*(len(a)))
        except:
            return (0+self.k)/float(sum(dict.values())+self.k*(len(a)))


    def getPOfDict(self,dict):
        return (sum([1 for message in self.training if(message.split("\t")[0]==dict)]) + self.k)/float(len(self.training)+self.k*(2))
        
        
        
        
