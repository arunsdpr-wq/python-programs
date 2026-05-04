from matplotlib import pyplot as plt
data=[25,25,20,20,10]
dept=['IT','Account','Sales','Purchase','HR']
plt.pie(data,labels=dept) 
plt.title('Pie chart showing the percentage of employees in each department of a company.')
plt.show()
