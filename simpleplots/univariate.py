import pandas as pd
import seaborn as sns


def plot_count(data: pd.Series, axis):
    sns.countplot(y=data, ax=axis)


def plot_hist(data: pd.Series, scale: bool, axis):
    sns.histplot(x=data, ax=axis, log_scale=scale)


def plot_box(data: pd.Series, axis):
    sns.boxplot(x=data, ax=axis)