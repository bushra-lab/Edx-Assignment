
# mention file path
file_path = "election_data.csv"

#function to calculate percentage_votes
def percentage_votes(candidate_votes,total_votes):
    percentage_votes={}
    for candidate, votes in candidate_votes.items():
        percentage=(votes/total_votes)*100 # formula to calculate percentage
        percentage_votes[candidate] = (votes,percentage)
    return percentage_votes
#function to read file and votes
def read_csv_count_votes(file_path):
    total_votes = 0 # defining initial parameters
    candidate_votes={}
    data = []
    candidates = set()
    with open('Resources/election_data.csv', 'r') as file:
        for line in file:
            fields = line.strip().split(',')
            data.append(fields)
            candidate=fields[2] # 
            if candidate not in candidate_votes:
                candidate_votes[candidate] = 1 # only incase if any candidate have no votes
            else:
                candidate_votes[candidate] += 1

            total_votes += 1
    return data, total_votes, candidate_votes

#function to calculate percentage
def find_winner(percentage_votes):
    max_percentage = max(percentage_votes.values(), key=lambda x: x[1])[1]
    winners = [candidate for candidate, (_, percentage) in percentage_votes.items() if percentage == max_percentage]   
    return winners



# read function

csv_data, total_votes,candidate_votes = read_csv_count_votes(file_path)
percentage_votes = percentage_votes(candidate_votes, total_votes)

#print("csv_data:", csv_data)
print("Election Results")
print("------------------------")
print("Total  votes:", total_votes)
print("------------------------")

#print( candidate)
for candidate, (votes, percentage) in percentage_votes.items():
    if percentage != 0:
        print(f"{candidate}: {percentage:.3f}% ({votes})" )
print("------------------------")

#read winner function
winners=find_winner(percentage_votes)

print(f"Winner:", winners)
print ("------------------------\n")
# write data on external file
write_file= "Result.txt"
with open(write_file, 'w') as file:
    file.write("Election Results\n")
    file.write("------------------------\n")
    file.write("Total  votes:"+ str(total_votes) +"\n")
    file.write("------------------------\n")
    for candidate, (votes, percentage) in percentage_votes.items():
        if percentage != 0:   
            file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write(f"Winner:"+ str(winners) + "\n")
    file.write("------------------------\n")