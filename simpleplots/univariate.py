import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_count(data: pd.Series, **kwargs):
    plt.figure(**kwargs)
    plt.title(f"{data.name} count")
    sns.countplot(x=data)
    plt.xlabel(None)
    plt.show()


def plot_hist(data: pd.Series, **kwargs):
    plt.figure(**kwargs)
    plt.title(f"{data.name} histogram")
    sns.histplot(x=data)
    plt.xlabel(None)
    plt.show()


def plot_box(data: pd.Series, **kwargs):
    plt.figure(**kwargs)
    plt.title(f"{data.name} boxplot")
    sns.boxplot(x=data)
    plt.xlabel(None)
    plt.show()
