import pandas as pd

data = {'Name': ['John', 'Mary', 'David', 'John', 'Mary', 'David'], 
        'Age': [25, 31, 42, 25, 31, 42], 
        'City': ['New York', 'Chicago', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles']}

df = pd.DataFrame(data)

# Select only the numeric columns
grouped_df = df.select_dtypes(include=['int64', 'float64']).groupby(df['Name']).mean()
print(grouped_df)