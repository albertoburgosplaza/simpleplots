import matplotlib.pyplot as plt
import pandas as pd
from pandas.api.types import (
    is_object_dtype,
    is_bool_dtype,
    is_categorical_dtype,
    is_numeric_dtype,
)
from simpleplots.univariate import plot_count, plot_hist, plot_box


def plot(
    data: pd.DataFrame,
    attribute: [str, list],
    title: str = None,
    size: tuple = (5, 3),
    log_scale: bool = False,
    categorify: bool = True,
    max_categories: int = 10,
):
    # Make first a copy of data
    data = data.copy()

    # Check if it's an univariate plot
    if isinstance(attribute, str):
        if title is None:
            title = f"{attribute}"

        if categorify & (len(data[attribute].unique()) <= max_categories):
            data[attribute] = data[attribute].astype("category")

        if (
            is_object_dtype(data[attribute].dtype)
            | is_categorical_dtype(data[attribute].dtype)
            | is_bool_dtype(data[attribute].dtype)
        ):
            fig, ax = plt.subplots(1, 1, figsize=size)
            fig.suptitle(title)
            plot_count(data[attribute], axis=ax)
            fig.show()
        elif is_numeric_dtype(data[attribute].dtype):
            fig, ax = plt.subplots(2, 1, figsize=size)
            fig.suptitle(title)
            plot_hist(data[attribute], axis=ax[0])
            ax[0].set_xlabel(None)
            plot_box(data[attribute], axis=ax[1])
            if log_scale:
                ax[0].set(xscale="log")
                ax[1].set(xscale="log")
            fig.show()
    elif isinstance(attribute, list):
        print("Multivariate plot")
