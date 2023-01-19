import py_visuo.utils
import py_visuo.custom_colors
import py_visuo.visualise
import numpy as np
import seaborn as sns 
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

fig, ax = plt.subplots(figsize=(5, 5))
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)
ax.plot(t, s)
py_visuo.visualise.set_plot_features(fig, ax, show_legend=False)


x = [1, 2, 3, 4, 5]
y1 = [1, 1, 2, 3, 5]
y2 = [0, 4, 2, 6, 8]
y3 = [1, 3, 5, 7, 9]
fibonacci_df =  pd.DataFrame({'x': x, 'Fibonacci':y1, 'Evens':y2, 'Odds':y3})
fig, ax = plt.subplots(figsize=(5,5))
py_visuo.visualise.create_stack_plot(fig, ax, fibonacci_df, 'x', ['Fibonacci', 'Evens', 'Odds'],  filter_size = 2)
py_visuo.visualise.set_plot_features(fig, ax, show_legend=False)


glue = sns.load_dataset("glue").pivot("Model", "Task", "Score")
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
sns.heatmap(glue, ax=ax[0], cmap=py_visuo.utils.get_continuous_cmap(py_visuo.custom_colors.blue_heatmap_light))
sns.heatmap(glue, ax=ax[1], cmap=py_visuo.utils.get_continuous_cmap(py_visuo.custom_colors.blue_heatmap_dark))

plt.show()
print('test')







