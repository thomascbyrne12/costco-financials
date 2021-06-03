# Imports dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Imports Resource csv files as DataFrames
cash_flow = pd.read_csv('Resources/cash_flow.csv', index_col = 'Value')
balance_sheet = pd.read_csv('Resources/balance_sheet.csv', index_col = 'Value')
profit_loss = pd.read_csv('Resources/profit_loss.csv', index_col = 'Value')

# Calculates Working Capital Ratio
total_ca = balance_sheet.loc['Total Current Assets'].astype(int)
total_cl = balance_sheet.loc['Total Current Liabilities'].astype(int)

working_capital = total_ca / total_cl

# Calculates Quick Ratio
inventories = balance_sheet.loc['Inventories'].astype(int)

quick_ratio = (total_ca - inventories) / total_cl

# Calculates Debt to Equity Ratio
# Replaces null values with zeroes
balance_sheet = balance_sheet.replace(np.nan, 0)

short_debt = balance_sheet.loc['Short Term Debt'].astype(int)
long_debt = balance_sheet.loc['Long Term Debt'].astype(int)
equity = balance_sheet.loc['Total Equity'].astype(int)

debt_to_equity = (short_debt + long_debt) / equity

# Calculates Earnings Per Share
profit_eps = profit_loss.loc['Net Income Available to Common Shareholders'].astype(int)

# Shares taken from seperate data source, outstanding shares for end of year
years = ('2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019')
shares = pd.Series((432333947, 433365150, 432424379, 436922037, 437762068, 437406636, 437126569,\
                    436989606, 438208376, 439656950), years)


eps = profit_eps / shares

# Adjustment made since shares data is not rounded
eps = eps * 1000000

# Calculates Price to Earnings Ratio

# Yearly Average Stock Price also taken from seperate data set
years = ('2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019')
yavg_price = pd.Series((60.67, 78.74, 92.06, 111.08, 121.58, 147.84, 154.35, 167.41, 208.81, 262.62), years)

p_to_e = yavg_price / eps

# Creates a DataFrame to store the ratios
temp = pd.DataFrame([working_capital, quick_ratio, debt_to_equity, eps, p_to_e],\
                    index = ['Working Capital', 'Quick Ratio', 'Debt to Equity', 'EPS', 'Price to Earnings'])
ratios_df = temp.transpose()

# Plots and saves EPS per Year data
ratios_df['EPS'].plot(color = 'cyan', linestyle = 'dashed')
plt.title('EPS per Year')
plt.xlabel('Year')
plt.ylabel('EPS')
plt.savefig('EPS per Year.png')

# Plots and saves Working Capital Ratio per Year data
ratios_df['Working Capital'].plot(color = 'orange', linestyle='dotted')
plt.title('Working Capital Ratio per Year')
plt.xlabel('Year')
plt.ylabel('Working Capital Ratio')
plt.savefig('Working Capital Ratio per Year.png')

# Plots and saves Quick Ratio per Year data
ratios_df['Quick Ratio'].plot(color = 'magenta', linestyle = '-.')
plt.title('Quick Ratio per Year')
plt.xlabel('Year')
plt.ylabel('Quick Ratio')
plt.savefig('Quick Ratio per Year')

# Plots and saves Debt to Equity Ratio per Year data
ratios_df['Debt to Equity'].plot(color = 'green', linestyle = ':')
plt.title('Debt to Equity Ratio per Year')
plt.xlabel('Year')
plt.ylabel('Debt to Equity Ratio')
plt.savefig('Debt to Equity Ratio per Year')

# Plots and saves Price to Earnings Ratio per Year data
ratios_df['Price to Earnings'].plot(color = 'yellow', linestyle = 'solid')
plt.title('Price to Earnings Ratio per Year')
plt.xlabel('Year')
plt.ylabel('Price to Earnings Ratio')
plt.savefig('Price to Earnings Ratio per Year.png')
