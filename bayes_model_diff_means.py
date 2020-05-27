# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:47:17 2020

@author: abhil
"""

import numpy as np
import pandas as pd
import pymc3
from pymc3 import Model,Normal,Uniform,StudentT,plot_posterior,fit,Deterministic

data = pd.read_csv("bcarotene.csv")


##After Drug Usage
dataframe_after_drug = data[data['month'] > 3].dropna()

##Before Drug Usage
dataframe_before_drug = data[data['month'] <= 3].dropna()




##Writing pymc3

beat_carotene_levels_before_drug = dataframe_before_drug.bcarot

beat_carotene_levels_after_drug = dataframe_after_drug["bcarot"]

##Comapring two means

with Model() as beta_carotene_model:
    mean1 = Uniform('mean1', lower=0, upper=1000)
    mean2 = Uniform('mean2', lower=0, upper=1000)
   
with beta_carotene_model:
    sigma1 = Uniform('sigma1',0,100)    
    sigma2 = Uniform('sigma2',0,100)

with beta_carotene_model:
    before_drug =Normal('before_drug',mu=mean1,sd=sigma1,observed=beat_carotene_levels_before_drug)     
    After_drug =Normal('After_drug',mu=mean2,sd=sigma2,observed=beat_carotene_levels_after_drug)     
    
with beta_carotene_model:
    diff_of_means=Deterministic("diff_of_means",mean2-mean1)    
    effect_size = Deterministic("effect_size",diff_of_means/np.sqrt((sigma1**2+sigma2**2)/2))

with beta_carotene_model:
    drug_traces=fit(random_seed=None).sample(1000)


plot_posterior(drug_traces[100:],varnames=['diff_of_means_Before_after_taking_drug','effect_size'],ref_val=0,color='#87ceeb')  
               
               
               