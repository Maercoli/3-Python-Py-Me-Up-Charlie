# Modules
import os
import csv

# Set path for file
filepath = os.path.join("PyBank","csv.file","budget_data.csv")

# Set variables
total_months = 0
total_profit_losses = 0
previous_net = 0
change = 0
total_month_change = 0
avg_month_change = 0
great_inc = 0
great_inc_month = ""
great_dec = 0
great_dec_mont = ""

# open and read csv file
with open (filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # read the header 
    header = next(csvreader)
    
    # read each row of data after the header
    for row in csvreader:
        # count the total number of months
        total_months = total_months + 1
        
        #calculate total profit/losses
        total_profit_losses = total_profit_losses + int(row[1])

        # calculate de change in profits
        if total_months > 1:
            change = int(row[1]) - previous_net 

        total_month_change =  total_month_change + change

        #reassign profit/losses value for previous month
        previous_net = int(row[1])       

        # find greatest increase and corresponding month 
        if change > great_inc:
            great_inc = change
            great_inc_month = row[0]

        if change < great_dec:
            great_dec = change
            great_dec_mont = row[0]

# find average change between months
avg_month_change = total_month_change / (total_months -1)

# print to the terminal
print(f'Financial Analysis')
print('-------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit_losses}')
print('Average Change: {:.2f}'.format(avg_month_change))
print(f'Greatest Increase in Profit:{great_inc_month} {great_inc}')
print(f'Greatest Decrease in Profit:{great_dec_mont} {great_dec}')

# write to text file
f = open("PyBank/analysis/analysis.txt",'w')
f.write(f'Financial Analysis\n')
f.write('------------------------\n')
f.write(f'Total Months:{total_months}\n')
f.write(f'Total:${total_profit_losses}\n')
f.write('Average Change: {:.2f}\n'.format(avg_month_change))
f.write(f'Greatest Increase in Profit:{great_inc_month} {great_inc}\n')
f.write(f'Greatest Decrease in Profit:{great_dec_mont} {great_dec}\n')
f.close()
