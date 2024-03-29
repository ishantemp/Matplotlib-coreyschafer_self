from matplotlib import pyplot as plt 
import numpy as np
## prints style available for plot 
# print(plt.style.available)

## list of default styles available printed from above list
# ['seaborn-talk', '_classic_test', 'seaborn-poster', 'seaborn-dark-palette', 'seaborn-darkgrid', 'fast', 'seaborn', 'ggplot',
#  'seaborn-paper', 'seaborn-whitegrid', 'seaborn-colorblind', 'fivethirtyeight', 'classic', 'seaborn-ticks', 'seaborn-pastel', 
#  'bmh', 'Solarize_Light2', 'seaborn-deep', 'tableau-colorblind10', 'seaborn-bright', 'dark_background', 'seaborn-muted',
#  'seaborn-dark', 'seaborn-notebook', 'grayscale', 'seaborn-white']


plt.style.use("fivethirtyeight")

## hand-drawn like style for plot
# plt.xkcd()


## dev_x and dev_y are grabbed from snippets.py(ishan/codes/corey-schafer/clonned-code_snippets/Python/Matplotlib/01-Introduction)

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(ages_x))  # x_indexes = array([0,1,..,9])
width = 0.25


## For all devlopers

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]


##for plotting graph
# k-- :- Black dashed line
plt.bar(x_indexes + width,dev_y,width=width,color='#444444',label="All Devs")



# Median Python Developer Salaries by Age

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.bar(x_indexes,py_dev_y,width=width,color='red',label="Python")



# Median JavaScript Developer Salaries by Age

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(x_indexes - width,js_dev_y,width=width,label="JavaScript")






## label for X axis
plt.xlabel('Ages')
## label 
plt.ylabel('Median Salary (INR)')
plt.title('Median Salary (INR) by Age')


plt.xticks(ticks=x_indexes,labels=ages_x)

## we have passed label argument to plots so we don't need to pass list here and that is much better way.
plt.legend()

## to bring grid instead of plain background to find exact points sometimes
plt.grid(True)


plt.tight_layout()

# plt.savefig('new_demo.png')

## for showing the plotted graph
plt.show()