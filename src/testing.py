# Package Import
import main
import seaborn as sns
import time

# Starting the timer
start = time.time()

# Test code
df = sns.load_dataset('titanic')
main.assets_build(df)

# Finish timer
print(f'Code execution took: {round(time.time() - start,3)}')