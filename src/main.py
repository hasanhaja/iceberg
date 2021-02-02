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

"""
Copied code from Matlab project 

% SUMMARY
% The autocorrelation of nao results in nothing and this suggests that nao
% might be closer to white noise.

data = readmatrix('Greenland_full_monthly 1901-2018.xlsx');

% Extract all the individual years
years_raw = data(1:end, 1);
years = annual_op(years_raw, 'first');
months = 1:length(years_raw);

% Extract all the raw data
smb = data(1:end, 3);
nao = data(1:end, 4);
lsst = data(1:end, 5);
i48n = data(1:end, 6);

% Plot raw data
% The purpose of this was to visualize what the raw data looked like to see
% if anything was being lost in the averages and sum calculation.
figure
plot(months, smb), title('SMB per month'), xlabel('Months (1901-2018)'), ylabel('Surface Mass Balance')
grid on, grid minor

figure
plot(months, nao), title('NAO per month'), xlabel('Months (1901-2018)'), ylabel('North Atlantic Oscillation')
grid on, grid minor

figure
plot(months, lsst), title('LSST per month'), xlabel('Months (1901-2018)'), ylabel('Labrador Sea Surface Temperature')
grid on, grid minor

figure
plot(months, i48n), title('I48N per month'), xlabel('Months (1901-2018)'), ylabel('I48N (number per month)')
grid on, grid minor

% Calculate the annual averages and the sum for L48N
smb_avg = annual_op(smb, 'mean');
nao_avg = annual_op(nao, 'mean');
lsst_avg = annual_op(lsst, 'mean');
i48n_sum = annual_op(i48n, 'sum');

% Plots of calculated data
figure
plot(years, smb_avg), title('Average SMB per year'), xlabel('Year'), ylabel('Average Surface Mass Balance')
grid on, grid minor

figure
plot(years, nao_avg), title('Average NAO per year'), xlabel('Year'), ylabel('Average North Atlantic Oscillation')
grid on, grid minor

figure
plot(years, lsst_avg), title('Average LSST per year'), xlabel('Year'), ylabel('Average Labrador Sea Surface Temperature')
grid on, grid minor

figure
plot(years, i48n_sum), title('Accumulative I48N per year'), xlabel('Year'), ylabel('I48N (number per year)')
grid on, grid minor

% Time varying correlation of each input and I48N
% Windowing is useful to capture time information that is lost in the
% fourier transform. It has no effect on cross correlation.
smb_corr = xcorr(smb, i48n);
nao_corr = xcorr(nao, i48n);
lsst_corr = xcorr(lsst, i48n);

figure, plot(smb_corr)
title('Cross correlation of SMB and I48N')
grid on, grid minor

figure, plot(nao_corr)
title('Cross correlation of NAO and I48N')
grid on, grid minor

figure, plot(lsst_corr)
title('Cross correlation of LSST and I48N')
grid on, grid minor

% XCorrelation of the annual averages with the accumulative iceberg number
smb_avg_corr = xcorr(smb_avg, i48n_sum);
nao_avg_corr = xcorr(nao_avg, i48n_sum);
lsst_avg_corr = xcorr(lsst_avg, i48n_sum);

figure, plot(smb_avg_corr)
title('Cross correlation of Average SMB and Accumulative I48N')
grid on, grid minor

figure, plot(nao_avg_corr)
title('Cross correlation of Average NAO and Accumulative I48N')
grid on, grid minor

figure, plot(lsst_avg_corr)
title('Cross correlation of Average LSST and Accumulative I48N')
grid on, grid minor

% Findings
% Autocorrelation results

nao_auto = xcorr(nao);
nao_avg_auto = xcorr(nao_avg);
% Autocorrelation of Nao and Nao_avg results in nothing. This suggests
% that it is close to white noise.

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
    if len(data) % 12 ~= 0:
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
