import numpy as np
import pandas as pd

def compute_correlation(df, column1, column2):
    # Calculate the correlation coefficient between two columns
    matrix = np.corrcoef(df[column1], df[column2])
    correlation = matrix[0, 1]
    
    return correlation

if __name__ == "__main__":
    df = pd.read_csv('data/cleaned_data.csv')
    
    # Compute correlations
    gdp_happiness_corr = compute_correlation(df, 'GDP per capita', 'Happiness Score')
    print(f"Correlation between GDP per capita and Happiness Score: {gdp_happiness_corr}")
    
    suicide_happiness_corr = compute_correlation(df, 'Crude Suicide Rates (Both Genders)', 'Happiness Score')
    print(f"Correlation between Suicide Rates and Happiness Score: {suicide_happiness_corr}")
    
    disease_gdp_corr = compute_correlation(df, 'Probability (%) of dying between age 30 and 70 From Disease(Both Sexes)', 'GDP per capita')
    print(f"Correlation between Disease-related Mortality and GDP per capita: {disease_gdp_corr}")
    
    disease_happiness_corr = compute_correlation(df, 'Probability (%) of dying between age 30 and 70 From Disease(Both Sexes)', 'Happiness Score')
    print(f"Correlation between Disease-related Mortality and Happiness Score: {disease_happiness_corr}")
