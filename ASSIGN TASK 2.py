# Step 1: Get user input and write to output.txt
text = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text + "\n")
print("Data successfully written to output.txt.")

# Step 2: Append more data to the same file
more_text = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(more_text + "\n")
print("Data successfully appended.")

# Step 3: Read and display the content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line, end='')
