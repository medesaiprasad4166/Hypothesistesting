import numpy as np
from scipy.stats import ttest_ind
a1=np.array([1.123,1.234,1.345,1.456,1.567])
a2=np.array([2.145,2.578,5.690,1.414,2.823])
ttest_ind,p_value=ttest_ind(a1,a2)
if p_value <0.05:
  print("Its a Null Hypothesis")
else:
  print("Fail to test a  Null Hypothesis")