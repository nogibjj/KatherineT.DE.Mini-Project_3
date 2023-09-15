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
    return

if __name__ == "__main__":
    print(polar_stats(cereal))
    polar_visualization(cereal)