import csv
import os

Canidate_list =[]  #create list to store unique canidates
vote_count =[]

CSV_PATH = os.path.join("Resources_Poll\election_data.csv") # Set Path
os.chdir(os.path.dirname(os.path.realpath(__file__))) # adjust path
with open(CSV_PATH) as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # skip header
        poll_data = list(csvreader)   

for i in poll_data:    # read data and add unique canidates to list
    canidate = i[2]
    if canidate not in Canidate_list:
       Canidate_list.append(canidate)
for i in poll_data: # make a list of only the vote
     canidate = i[2]
     vote_count.append(canidate)
total_votes = len(poll_data) # count total votes     
canidate0 = Canidate_list[0] #define canidate names
canidate1= Canidate_list[1]
canidate2= Canidate_list[2]

total0 = vote_count.count(canidate0)    # count individual canidate votes
total1 = vote_count.count(canidate1)
total2 = vote_count.count(canidate2)

if total0 > total1 and  total0 > total2: # find wining name
    winner = canidate0
if total1 > total0 and  total1 > total2:
    winner = canidate1    
if total2> total1 and  total2 > total0:
    winner = canidate2   
percent0 = round((int(total0) / int(total_votes) * 100),3) # calculate percent of votes
percent1 = round((int(total1) / int(total_votes) * 100),3)
percent2 = round((int(total2) / int(total_votes) * 100),3)

print("Election Results" "\n" "-----------------------------------------")             # print in terminal
print("Total Votes   " + str(total_votes) + "\n" "-----------------------------------------")
print(str(canidate0) + ":  " + str(percent0) + "%  " + "(" + str(total0) + ")")
print(str(canidate1) + ":  " + str(percent1) + "%  " + "(" + str(total1) + ")")
print(str(canidate2) + ":  " + str(percent2) + "%  " + "(" + str(total2) + ")" + "\n" + "------------------------------------------------------------")
print("Winner:  " + str(winner) + "\n" + "---------------------------------")

with open("Analysis_Poll\Election_Results.txt", "w") as file:     #print to txt documant in analysis folder
     print("Election Results" "\n" "-----------------------------------------", file=file)             
     print("Total Votes   " + str(total_votes) + "\n" "-----------------------------------------", file=file)
     print(str(canidate0) + ":  " + str(percent0) + "%  " + "(" + str(total0) + ")", file=file)
     print(str(canidate1) + ":  " + str(percent1) + "%  " + "(" + str(total1) + ")", file=file)
     print(str(canidate2) + ":  " + str(percent2) + "%  " + "(" + str(total2) + ")" + "\n" + "------------------------------------------------------------", file=file)
     print("Winner:  " + str(winner) + "\n" + "---------------------------------", file=file)