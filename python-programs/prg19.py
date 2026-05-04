import pandas as pd 
import matplotlib.pyplot as plt 
data = [['101', 'M', 34], 
        ['102', 'F', 40], 
        ['103', 'F', 37], 
        ['104', 'M', 30], 
        ['105', 'F', 44], 
        ['106', 'M', 36], 
        ['107', 'M', 32], 
        ['108', 'F', 26], 
        ['109', 'M', 32], 
        ['111', 'M', 36]]  
df = pd.DataFrame(data)
df.hist() 
plt.title('Histogram Showing the number of Employees in Specific Age Groups')
plt.show()
