#dependencies
import csv 



#files to load and output
file_to_load = os.path.join(".", "Resources", "budget_data.csv")
file_to_output = os.path.join(".", "Analysis", "budget_analysis.txt")



#Parameters
total_months = 0
total_net = 0
net_change_list = []
month_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]



#Read file and puts into a list
with open(file_to_load) as financial_analysis:
    reader = csv.reader(financial_analysis)

#read header and print header row
    header = next(reader)
    
    first_row = next(reader)
    
    total_net += int(first_row[1])
    previous_net = int(first_row[1])
    
      
    
#read each row of data after header and track total months and total
    for row in reader:
        
        
        total_months+= 1
        total_net += int(row[1])
        

        
        #track the net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
    
        
        #calculate greatest increase
        if(net_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
          
        #calculate greatest decrease
        if(net_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
            
        
 
#gets the average change     
net_average_change = sum(net_change_list)/len(net_change_list)


#printing the output
output = (
    f" Finacial Analysis\n"
    f"-----------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_average_change:.2f}\n"
    f"Greatest Increase in Profits:{greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits:{greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(output)
