"""
Test Cases
"""
#import functions
from main import polar_stats, polar_visualization
import polars as pl

#define test function
def test_sum_stats():
    #read dataset
    cereal = pl.read_csv("cereal.csv",separator = ';')
    summary = polar_stats(cereal)
    assert cereal['calories'].mean() == summary["calories"][2], "Mean test failed"
    assert cereal['protein'].median() == summary['protein'][6], "Median test failed"
    assert cereal['rating'].min() == summary['rating'][4], "Standard deviation test failed"
    print("All Test passed!")

#test
if __name__ == "__main__":
    test_sum_stats()
