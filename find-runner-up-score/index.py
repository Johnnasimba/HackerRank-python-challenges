
# Given a list
list = [2, 3, 6, 6, 5]

# Convert the list into a set to remove all duplicate values and remain with only distinct values

new_list = set(list)

# Find the max number of the new list and remove it
new_list.remove(max(new_list))

# Now that you removed the max number, if you try to find max number again the answer will be the second heightest since the first one was removed

print(max(new_list))
