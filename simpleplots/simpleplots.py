import pandas as pd
from pandas.api.types import is_object_dtype
from simpleplots.univariate import plot_object


def plot(data: pd.DataFrame, attribute: [str, list], **kwargs):
    # Check if it's an univariate plot
    if isinstance(attribute, str):
        if is_object_dtype(data[attribute].dtype):
            plot_object(data[attribute], **kwargs)
    elif isinstance(attribute, list):
        print("Multivariate plot")
