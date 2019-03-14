# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 21:59:49 2019

@author: c1896292
"""
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

first_Suitable_Lane_Overflow = 9345
emptiest_Suitable_Lane_Overflow = 17791
fullest_Suitable_Lane_Overflow = 8115
random_Suitable_Lane_Overflow = 9337

objects = ('First Lane', 'Emptiest Lane', 'Fullest Lane', 'Random Lane')
y_pos = np.arange(len(objects))
performance = [first_Suitable_Lane_Overflow,emptiest_Suitable_Lane_Overflow,fullest_Suitable_Lane_Overflow,random_Suitable_Lane_Overflow]
 
plt.bar(y_pos, performance, align='center', alpha=1)
plt.xticks(y_pos, objects)
plt.ylabel('Overflow (cm)')
plt.title('Queueing System Overflow')
 
plt.show()
