print("Beginning of the tool counter program")

# This will store all the tools at a future datestop
tool_dictionary = {}

# Main feedback loop
while True:
    language_name = input("Enter the name of the language. Type 'stop' to stop and 'print' to print.\n")

    # First we check if the tool already exists in our dictionary
    if language_name in tool_dictionary:
        print(f"Incremented {language_name}.")
        tool_dictionary[language_name] += 1

    # Then, we check for the print command
    elif language_name == 'print':
        sorted_tools = sorted(tool_dictionary.items(), key=lambda x: x[1], reverse=True)
        # After we sort the tools, we print the list of tools
        for i in sorted_tools:
            print(f"{i[0].title()} ({i[1]} instances)")

    # If the user entered 'stop' the program terminates
    elif language_name == 'stop':
        break

    # If it's a new tool we haven't seen before, it adds it to the dictionary
    else:
        tool_dictionary[language_name] = 1
    
print("Good luck learning!")