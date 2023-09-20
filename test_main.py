"""
Test Cases
"""
#import functions
from main import polar_stats,polar_visualization,generate_markdown
import polars as pl

#define test function
def test_sum_stats():
    #read dataset
    cereal = pl.read_csv("cereal.csv",separator = ';')
    summary = polar_stats(cereal)
    polar_visualization(cereal)
    generate_markdown(cereal)
    assert cereal['calories'].mean() == summary["calories"][2]
    assert cereal['protein'].median() == summary['protein'][6]
    assert cereal['rating'].min() == summary['rating'][4]
    print("All Test passed!")

#test
if __name__ == "__main__":
    test_sum_stats()
