#Kindly ignor this file i am still learning git push and pull additionally how to delete files in directory
file_path = "election_data.csv"
def percentage_votes(candidate_votes,total_votes):
    percentage_votes={}
    for candidate, votes in candidate_votes.items():
        percentage=(votes/total_votes)*100
        percentage_votes[candidate] = (votes, percentage)
    return percentage_votes

def read_csv_count_votes(file_path):
    total_votes = 0
    candidate_votes={}
    data = []
    candidates = set()
    with open('Resources/election_data.csv', 'r') as file:
        for line in file:
            # Split the line into fields
            fields = line.strip().split(',')
            data.append(fields)
            candidate=fields[2]
            if candidate not in candidate_votes:
                candidate_votes[candidate] = 1
            else:
                candidate_votes[candidate] += 1

            total_votes += 1
    return data, total_votes, candidate_votes



csv_data, total_votes,candidate_votes = read_csv_count_votes(file_path)
percentage_votes = percentage_votes(candidate_votes, total_votes)

print("Election Results")
print("------------------------")
print("Total  votes:", total_votes)
print("------------------------")

for candidate, (votes, percentage) in percentage_votes.items():
    print(f"{candidate}: {percentage:.2f}%, ,{(votes)}" )
print("------------------------")
winners = [candidate for candidate, (_, percentage) in percentage_votes.items() if percentage == max(percentage_votes.values(), key=lambda x: x[1])[1]]

# Print out the names of the winner(s)
if len(winners) == 1:
    print("Winner:", winners[0])
else:
    print("Winners:", ", ".join(winners))

