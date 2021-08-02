
# Save the inputs into a list
records = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score]) 

# Sample list
records = [["chi", 20.0], ["beta", 50.0], ["Alpha", 50.0], ["James", 60]]


# List with scores only
score_list = [record[1] for record in records]

# remove duplicate values
new_score_list = set(score_list)
# remove first lowest score
new_score_list.remove(min(new_score_list))

# save second lowest grade .This is the grade of student with lowest grade

second_lowest_grade = min(new_score_list)

# Loop through the first list again.
# Find the names of student with the second lowest score you save above
# Sort them alphabetically and print the names on separate line

second_lowest_names = []
for record in records:
    if record[1] == second_lowest_grade:
        second_lowest_names.append(record[0])

sorted_second_lowest_names = sorted(second_lowest_names)

# Loop through the list and print the names
for name in sorted_second_lowest_names:
    print(name)

