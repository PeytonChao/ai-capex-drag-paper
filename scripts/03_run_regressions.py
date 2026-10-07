import pandas as pd
from linearmodels.panel import PanelOLS

# Load clean panel dataset
df = pd.read_csv("data/panel_dataset_clean.csv")

# Ensure Quarter is formatted properly
df['Quarter'] = pd.to_datetime(df['Quarter'])

# Drop rows with missing values in key regression variables
regression_vars = ['OpMargin', 'CapEx_Ratio', 'CapEx_x_Software', 'RD_Ratio', 'Log_Assets', 'Leverage']
df = df.dropna(subset=regression_vars)

# Set panel index
df = df.set_index(['Ticker', 'Quarter'])

# Assign dependent and independent variables
dependent = df['OpMargin']
exog_vars = df[['CapEx_Ratio', 'CapEx_x_Software', 'RD_Ratio', 'Log_Assets', 'Leverage']]

# Run Firm Fixed Effects Model (Absorbs static firm characteristics)
model_fe = PanelOLS(
    dependent, 
    exog_vars, 
    entity_effects=True, 
    time_effects=False, 
    drop_absorbed=True
)

# Fit model with heteroskedasticity-robust standard errors
results_fe = model_fe.fit(cov_type='robust')

# Output results to console and text file
print(results_fe)

with open("outputs/regression_results.txt", "w") as f:
    f.write(str(results_fe))