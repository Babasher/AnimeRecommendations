# AnimeRecommendations
Program that uses the Jikan API to pull the top 'upcoming' anime and their genres. 
Compares the upcoming anime genres with previously watched anime genres to determine if 
the upcoming anime should be recommended.

## Installation
https://jikan.moe/
```bash
pip install jikanpy
```

## Disclaimer
The program takes a few minutes to execute (2 - 3 minutes max). 
Do not terminate and run multiple times.
This could result in getting IP banned from MAL or being blocked from Jikan API services. 

***To Do:***
* Read user information from an excel file. User information is previously watched anime with genres.
* Store API requests into a file - reduces program run time and limits unecessary requests.
* Compare two data sets, create a new data set with appropriate recommendations. 


