import csv
import os


Total_Profits = int(0)  #set defualt of interger to total profits
Monthly_Change = []     # create a list to add monthly change in profits to

CSV_PATH = os.path.join("Resources_Bank\Budget_data.csv") # Set Path
os.chdir(os.path.dirname(os.path.realpath(__file__))) # adjust path
with open(CSV_PATH) as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # skip header
        profit_data = list(csvreader)   # save all data to profit_data
        change1 = list(profit_data[0])       
        change2 = change1[1]   # set first month to calculate monthly change



total_months = len(profit_data)  # count entries in profit_data to get month count
    

for i in profit_data:  
 Total_Profits = Total_Profits + int(i[1])    # total index 1 of profit data to get total profits
 change1 =  i[1]
 change_m2m = int(change1) - int(change2)        
 Monthly_Change.append(change_m2m)
 change2 = i[1]
del Monthly_Change[0] #delete the 0 to show no change in the first month
Average_change = sum(Monthly_Change) / len(Monthly_Change)



Lowest_Month = min(Monthly_Change, key=float)  # find the greatest decrease in pro
Greatest_Month = max(Monthly_Change, key=float) # find greatest increase in profit

for i in [ i for i,x in enumerate(Monthly_Change) if x == Greatest_Month]: # find greatest increase  month index value in monthly change[]
  G = int(i) + 1  # set index to +1 becuase first month was removed
  Gmonth = profit_data[G][0]  # match month back to monthly_change

for i in [ i for i,x in enumerate(Monthly_Change) if x == Lowest_Month]: # find greatest decrease month index value in monthly change[]
  L= int(i) + 1  # set index to +1 becuase first month was removed
  Lmonth = profit_data[L][0]  # match month back to monthly_change

  Average_change = round(Average_change, 2) # round average Change
                                                                #Print report to terminal
print("Finacial Analysis" "\n" "-----------------------------------------")
print("Total Months:   " + str(total_months))
print("Total: " + '$' + str(Total_Profits))
print("Average Change:   " + '$' + str(Average_change))  
print("Greatest Increase In Profits:   " + str(Gmonth) + '   $' + str(Greatest_Month))   
print("Greatest Decrease In Profits:   " + str(Lmonth) + '   $' + str(Lowest_Month)) 
                                
                                                                            # create and print to file called "Finacial analysis"
with open("Analysis_Bank\Finacial_Analysis.txt", "w") as file:
    print("Finacial Analysis" "\n" "-----------------------------------------", file=file)
    print("Total Months:   " + str(total_months), file=file)
    print("Total: " + '$' + str(Total_Profits),file=file)
    print("Average Change:   " + '$' + str(Average_change),file=file)  
    print("Greatest Increase In Profits:   " + str(Gmonth) + '   $' + str(Greatest_Month), file=file)   
    print("Greatest Decrease In Profits:   " + str(Lmonth) + '   $' + str(Lowest_Month), file=file) 
   


                