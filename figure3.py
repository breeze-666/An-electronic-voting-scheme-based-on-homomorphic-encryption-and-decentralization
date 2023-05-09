#coding=UTF-8

import matplotlib.pyplot as plt
import numpy as np
plt.rc('font',family='Times New Roman')
#plt.rcParams['font.family']='serif'
#plt.rcParams['font.sans-serif']=['Times New Roman']
#plt.rcParams['axes.unicode_minus']=False
# epoch,acc,loss,val_acc,val_loss
x_axis_data = [1000, 2000, 4000, 7000, 10000]
Cost_e=0.0068
Nc=5
y_axis_data1 = [2*Cost_e*x_axis_data[0]*Nc ,  2*Cost_e*x_axis_data[1]*Nc ,  2*Cost_e*x_axis_data[2]*Nc ,2*Cost_e*x_axis_data[3]*Nc  ,2*Cost_e*x_axis_data[4]*Nc]
y_axis_data2= [6*Cost_e*Nc*x_axis_data[0]+4*Cost_e ,6*Cost_e*Nc*x_axis_data[1]+4*Cost_e ,6*Cost_e*Nc*x_axis_data[2]+4*Cost_e  ,6*Cost_e*Nc*x_axis_data[3]+4*Cost_e ,6*Cost_e*Nc*x_axis_data[4]+4*Cost_e]


# plot
plt.plot(x_axis_data, y_axis_data1, '^-', alpha=0.5, linewidth=1, label='HED-Voting', color='black')  
plt.plot(x_axis_data, y_axis_data2, 's--', alpha=0.5, linewidth=1, label='HSE-Voting',color='black')

plt.title('The time cost comparison of 5 candidates for CC')
plt.legend()  # show the label
plt.xlabel('The number of voters')
plt.ylabel('Time cost(s)')  # accuracy
plt.grid(axis="y",color='black',ls='dotted')

# plt.ylim(-1,1)#set ylabel
plt.show()
