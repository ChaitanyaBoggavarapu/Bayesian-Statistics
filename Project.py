import pandas as pd

import numpy as np

from matplotlib import pyplot as plt

from matplotlib import *



##To quantify Quantify whether the effect of treatment on serum beta-carotene differs by age, gender, BMI, or cholesterol

##Creatinf Dataframe with months doeses taken i.e months greater than 3

class Project:
    def correlationafterthreemonths(self,dataframe):
        self.dataframe = dataframe
        dataframe_new = self.dataframe[self.dataframe['month'] > 3]
        
        #print(dataframe_new.corr)     
        
        corel = dataframe_new.corr()
        print(corel)
#        s#elf.plotheapmap(corel)
        return corel
    #plt.matshow(cor)
    
    ##Create a new list varibale to append
    
    
    
    
    
    def plotheapmap(self,corelationvriable):
        
    
        labels = [c[:2] for c in corelationvriable.columns]
        
        fig = plt.figure(figsize=(12,12))
        ax = fig.add_subplot(111)
        
        ax.matshow(corelationvriable, vmin=-1, vmax=1,cmap="RdYlGn")
        cmap = "RdYlGn"
        fig.colorbar(cm.ScalarMappable(norm=None, cmap=cmap))
        
        ax.set_xticks(np.arange(len(labels)))
        ax.set_yticks(np.arange(len(labels)))
        
        ax.set_xticklabels(labels)
        ax.set_yticklabels(labels)
        plt.title("Correlation of Variables")
        plt.show()
    
    
    
    def calculatecorelationbydose(self,dataframe,dose):
        
        #corelationdataframe = pd.DataFrame()
        dataframe_dose = self.dataframe[self.dataframe['dose'] ==int(dose)]
        print(dataframe_dose['dose'])
        newcor = dataframe_dose.corr()
        print(newcor)
        #corelationdataframe.append(newcor)
        
        #self.plotheapmap(newcor)
        return newcor
     
    def plotbox(self,dataframe,Enterlistforboxplot):
        
        for i in range(len(Enterlistforboxplot)):
            plt.figure()
    
            self.dataframe.boxplot(column=Enterlistforboxplot[i])
            
            
            plt.savefig(Enterlistforboxplot[i]+".png")
    
        
    def getmeansbylistbygender(self,dataframe,Entermaleandfemaleinlist):
        
        
        for i in range(len(Entermaleandfemaleinlist)):
            count = 
            
            
        
        
        
        
        


