# Package Import
import main
import seaborn as sns
import time

# Build fake data
df = sns.load_dataset(name = 'titanic')

# Build timing container
timing_container = {}

# Building the testing function
def speed_test(dataframe):
    
    """
    This function takes a dataframe as an argument, and times how long
    each approach for main takes. Then, it appends those results into a tuple, which
    has the first position as the non-direct and the second as the direct. 
    
    Parameters:
    ----------
    dataframe: pd.DataFrame
        The dataframe to use as a testing sample
        
    Returns:
    -------
    timing_results: tuple
        The results of the tests. The first position is nondirect,
        the second position is direct. 
    """
    
    # Build timer for nondirect approach
    nd_start = time.time()
    main.assets_build(dataframe)
    nd_end = time.time()
    
    # Build the timer for direct approach
    d_start = time.time()
    main.direct_assets_build(dataframe)
    d_end = time.time()
    
    # Build results
    timing_results = [nd_end - nd_start, d_end - d_start]
    
    return timing_results

# Running the testing function 100 times
non_direct_counter = 0
direct_counter = 0

for i in range(0,50):
    
    # Execute race
    loop_iteration_result = speed_test(df)
    
    # Add race to test_loops
    non_direct_counter += loop_iteration_result[0]
    direct_counter += loop_iteration_result[1]
    
print(
    f'The average for non_direct is: {round(non_direct_counter/100, 5)}',
    f'The average for direct is: {round(direct_counter/100, 5)}'
)