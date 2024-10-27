import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    s, i, t1, t2, t3 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    
    x = np.linspace(1880, 2050, 171)
    plt.plot(x, s*x+i, color='k', linestyle='--')

    # Create second line of best fit
    x2 = np.linspace(2000, 2050, 51)
    s2, i2, t1, t2, t3 = linregress(x=df[df['Year']>=2000]['Year'], y=df[df['Year']>=2000]['CSIRO Adjusted Sea Level'])

    plt.plot(x2, s2*x2+i2, color='r', linestyle='--')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()