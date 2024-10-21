import pandas as pd

try:
    # Read the CSV file
    df = pd.read_csv('csv.txt')
    
    # Print the first few rows of the DataFrame
    print(df.head())
except FileNotFoundError:
    print("Error: The file 'data.csv' was not found. Please check the file path.")
except pd.errors.EmptyDataError:
    print("Error: The file 'data.csv' is empty. Please check the file content.")
except pd.errors.ParserError:
    print("Error: The file 'data.csv' could not be parsed. Please check the file format.")
except UnicodeDecodeError:
    print("Error: The file 'data.csv' could not be decoded. Please check the file encoding.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")