# sweeper

:paintbrush: [Mockups](https://github.com/dsimonds-bot/sweeper/discussions/2) </br>
:teacher: [Demo](https://github.com/dsimonds-bot/sweeper/blob/main/src/scratch.ipynb) </br>
:email: davesimonds6@gmail.com </br>

Project sweeper takes its namesake from the League of Legends Item, the oracle lens. This searches into areas where the player cannot see, identifying traps or things to look out for. 
 
In a way, I hope this project can help acheive the same by automating most of EDA. By simply passing in a dataframe, the user recieves:

## High Level dataframe statistics 
:black_medium_square: Shape, missing values, datatypes, and more.

## Numeric column report
:black_medium_square: Each numerical feature will have an auto-generated page dedicated to it alone, containing histograms, boxplots, descriptive statistics, and a brief write up. This should help the user identify potential skewed inputs, varying scale, etc. 

## Categorical feature report
:black_medium_square: sweeper will automatically create a grid of bar charts for the number of occurences for each distinct value of a categorical column. If you have 3, if you have 500, sweeper will find the optimal layout for your report.

## Demo
![image](https://user-images.githubusercontent.com/57107058/230261493-dbb6a40a-c462-49d4-9ff4-99df2b1cfe92.png)
