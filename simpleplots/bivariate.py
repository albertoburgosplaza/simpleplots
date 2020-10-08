import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def plot_scatter(data: pd.DataFrame, x: str, y: str, color: str, axis):
    if color is not None:
        sns.scatterplot(x=x, y=y, data=data, hue=color, ax=axis)
        plt.legend(bbox_to_anchor=(1.01, 1), borderaxespad=0)
    else:
        sns.scatterplot(x=x, y=y, data=data, ax=axis)
