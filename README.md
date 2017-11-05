# Interview-Assignment

There are three folders, one folder contains only one .py file and two other folders contain two files each, one is .py file and another is .txt file, 
three folders are, 'assignment1' which contains the first assignment, 'assignment2' the second one and 'assignment3' the third and last one.



For the first two assignments, I downloaded the csv manually from url (two csv files are IN.csv and IN2.csv, IN.csv is the original one) and made a few changes in the 
file before using it (IN2.csv is the file with changes), they are:

1. Most of the cells of 'accuracy' attribute are empty, in order to import data smoothly into the database I have filled all the blank cells with 0.

2. All the cells of attribute 'key' were prefixed with IN/, I have removed it for the same reason as above.

3. I have changed the entry of cell number 3883 of attribute 'place_name', as 'text' data type in PostgreSQL was not accepting that entry.



Although I have been able to finish all the final objectives given to me, however there are things which I have not been successful in implementing :

1. In assignment 3, I was not able to load the boundaries latitude and longitude (geometry -> coordinates) into postgresql in a new table (I have not used SQLAlchemy
as I was not sure if I was allowed to use it, instead I have used psycopg2 in assignments).

2. In assignment 1, I have checked if a pin already exists but I was not clear what you meant by "or if there are existing latitude+longitude THAT ARE CLOSE ENOUGH 
TO BE THE SAME (dont assume that they will exactly be the same.)" because csv file already has a lot of pins with exactly same longitude and latitude.

3. I was not able to write testcases (using test frameworks) for any of the assignments as I have never used them before, I tried to understand them and was able to 
for trivial programs, but not in the case of flask applications. (I have shown some results for second and third assignments in the .txt file that can be found in 
respective folders, all the results are reproducible) 
