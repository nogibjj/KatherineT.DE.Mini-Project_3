"""
Main function goes here
"""

#import polars and pyplot
import polars as pl
import matplotlib.pyplot as plt

#read dataset
cereal = pl.read_csv("cereal.csv",separator = ';')

#define summary statistics function
def polar_stats(data):
    return data.describe()
 
#define visualization function
def polar_visualization(data):
    plt.hist(data["calories"], bins=10, color="purple")
    plt.xlabel("Calories")
    plt.ylabel("Frequency")
    plt.title("Cereal Calories Histogram")
    plt.show()
    plt.savefig("cereal.png")
    return

def generate_markdown(data):
    """generate an md file with outputs"""
    markdown_table = polar_stats(data)
    markdown_table = str(markdown_table)

    # Write the markdown table to a file
    with open("output.md", "w", encoding="utf-8") as file:
        file.write("Summary:\n")
        file.write(markdown_table)
        file.write("\n\n")  # Add a new line
        file.write("![cereal](cereal.png)\n")
