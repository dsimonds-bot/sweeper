# Package Import
import pandas as pd
import seaborn as sns
import main

# Load data
df = sns.load_dataset('titanic')

# Use package
main.assets_build(df)