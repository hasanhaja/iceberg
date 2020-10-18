"""
TODO Read data as a matrix (pandas dataframe)
    TODO Fix NaN values since they don't exist in the original data. Update file with full data
TODO Extract years, months and port `annual_op.m` function
TODO Calculate averages
TODO Plot averages
TODO Calculate xcorr and autocorr
TODO Please explore the potential to use all inputs to represent the output. The selection of model and method is open.
TODO Work on relationship between the inputs and the output including correlation and modelling.
TODO generate figures and tables to justify findings
"""
import pandas as pd
import numpy as np
# from os.path import join, abspath


def read_data(path):
    return pd.read_csv(path)


def get_col_from_data(data, col):
    """
    This function returns all the rows for the selected column and raises a ValueError if the column requested does not exist in the Dataframe.

    For example:
        These are the available columns for the Greenland data: [' Ice Year', 'Month', 'SMB', 'NAO', 'LSST', 'I48N'] and it is case sensitive.

    """
    cols = list(data.columns)
    if col not in cols:
        raise ValueError(
            f"Column does not exist in the Dataframe. Use one of the following:\n{cols}")

    return data[col]


def annual_op(data, option):
    if len(data) % 12 ~ = 0:
        raise ValueError("Data is not divisible by 12.")
    
    # Default function that is a pass through.
    operation = lambda x: x

    if option == "mean":
        operation = lambda x: np.mean(x)
    elif option == "sum":
        operation = lambda x: 


def main():
    # data = join("..", "data", "Greenland_full_monthly 1901-2018.xlsx")
    data = "../data/Greenland_full_monthly 1901-2018.csv"
    data = read_data(data)

    smb = get_col_from_data(data, "SMB")
    nao = get_col_from_data(data, "NAO")
    lsst = get_col_from_data(data, "LSST")
    i48n = get_col_from_data(data, "I48N")

    print(i48n)


if __name__ == "__main__":
    main()
