# -*- coding: utf-8 -*-
"""
Created on Sat May  2 00:06:52 2020

@author: abhil
"""


import sys
import pandas as pd
from Project import *
import numpy as np
    




if __name__== "__main__":
    
    print("Please enter CSV file name and second argument as the dose")
    Csvfilename = input("Enter the CSV file name")
    dose = input("Enter the dose")    
    
    dataframes = pd.read_csv(Csvfilename)
    
    p = Project()
    cor = p.correlationafterthreemonths(dataframes)
    coreal60 = p.calculatecorelationbydose(dataframes,dose)
    p.plotbox(dataframes,['bcarot','vite','age','bmi','dose','chol'])
    


dataframes = pd.read_csv('bcarotene.csv')


dataframes[dataframes['ptid'].unique()]



a = dataframes.groupby(['ptid', 'male'], as_index=False).

print(a)

print (dataframes.groupby('ptid').groups)

print(type(a))


def checkIn(d, val):
	try:
		a = d[val]
		return True
	except:
		return False

def addTo(dic, key, value):
	dic.update({key : value})
	return dic


dic = {}
for index, row in dataframes.iterrows():
    
	if checkIn(dic, row[0]) == False:
		dic = addTo(dic, row[0], [row[6],row[5],row[7],row[8]])
        

 
def CountmaleandFemale(d):
    male = 0
    female = 0   
    maleage = []
    femaleage = []
    bmifemale = []
    cholfemale = []
    bmimale = []
    cholmale = []
    for index,value in d.items():
        print(value)
        if(value[0]==0.0):
            print('in if')
            female=female+1
            femaleage.append(value[1])
            bmifemale.append(value[2])
            cholfemale.append(value[3])
            
        else:
     
            male=male+1
            maleage.append(value[1])
            bmimale.append(value[2])
            cholmale.append(value[3])
    return male,female,np.mean(maleage),np.mean(femaleage),np.mean(bmimale),np.mean(bmifemale),np.mean(cholmale),np.mean(cholfemale)
        
male,female,meanmaleage,meanfemaleage,bmimale,bmifemale,cholmale,cholfemale=CountmaleandFemale(dic)        

data = [['Male', male, meanmaleage, bmimale, cholmale ], ['Female', female, meanfemaleage, bmifemale, cholfemale ]]

df = pd.DataFrame(data,columns=['Parameter','Count','Age','BMI','Cholestrol']) 
   




             



        