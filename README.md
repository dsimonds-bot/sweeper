# sweeper
Project sweeper takes its namesake from the League of Legends Item, the oracle lens. This searches into areas where the player cannot see, identifying traps or things to look out for. 
 
In a way, I hope this project can help acheive the same by automating most of EDA. By simply passing in a dataframe, the user recieves:

## High Level dataframe statistics
Shape, missing values, datatypes, and more.

## Numeric column report
Each numerical feature will have an auto-generated page dedicated to it alone, containing histograms, boxplots, descriptive statistics, and a brief write up. This should help the user identify potential skewed inputs, varying scale, etc. 

## Categorical feature report
sweeper will automatically create a grid of bar charts for the number of occurences for each distinct value of a categorical column. If you have 3, if you have 500, sweeper will find the optimal layout for your report.

## Demo
![image](https://user-images.githubusercontent.com/57107058/230260485-ecba1c91-5f2a-45f8-a749-ea5e3b57bf92.png)
![image](https://user-images.githubusercontent.com/57107058/230260556-709f8302-bc1e-4273-8e22-2ed67b00c5b4.png)
