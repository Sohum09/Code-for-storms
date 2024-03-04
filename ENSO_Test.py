import pandas as pd
import matplotlib.pyplot as plt

def plot_enso_data(year):
    if year < 1950:
        # Load the 1882-2013 dataset
        df = pd.read_csv('enso_old.csv')
        # Filter the dataset for the given year
        df_year = df[df['year'] == year]
        # Exclude the last row
        df_year = df_year.iloc[:-1]
        # Plotting
        fig, ax = plt.subplots()
        ax.plot(df_year['month'], df_year['ENSO'], marker='o', label='ENSO', color='blue')
        plt.title(f'ENSO Data for {year} (1882-2022)')
        plt.xlabel('Month')
        plt.ylabel('ENSO (°C)')
        plt.grid(True)
    else:
        # Load the 1950-2023 dataset
        df = pd.read_csv('ENSO.csv', parse_dates=['Date'])
        # Filter the dataset for the given year
        df_year = df[df['Year'] == year]
        # Plotting
        fig, ax = plt.subplots()
        ax.plot(df_year['Month'], df_year['ONI'], marker='o', label='ONI', color='orange')
        plt.title(f'ENSO (ONI) Data for {year} (1882-2022)')
        plt.xlabel('Month')
        plt.ylabel('ENSO (ONI) (°C)')
        plt.grid(True)

    # Annotate each point with its exact value
    for i, txt in enumerate(df_year['ENSO' if year < 1950 else 'ONI']):
        plt.annotate(f'{txt:.2f}', (df_year['month'].iloc[i] if year < 1950 else df_year['Month'].iloc[i], txt), textcoords="offset points", xytext=(0, 5), ha='center')

    # Background color based on the sign of the values
    ax.axhspan(0, max(df_year['ENSO' if year < 1950 else 'ONI']), facecolor='red', alpha=0.1)
    ax.axhspan(min(df_year['ENSO' if year < 1950 else 'ONI']), 0, facecolor='blue', alpha=0.1)

    plt.xticks()
    plt.legend()
    plt.tight_layout()
    plt.show()

# Example usage
plot_enso_data(1913)  # Change the year as needed
