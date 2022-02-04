# map-reduce-venkatesh
This is to practice the map and reduce in python.

## Data Description:
- This DataSet contains details of the NBA players age, games played, no of wins, lost, minutes played, points from the different teams in the year 2020-21 Regular Season.
- The Dataset is a free source from ***[Kaggle](https://www.kaggle.com)***

## Study:
- From this Dataset, I want to find out the total number of wins for different team that consists of players those played in the NBA game for the year 2020-21.

## Execution:
- A ***Mapper File*** extracts the team from each row in the dataset, which is used as a ***Key*** and wins for the  ***Values***  .This output is given as input to the ***Sorter File*** which in sort the values and then the ouput of sorter file is given to ***reducer File*** which reduces and then gives the output to ***output.txt*** .

## Powershell Command:
- ***cat 202021-reg-tra-player.csv | python 03mapper.py | python 03sorter.py | python 03reducer.py > output.txt*** .

## Summary:
- From the output file we can see that the team UTA has highest number of wins 610 and the lowest wins as the HOU team 184. where as the MEM and GSW has the equal number of wins, in addition to that BOS, CHA and IND are almost having equal numbner of wins.

![image](https://user-images.githubusercontent.com/77640153/152580486-3f85d467-9850-4ee5-98d9-090e345a9cd3.png)

