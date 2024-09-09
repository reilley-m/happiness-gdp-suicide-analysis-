import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def create_bar_graph(df, x, y, xlabel, ylabel, title):
    # Create a bar graph
    fig, ax = plt.subplots()
    df[y] = pd.to_numeric(df[y])
    df_sorted = df.sort_values(by=y, ascending=True)
    
    ax.bar(df_sorted[x], df_sorted[y])
    plt.xticks(rotation=90)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def create_heatmap(df):
    # Create a correlation heatmap
    sns.set_style("white")
    correlation = df.corr()
    
    # Create a mask for the upper triangle
    mask = np.triu(np.ones_like(correlation, dtype=bool))
    
    # Generate the heatmap
    fig, ax = plt.subplots(figsize=(11, 9))
    color = sns.diverging_palette(220, 10, as_cmap=True)
    
    sns.heatmap(correlation, cmap=color, mask=mask, vmax=.5, center=0, square=True, linewidths=.7)
    plt.show()

def plot_regional_maps(merged_data, column, title, colorbar_label):
    # Create a regional map
    fig, ax = plt.subplots(figsize=(12, 8))
    merged_data.plot(column=column, cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8')
    
    # Add titles and labels
    ax.set_title(title)
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    
    # Add colorbar
    sm = plt.cm.ScalarMappable(cmap='YlOrRd')
    sm.set_array(merged_data[column])
    cbar = fig.colorbar(sm, ax=ax, fraction=0.03, pad=0.04)
    cbar.set_label(colorbar_label, rotation=90)
    
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('data/cleaned_data.csv')
    
    # Create a bar graph for regional suicide rates
    create_bar_graph(df, 'Region', 'Crude Suicide Rates (Both Genders)', 'Region', 'Suicide Rates per 100,000', 'Regional Suicide Rates')
    
    # Create a correlation heatmap
    create_heatmap(df)
