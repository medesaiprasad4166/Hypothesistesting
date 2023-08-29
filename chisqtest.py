import numpy as np
from scipy.stats import f_oneway
a1=np.array([1.2,1.2,1.5])
a2=np.array([15,21,25])
a3=np.array([9.54,8.59,8.61])
f_stat,p_value=f_oneway(a1,a2,a3)
if p_value <0.05:
  print("Its a Null Hypothesis")
else:
  print("Fail to test a  Null Hypothesis")