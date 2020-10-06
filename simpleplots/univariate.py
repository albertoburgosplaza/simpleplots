import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_count(data: pd.Series, axis):
    sns.countplot(y=data, ax=axis)


def plot_hist(data: pd.Series, axis):
    sns.histplot(x=data, ax=axis)


def plot_box(data: pd.Series, axis):
    sns.boxplot(x=data, ax=axis)
