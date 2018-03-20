import random

class utils:
    spam = {}
    ham = {}
    spamWords = []
    hamWords = []
    training = []
    crossValidation = []
    test = []

    def __init__(self):
        pass

    def analizer(self,lines):
        for line in lines:
            cleanLine = ''.join([c.lower() for c in line.split("\t")[1] if(ord(c.lower())>=97 and ord(c.lower())<=122 or ord(c.lower())==32)])
            if(line.split("\t")[0].lower()=="ham"):
                self.addDictionary(self.ham,cleanLine.split(" "))
                self.hamWords.append(cleanLine)
            else:
                self.addDictionary(self.spam,cleanLine.split(" "))
                self.spamWords.append(cleanLine)

    def addDictionary(self,dictionary,words):
        for word in words:
            if((word.lower() not in dictionary) and len(word)>1):
                dictionary[word.lower()] = 0
            elif((word.lower() in dictionary) and len(word)>1):
                dictionary[word.lower()] += 1

    def partitions(self):
        random.shuffle(self.spamWords)
        random.shuffle(self.hamWords)
        print("spamWords len "+str(len(self.spamWords)))
        print("hamWords len "+str(len(self.hamWords)))
        print("Suma "+str(len(self.spamWords)+len(self.hamWords)))
        self.training.extend(self.spamWords[:int(len(self.spamWords)*0.8)])
        self.training.extend(self.hamWords[:int(len(self.hamWords)*0.8)])
        self.crossValidation.extend(self.spamWords[int(len(self.spamWords)*0.8):int(len(self.spamWords)*0.9)])
        self.crossValidation.extend(self.hamWords[int(len(self.hamWords)*0.8):int(len(self.hamWords)*0.9)])
        self.test.extend(self.spamWords[int(len(self.spamWords)*0.9):])
        self.test.extend(self.hamWords[int(len(self.hamWords)*0.9):])
        print("training len "+str(len(self.training)))
        print("crossValidation len "+str(len(self.crossValidation)))
        print("test len "+str(len(self.test)))
        print("suma total "+str(len(self.training)+len(self.crossValidation)+len(self.test)))
        
        
        
