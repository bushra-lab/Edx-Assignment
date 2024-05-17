#defile file path
file_path="budget_data.csv"

# define a function that read file
def read_csv_count_months(file_path):

#define variables
    total_months = 0
    added_Dates=set()
    data=[]
    change_new=[]
    change_values=[]
    previous_money=None
    total_amount=0
    with open(file_path, 'r') as file:          #deal headers of csv_file
        next(file)               #read lines in csv_file
        for line in file:           # Split the line into fields
            fields = line.strip().split(',')            # read data in file and columns
            data.append(fields)
            Date=fields[0]
            Money=int(fields[1])
            added_Dates.add(Date)
            total_amount += Money # add total_amount

            if previous_money is not None:  # calculate change and store it in a list
                change = Money - previous_money
                change_new.append((Date, change))
                change_values.append(change)
            previous_money = Money

        average_change = sum(change_values) / len(change_values) if change_values else 0   # write formula for average change, increase and decrease in profit 
        Increase_in_profit=max(change_new, key=lambda x:x[1])
        Decrease_in_profit=min(change_new, key=lambda x:x[1])
        
    total_months =len(added_Dates)
    return data, total_months, total_amount, change_new, Increase_in_profit, Decrease_in_profit, average_change # return data

#def average(total_months, total_amount):
    if total_months==0:
        return 0
    mean = (total_amount)/(total_months)
    return mean
#call function
data, total_months, total_amount, change_new, Increase_in_profit, Decrease_in_profit, average_change = read_csv_count_months(file_path)

#mean =average(total_months, total_amount)

# print all commands
print("Financial Analysis")
print("------------------------")
print(f"Total months: {total_months}")
print(f" Total :  ${total_amount}")

print(f"Average Changes:, {average_change:.2f}")

print(f"Greatest Increase in Profits:, {Increase_in_profit[0]},$({Increase_in_profit[1]})")
print(f"greatest Decrease in Profits:, {Decrease_in_profit[0]}, $({Decrease_in_profit[1]})")

# write data on external file
write_file= "Result.txt"
with open(write_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("------------------------\n")
    file.write("Total months: {total_months}" +"\n")
    file.write(f" Total :  ${total_amount}" +"\n")
    file.write(f"Average Changes:, {average_change:.2f}"+ "\n")
    file.write(f"Greatest Increase in Profits:, {Increase_in_profit[0]},$({Increase_in_profit[1]})"+ "\n")
    file.write(f"greatest Decrease in Profits:, {Decrease_in_profit[0]}, $({Decrease_in_profit[1]})"+"\n")


