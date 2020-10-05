import matplotlib.pyplot as plt
import pandas as pd
from pandas.api.types import (
    is_object_dtype,
    is_bool_dtype,
    is_categorical_dtype,
    is_numeric_dtype,
)
from simpleplots.univariate import plot_count, plot_hist, plot_box


def plot(data: pd.DataFrame, attribute: [str, list], **kwargs):
    # Check if it's an univariate plot
    if isinstance(attribute, str):
        if is_object_dtype(data[attribute].dtype):
            plot_count(data[attribute], **kwargs)
        elif is_categorical_dtype(data[attribute].dtype):
            plot_count(data[attribute], **kwargs)
        elif is_bool_dtype(data[attribute].dtype):
            plot_count(data[attribute], **kwargs)
        elif is_numeric_dtype(data[attribute].dtype):
            plot_hist(data[attribute], **kwargs)
    elif isinstance(attribute, list):
        print("Multivariate plot")
