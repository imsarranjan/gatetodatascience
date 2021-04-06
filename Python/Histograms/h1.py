import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

marks = [20,35,45,65,32,54,85,65,90,84,44,62]
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(marks, bins=bins, edgecolor='black', log=True)

array_mark = np.array(marks)
median_mark = np.median(array_mark)
color = 'red'

plt.axvline(median_mark, color=color, label='Marks Median', linewidth=2)

plt.legend()

plt.title('Marks of Students')
plt.xlabel('Marks')
plt.ylabel('Total Students')

plt.tight_layout()

plt.show()
