import pandas as pd

def load_data():
    # Load the datasets
    happiness_df = pd.read_csv('data/world_happiness.csv')
    suicide_df = pd.read_csv('data/suicide_rates.csv')
    gdp_df = pd.read_csv('data/world_gdp.csv')
    
    return happiness_df, suicide_df, gdp_df

def clean_suicide_data(suicide_df):
    # Rename columns for easier understanding
    suicide_df = suicide_df.rename(columns={
        'Unnamed: 0': 'Country', 
        'Crude suicide rates (per 100 000 population)': 'Crude Suicide Rates (Both Genders)',
        'Crude suicide rates (per 100 000 population).1': 'Crude Suicide Rates (Male)',
        'Crude suicide rates (per 100 000 population).2': 'Crude Suicide Rates (Female)'
    })
    
    # Filter for year 2016
    suicide_df = suicide_df[suicide_df['Year'] == 2016]
    
    return suicide_df

def clean_gdp_data(gdp_df):
    # Rename columns
    gdp_df = gdp_df.rename(columns={'Country Name': 'Country', '2016': 'GDP per capita'})
    
    return gdp_df

def merge_datasets(happiness_df, suicide_df, gdp_df):
    # Merge datasets on 'Country'
    df = pd.merge(happiness_df, suicide_df, on='Country', how='inner')
    df = pd.merge(df, gdp_df, on='Country', how='inner')
    
    # Drop irrelevant columns
    df.drop(['Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 
             'Freedom', 'Trust (Government Corruption)', 'Generosity'], axis=1, inplace=True)
    
    return df

# Function to save the cleaned data
def save_clean_data(df):
    df.to_csv('data/cleaned_data.csv', index=False)

if __name__ == "__main__":
    happiness_df, suicide_df, gdp_df = load_data()
    suicide_df = clean_suicide_data(suicide_df)
    gdp_df = clean_gdp_data(gdp_df)
    df = merge_datasets(happiness_df, suicide_df, gdp_df)
    save_clean_data(df)
