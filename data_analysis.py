import pandas as pd
import numpy as np

def calculate_summary_stats(df, group_col):
    # Calculate mean, median, and standard deviation of numeric columns by region
    columns = df.select_dtypes(include=np.number).columns.tolist()
    grouped = df.groupby(group_col)[columns].agg(['mean', 'median', 'std'])
    
    return grouped

def find_outliers(df, column_name, z_threshold=3):
    # Calculate z-scores for the column to find outliers
    z_score = np.abs((df[column_name] - df[column_name].mean()) / df[column_name].std())
    outliers = df[z_score > z_threshold]
    
    if outliers.empty:
        print(f"No outliers found in {column_name}.")
    else:
        return outliers

def find_extremes(df, column, n=3):
    # Find top and bottom 'n' extreme values for the given column
    sorted_df = df.sort_values(by=column)
    lowest_df = sorted_df.head(n)
    highest_df = sorted_df.tail(n)
    
    return pd.concat([lowest_df, highest_df])

if __name__ == "__main__":
    df = pd.read_csv('data/cleaned_data.csv')
    
    # Calculate regional stats
    summary_stats = calculate_summary_stats(df, 'Region')
    print(summary_stats)
    
    # Find outliers for suicide rates
    suicide_outliers = find_outliers(df, 'Crude Suicide Rates (Both Genders)')
    print(suicide_outliers)
    
    # Find countries with extreme happiness scores
    happiness_extremes = find_extremes(df, 'Happiness Score', 3)
    print(happiness_extremes)
