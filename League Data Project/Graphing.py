import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('MasterData.csv')

# Set the x values
#x_values = [50, 100, 150, 250]

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Extract the name and data for the current row
    name = row[0]
    y_values = row[1:]

    # Convert the y values to numbers
    y_values = [float(y) for y in y_values if y != '0' and y>0]

    # Only plot the graph if the lengths of x and y are equal

    # Plot the y values against the x values as a line graph
    plt.plot(y_values)

    # Add a title and axis labels
    plt.title(name)
    plt.xlabel('Games Played')
    plt.ylabel('Winrate')

    # Save the figure to a file with the name from the first column
    plt.savefig(f'{name}.png')

    # Clear the figure for the next iteration
    plt.clf()
