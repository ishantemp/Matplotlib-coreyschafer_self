
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

# random list of values for scatter plots

x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]

sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
          538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

plt.scatter(x,y , s=sizes , c=colors ,cmap='Greens', edgecolor='black' , linewidth=1 , alpha=0.7)
# cmap is used for the main color of which shading will be used 



## for vertical colorbar with graph too be used as 'Satisfaction level'(coz our label is 'Satisfaction' here)
## i.e. for darker Satisfaction level will be high and so on for each shade of green color 
cbar = plt.colorbar()
cbar.set_label('Satisfaction')


plt.tight_layout()

plt.show()
