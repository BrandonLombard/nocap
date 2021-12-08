import sys
from colorama import Fore

# Set some variables to keep track of commands used.
history = []
i = 0

# Keep track of current variables here.
variables_list = []

print("nocap: v0.1")
print("type help for assistance.")
# While the program is running, output the shell.
while True:
  # Output shell >
  text = input(Fore.WHITE + 'nocap.cmd > ')
  # Creates a list holding the history of commands used.
  history += [text]

########################
#       COMMANDS       #
########################

  # If user types exit, then the program will close.
  if text == 'exit':
    sys.exit()
  # Allow the user to see all current variables and their values.
  if text == 'var':
    if variables_list == []:
      error = (Fore.RED + "There are no variables assigned for this sesson.")
      history += [error]
      print(error)
    else:
      # Output variable list
      print(variables_list)
  # User can call for history.
  if text == 'his':
    print(history)

# Help for user and command list
  if text == 'help':
    print("\ncommand list:\n")
    # Exit command help
    print(Fore.CYAN + "exit" + Fore.WHITE + " = exit the session.")
    # Variable command help
    print(Fore.CYAN + "var" + Fore.WHITE + " = see list of current variables. ")
    # Integer variable help
    print(Fore.CYAN + "int" + Fore.WHITE + " = integer. Syntax: int name = 1")
    # String variable help
    print(Fore.CYAN + "str" + Fore.WHITE + " = string. Syntax: str name = this is a string")
    # Calling variables help - simple
    print(Fore.WHITE + "You can enter a variable name and it will output the \nvalue of that variable.")
    print(Fore.CYAN + "math" + Fore.WHITE + " = conduct math on two numbers. Currently support: +, -, *, /, ^ (power operator). Syntax: math 1 + 1")
    print() # New line for formatting.
  
  # Extract numbers from input
  numbers = []  # Numbers collected in a list
  for word in text.split():
    if word.isdigit():
      numbers.append(int(word))

  # Turn the input into a list.
  split_input = text.split()

  # Check if user enters a variable name from current variables list
  def find_in_list_of_list(mylist, char):
    for sub_list in variables_list:
        if char in sub_list:
            return (mylist.index(sub_list), sub_list.index(char))
    raise ValueError("'{char}' is not in list".format(char = char))

  if any(text in x for x in variables_list) == True:
    # Obtain location of inputted variable and its value
    location_of_variable = find_in_list_of_list(variables_list, text)
    first_location = location_of_variable[0]
    second_location = location_of_variable[1]
    # Output variable value
    print(variables_list[first_location][0], '=', variables_list[first_location][1])



#########################
#       VARIABLES       #
#########################

  # Allow the user to create integers and store them into variables
  if split_input[0] == 'int':  # INTEGERS
    # Does not allow variable names to have integers in them
    if split_input[1].isdigit():
      variable_name = 'None'
      error = Fore.RED + "Syntax Error: Variables cannot have numbers in them."
      history += [error]
      print(error)
    else:
      # Assign the second element in the list to variable_name
      variable_name = split_input[1]
      if split_input[2] == "=":
          if split_input[3].isdigit():
            integer_value = int(split_input[3])
            print(split_input[0], variable_name, '=', integer_value)
            variables_list += [[variable_name,int(integer_value)]]
            #print(history)
          else:
            # Error checking and printing to screen + history
            error = (Fore.RED + "Variable Error: Expected Integer.")
            history += [error]
            print(error)
      else:
      # Error checking and printing to screen ][po0-qa~W32PO0-\]        + history
        error = (Fore.RED + "Syntax Error: Expected '=' after variable name.")
        history += [error]
        print(error)
  else:
    pass

  # Allow the user to create strings and store them into variables
  if split_input[0] == 'str':  # STRINGS
    # Does not allow variable names to have integers in them
    if split_input[1].isdigit():
      error = Fore.RED + "Syntax Error: Variables cannot have numbers in them."
      history += [error]
      print(error)
    else:
      # If variable is already used then delete old variable and replace with new
      already_used = split_input[1] in [j for i in variables_list for j in i]
      if already_used:
        variable_location = find_in_list_of_list(variables_list, split_input[1])
        variables_list[variable_location[0]].pop(0) 
        variables_list[variable_location[0]].pop(0) 
        # Assign the second element in the list to variable_name
        variable_name = split_input[1]
        if split_input[2] == "=":  # put into a string
            string_value = " ".join(str(item) for item in split_input[3:-1])
            print(split_input[0], variable_name, '=', string_value)
            variables_list += [[variable_name , str(string_value)]]
        else:
          # Error checking and printing to screen + history
          error = Fore.RED + ("Syntax Error: Expected '=' after variable name.")
          history += [error]
          print(error)
      else:
        # Assign the second element in the list to variable_name
        variable_name = split_input[1]
        # If the third piece of the input is an equals sign
        if split_input[2] == "=": 
          # join the rest of the input to string_value to act as a string.
            string_value = " ".join(str(item) for item in split_input[3:-1])
            # Print out complete command to indicate a working code
            print(split_input[0], variable_name, '=', string_value)
            # Add that variable name and value to the variables list.
            variables_list += [[variable_name , str(string_value)]]
        else:
          # Error checking and printing to screen + history
          error = Fore.RED + ("Syntax Error: Expected '=' after variable name.")
          history += [error]
          print(error)
  else:
    pass

##########################
#          MATH          #
##########################

  if split_input[0] == "math":
    # 0 / 0 equals undefined
    if text == "math 0 / 0":
      print("Undefined")
    # else continue the program
    else:
      # Adding two values.
      if len(split_input) < 4:
        # Error checking and printing to screen + history
        error = Fore.RED + ("Math Error: Missing values or elements after math command.")
        history += [error]
        print(error)
      # If one or more math values are not an integer, produce an error.
      elif (split_input[1].isdigit() == False) or (split_input[3].isdigit() == False):
        # Error checking and printing to screen + history
        error = Fore.RED + ("Math Error: Expected integer(s) for math values.")
        history += [error]
        print(error)
      else:
        if split_input[2] == '+':
          print(int(split_input[1]) + int(split_input[3]))
        # Subrating two values
        elif split_input[2] == '-':
          print(int(split_input[1]) - int(split_input[3]))
        # Multiplying two values.
        elif split_input[2] == '*':
          print(int(split_input[1]) * int(split_input[3]))
        # Dividing two values.
        elif split_input[2] == '/':
          print(int(split_input[1]) / int(split_input[3]))
        # Power operator
        elif split_input[2] == '^':
          print(int(split_input[1]) ** int(split_input[3]))
        else:
          # Error checking and printing to screen + history
          error = Fore.RED + ("Math Error: Expected '+', '-', '*', '/', or '^'.")
          history += [error]
          print(error)