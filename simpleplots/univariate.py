import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_object(data: pd.Series, **kwargs):
    plt.figure(**kwargs)
    plt.title(f"{data.name} count")
    sns.countplot(x=data)
    plt.xlabel(None)
    plt.show()
