# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 23:08:32 2019

@author: prasanth
"""
import random                                                      
import pandas as pd
import numpy as np
from scipy.stats import norm
btc = pd.DataFrame(pd.read_csv("bitcoin.csv"))
btc['Price']
btc.Price
btcReturns = [np.log(btc.Price[i]/btc.Price[i-1]) for i in range(8,2246)]
print(len(btcReturns))
btcprices = list(btc.Price[:2246])[::-1]
btcstd=np.std(btcReturns,ddof=1)
bavg=np.average(btcReturns)
drift=bavg-(btcstd**2)/2
print("the drift is")
print(drift)
print("the bavg is")
print(bavg)

a=999999999999999999999
for each in range(10000):
    f=[btc.Price[8]]
    for day in range(8):
        f.append(f[-1]*np.exp(drift+(btcstd*(norm.ppf(random.SystemRandom.random(0))))))
    ds=np.square((f[0:8:]-btc.Price[8:0:-1]))
    mofds=ds.mean()
    ans=np.sqrt(mofds)
    if(ans<a):
        a=ans
        g=f

print(g)
print(" mean square root error  when simulation are 100000:")
print(ans)
        

import matplotlib.pyplot as plt
plt.plot(g)
l =[]
l.extend(btc.Price[8:0:-1])
plt.plot(l, label = "Actual")
plt.plot(g, label="Predicted")
plt.legend(bbox_to_anchor=(.5,1), loc =0, borderaxespad=0.)
plt.show()