# filtering a data frame
import pandas as pd

data = {'Name': ['John', 'Mary', 'David'], 
        'Age': [25, 31, 42], 
        'City': ['New York', 'Chicago', 'Los Angeles']}

df = pd.DataFrame(data)

filtered_df = df[df['Age'] > 30]
print(filtered_df)