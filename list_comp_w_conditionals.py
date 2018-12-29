# Find the intersection of two lists
answer = [num for num in [1, 2, 3, 4] if num in [3, 4, 5, 6] ]
print(answer)


# Return list of names with contained name string returned in reverse order and in  lowercase
answer2 = [name[::-1].lower() for name in ["Elie", "Tim", "Matt"]]
print(answer2)
