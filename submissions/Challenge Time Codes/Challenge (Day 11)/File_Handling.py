with open('names.txt', 'r') as file:
    lines = file.readlines()
    print("List of names in the file before sorting:")
    for line in lines:
        print(line.strip())
    sorted_names = sorted(lines)

with open('names.txt', 'w') as file:
    file.writelines(sorted_names)
    print("\nList of names in the file after sorting:")
    for line in sorted_names:
        print(line.strip())