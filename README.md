# Election_Analysis

## Project Overview
A Colorado Board of Elections employee, Tom, has given me the following tasks to complete the election audit of a recent local congressional election.

1. Total number of votes cast
1. Total number of votes each candidate received
1. Total number of votes for each county and the percentage total
1. The largest county turnout
1. Percentage of votes each candidate won
1. The winner of the election based on popular vote

### Resources
- Data Sources: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.46.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election
- The cadididates were:
	- Charles Casper Stockham
	- Diana DeGette
	- Raymon Anthony Doane
- The county results were:
	- Jefferson county received 10.5% of the vote and 38,855 number of votes
	- Denver county received 82.8% of the vote and 306,055 number of votes
	- Arapahoe county received 6.7% of the vote and 24,801 number of votes
- The Largest county Turnout:
	- Denver county has the largest turnout with 82.8% of the vote and 306,055 number of votes.
- The candidate results were:
	- Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes
	- Diana DeGettereceived 73.8% of the vote and 272,892 number of votes
	- Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes
- The Winner of the election was:
	- Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
	
## Challenge Summary
This program was written strictly for election held at the county level. However, with minor modifictations, this program can be used for any elections. In our Python code file [PyPoll_Challenge](PyPoll_Challenge.py.py), make the following 2 changes in order to run our program for any types of elections:
-On line 89, change the following line of code to your choice of election:

    f"County Votes:\n")
    
-On line 116, change the following line of code to your choice of election:

    f"Largest County Turnout: {winning_county}\n"
	
Once the above 2 changes are made, this Python program can be run for any types of elections.
