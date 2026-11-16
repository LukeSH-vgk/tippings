from fitting_functions import *
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
data = np.loadtxt("tips.csv", delimiter=",", dtype=str)

x = data[1:, 0].astype(np.float32)  # bills
y = data[1:, 1].astype(np.float32)  # tips
print("y = ", y)
print("x = ", x)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
m = params[0]
b = params[1]

fig = plt.figure()
plt.scatter(x, y)
plt.plot(x,linear(m,x,b),label='Fitted line')
plt.xlabel("bills ($)")
plt.ylabel("tips ($)")
plt.show()
fig.savefig('TIPSplot.png')

print_equ(m,b,"dollars","dollars")
# for tips over bills: y = 0.18221473222560391 dollars/dollars x + -0.2922674195507699 dollars

x = data[1:, 0].astype(np.float32)  # bills
y = data[1:, -1].astype(np.float32)  # Pcttip
print("y = ", y)
print("x = ", x)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
m = params[0]
b = params[1]

fig = plt.figure()
plt.scatter(x, y)
plt.plot(x,linear(m,x,b),label='Fitted line')
plt.xlabel("bills ($)")
plt.ylabel("PctTips (%)")
plt.show()
fig.savefig('PCTplot.png')

print_equ(m,b,"dollars","Percentage")
# bills over percentage: y = 0.04881243455874584 Percentage/dollars x + 15.509648238069316 Percentage
fig.savefig('dataplot.png')
