from pathlib import Path

# Opgave 10-1 Learning Python
path = Path('AI programmering opgaver/Kapitel 10+11 opgaver/learning_python.txt')

# Read the entire content of the file
contents = path.read_text()
contents.replace('Python', 'C')

print("Contents of the file:")
print(contents)


# Read the file line by line
lines = path.read_text().splitlines()  # Split the content into lines
print("\nContents printed line by line:")
for line in lines:
    print(line)

# Optionally, print the total length of the content
print(f"\nTotal length of the content: {len(contents)} characters")

#Opgave 10-2 Learning C


# Replace 'Python' with 'C'
modified_contents = contents.replace('Python', 'C')

print("Contents of the file with 'Python' replaced by 'C':")
print(modified_contents)


# Read the file line by line and replace 'Python' with 'C' in each line
lines = path.read_text().splitlines()  # Split the content into lines
print("\nContents printed line by line with 'Python' replaced by 'C':")
for line in lines:
    modified_line = line.replace('Python', 'C')  # Replace 'Python' in each line
    print(modified_line)

# Optionally, print the total length of the modified content
print(f"\nTotal length of the modified content: {len(modified_contents)} characters")

