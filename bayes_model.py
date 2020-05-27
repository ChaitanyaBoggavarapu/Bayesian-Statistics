# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:18:46 2020

@author: abhil
"""
import numpy as np
import pandas as pd
import pymc3
import seaborn as sns


#print(np.log(4))

data = pd.read_csv("bcarotene.csv")


##After Drug Usage
dataframe_after_drug = data[data['month'] > 3].dropna()

##Before Drug Usage
dataframe_before_drug = data[data['month'] <= 3].dropna()




##Writing pymc3

beat_carotene_levels_before_drug = dataframe_before_drug.bcarot

beat_carotene_levels_after_drug = dataframe_after_drug["bcarot"]

beat_carotene_levels_before_drug_array = np.asarray(beat_carotene_levels_before_drug)

print(np.mean(beat_carotene_levels_after_drug))
print(np.mean(beat_carotene_levels_before_drug))

##plotting histogram

sns.distplot(beat_carotene_levels_before_drug).set_title("beat_carotene_levels_before_drug")

sns.distplot(beat_carotene_levels_after_drug).set_title("beat_carotene_levels_after_drug")


beat_carotene_levels_before_drug.shape
##Looks like normal distribution on no_drug_affect will choose normal prior assuming mean ranging fromN(0,100) and variance U(0,10)

from pymc3 import Model,Uniform,Normal

with Model() as beta_carotene_model:
    mean = Uniform('mean', lower=0, upper=500)
    sigma = Uniform('sigma',0,100)
    





##Getting Likelihood and we assumed it cacanormal

with beta_carotene_model:
    print(beat_carotene_levels_before_drug)
    y = Normal('beat_carotene_levels_before_drug',mu=mean,sd=sigma,observed=beat_carotene_levels_before_drug)
    
    


##Calculate posterior distribution here we are using variational inference
    
from pymc3 import fit

with beta_carotene_model:
    samples=fit(random_seed=None).sample(1000)



##plot posterior
    
from pymc3 import plot_posterior

plot_posterior(samples,varnames=['mean'],ref_val=240,color="LightSeaGreen")    

##What is the probability a randomly choose person willhave higher beta carotene level more than 130
    
mus = samples["mean"]
sigmas = samples["sigma"]

random_samples = Normal.dist(mus,sigmas).random()

sns.distplot(random_samples,label='simulated')
sns.distplot(beat_carotene_levels_before_drug,label="observed")

###Doing the samething on the after taking drugs 


with Model() as beta_carotene_model_after_drug:
    mean = Uniform('mean', lower=0, upper=10000)
    sigma = Uniform('sigma',0,100)
    





##Getting Likelihood and we assumed it cacanormal

with beta_carotene_model_after_drug:
    print(beat_carotene_levels_after_drug)
    y = Normal('beat_carotene_levels_after_drug',mu=mean,sd=sigma,observed=beat_carotene_levels_after_drug)
    
    


##Calculate posterior distribution here we are using variational inference
    
from pymc3 import fit

with beta_carotene_model_after_drug:
    samples=fit(random_seed=None).sample(1000)



##plot posterior
    
from pymc3 import plot_posterior

plot_posterior(samples,varnames=['mean'],ref_val=240,color="LightSeaGreen")    

##What is the probability a randomly choose person willhave higher beta carotene level more than 130
    
mus = samples["mean"]
sigmas = samples["sigma"]

random_samples = Normal.dist(mus,sigmas).random()

sns.distplot(random_samples,label='simulated')
sns.distplot(beat_carotene_levels_after_drug,label="observed")

