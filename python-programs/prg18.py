import pylab as plt
empid=[101,102,103,104,105]
sal=[25000,35000,32000,10000,30000]
plt.bar(empid,sal, label='Employee data') 
plt.xlabel('Employee ID') 
plt.ylabel('Employee Salary') 
plt.title('EMPLOYEE CHART') 
plt.legend() 
plt.show()
