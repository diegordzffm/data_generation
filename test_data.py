import pandas as pd

# Create a DataFrame with test data
data = {
    "Financial.Date of the default status of the Instrument CICR": ["01/23", "02/24", "12/24"],
    "Header.Reference period": ["12/22", "01/24", "11/24"]
}


# Create a DataFrame with test data that violates the rule
data2 = {
    "Instrument. Anticipated redemption date": ["01/23", "02/24", "12/24", "NotApplicable"],
    "Financial.Default Status": ["In default", "Not in default", "In default", "Not in default"],
    "Financial.Exigibility status": ["Exigible", "Not exigible", "Required", "NotRequired"]
}

# Creating the DataFrame
df2 = pd.DataFrame(data2)

# Displaying the DataFrame
print(df2)

# Creating the DataFrame
'''df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)'''
