import numpy as np
from scipy.stats import chi2_contingency
a1=np.array([[15,12],[18,9]])
chi2_stat,p_value,dof,expected=chi2_contingency(a1)
if p_value <0.05:
  print("Its a Reject Hypothesis:There is a significant association between variables")
else:
  print("Fail to Reject a  Null Hypothesis")