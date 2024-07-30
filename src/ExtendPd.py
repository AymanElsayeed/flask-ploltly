"""
Extend pandas functionality within given CSV file
"""
import datetime
import numpy as np
import pandas as pd


@pd.api.extensions.register_dataframe_accessor("Ayman")
class AymanDataframeAccessor:
    """
    Extensions class for pandas data frame object
    :examples
    ---------

    """
    def __init__(self, pandas_obj):
        """
        Constructor method.
        :param pandas_obj:
        """
        self._df: pd.DataFrame = pandas_obj

        self._exclude_1 = [np.float_, np.int_, datetime.datetime]

    def unique_subgroup(self) -> dict:
        """
        the unique values of each categorical columns
        :return: dict
        """
        temp = self._df.select_dtypes(exclude=self._exclude_1)
        sub_group = temp.apply(lambda x: x.unique().tolist()).to_dict()
        return sub_group
