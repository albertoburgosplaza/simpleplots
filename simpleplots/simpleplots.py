import numpy as np
import time
import matplotlib.pyplot as plt
import pandas as pd
from pandas.api.types import (
    is_object_dtype,
    is_bool_dtype,
    is_categorical_dtype,
    is_numeric_dtype,
    is_datetime64_any_dtype,
)
from simpleplots.univariate import plot_count, plot_hist, plot_box
from simpleplots.bivariate import plot_scatter


def plot(
    data: pd.DataFrame,
    attributes: list,
    title: str = None,
    size: tuple = (5, 5),
    scale: bool = True,
    scale_threshold: float = 10e2,
    categorify: bool = True,
    max_categories: int = 10,
    color: str = None,
):
    implied_attributes = attributes.copy()
    if color is not None:
        implied_attributes.append(color)
    data = preprocess(data, implied_attributes, categorify, max_categories)

    # Univariate plot
    if len(attributes) == 1:

        if title is None:
            title = f"{attributes[0]}"

        if (
            is_object_dtype(data[attributes[0]].dtype)
            | is_categorical_dtype(data[attributes[0]].dtype)
            | is_bool_dtype(data[attributes[0]].dtype)
        ):
            if len(data[attributes[0]].unique()) <= max_categories:
                fig, ax = plt.subplots(1, 1, figsize=size)
                fig.suptitle(title)
                plot_count(data[attributes[0]], axis=ax)
                fig.show()
            else:
                print("Too many unique values. Change max_categories argument value.")
        elif is_numeric_dtype(data[attributes[0]].dtype):
            if scale & (
                (data[attributes[0]].max() - data[attributes[0]].min())
                < scale_threshold
            ):
                scale = False
            fig, ax = plt.subplots(2, 1, figsize=size)
            fig.suptitle(title)
            plot_hist(data[attributes[0]], scale, axis=ax[0])
            ax[0].set_xlabel(None)
            plot_box(data[attributes[0]], axis=ax[1])
            if scale:
                ax[1].set(xscale="log")
            fig.show()
        elif is_datetime64_any_dtype(data[attributes[0]].dtype):
            fig, ax = plt.subplots(2, 1, figsize=size)
            fig.suptitle(title)
            plot_hist(data[attributes[0]], scale=False, axis=ax[0])
            ax[0].set_xlabel(None)
            temp = data[attributes[0]].astype(np.int64) / 1e9
            plot_box(temp, axis=ax[1])
            ax[1].xaxis.set_major_formatter(convert_to_date_string)
            fig.show()
    else:
        if title is None:
            title = attributes[0]
            for a in attributes[1:]:
                title += " vs " + a

        # Bivariate plot
        if len(attributes) == 2:
            if is_category(data[attributes[0]]) & is_category(data[attributes[1]]):
                print("category vs category")
            elif is_category(data[attributes[0]]) & is_numeric_dtype(
                data[attributes[1]].dtype
            ):
                print("category vs numeric")
            elif is_numeric_dtype(data[attributes[0]].dtype) & is_numeric_dtype(
                data[attributes[1]].dtype
            ):
                fig, ax = plt.subplots(1, 1, figsize=size)
                fig.suptitle(title)
                plot_scatter(data, attributes[0], attributes[1], color, axis=ax)
                fig.show()
            elif is_datetime64_any_dtype(data[attributes[0]].dtype) & is_numeric_dtype(
                data[attributes[1]].dtype
            ):
                fig, ax = plt.subplots(1, 1, figsize=size)
                fig.suptitle(title)
                plot_scatter(data, attributes[0], attributes[1], color, axis=ax)
                fig.show()


def is_category(attribute: pd.Series) -> bool:
    return (
        is_object_dtype(attribute.dtype)
        | is_categorical_dtype(attribute.dtype)
        | is_bool_dtype(attribute.dtype)
    )


def preprocess(
    data: pd.DataFrame, all_attributes: list, categorify, max_categories
) -> pd.DataFrame:
    data = data.copy()
    for a in all_attributes:
        if categorify & (len(data[a].unique()) <= max_categories):
            data[a] = data[a].astype("category")
    return data


@plt.FuncFormatter
def convert_to_date_string(x, pos):
    return time.strftime("%Y", time.localtime(x))
