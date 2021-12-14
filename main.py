####################################################
#             CODE UNDER CONSTRUCTION              #
####################################################

########################
#       IMPORTS        #
########################
import sys
from colorama import Fore  # For changing text


###############################
#       TERMINAL CLASS        #
###############################
class Terminal:
    # Split the terminal text into a list.
    def split_terminal(self):
      self.user_input = self.user_input.split()

    # Show command options when user types help in terminal.
    def help_command(self):
      print('variables: ')
      print(Fore.CYAN + 'str ____ = ____', Fore.WHITE, ': create strings')
      print(Fore.CYAN + 'int ____ = ____', Fore.WHITE, ': create integers')
      print(Fore.CYAN + 'bool ____ = ____', Fore.WHITE, ': create booleans')
      print(Fore.CYAN + 'math ____ + ____', Fore.WHITE, ': do math - can use +, -, *, /, ^')
      print('Commands: ')
      print(Fore.CYAN + 'exit' + Fore.WHITE + ' or ' + Fore.CYAN +  'bye' + Fore.WHITE + ': close interface.')

###############################
#       VARIABLES CLASS       #
###############################
class Variables:

    # STRINGS

    def do_string(self):
        # Ensure that the user's input is at least 3 words. If not, an error will be thrown.
        if len(self.user_input) > 2:
            # Make sure there is an equals sign after the variable name or error is thrown.
            if self.user_input[2] == '=':
                self.variables_add = []  # Reset variables_add list
                # Combine string text and set to string value.
                self.variable_value = " ".join(str(item) for item in self.user_input[3:])
                # Add variable name and string to the variables list.
                self.variables_add += [self.user_input[1], self.variable_value]
                # If there is already a variable by that name, then overwrite it.
                if any(self.user_input[1] in x for x in self.variables_list):
                  # Find user input variable with for loop
                  for d in self.variables_list:
                    # Keep variable name
                    if d[0] == self.user_input[1]:
                      # Changes the value, not the variable name.
                      d[1] = self.variable_value
                      
                # Append to variable list if it is not already within the variables list.
                else:
                  self.variables_list.append(self.variables_add)

                # Print variables_add for confirmation
                print(self.variables_add[0], '=', self.variables_add[1]) 
            else:
              # Error is thrown if there is no equals sign after the variable name.
              self.error = Fore.RED + "Syntax Error: '=' Expected after variable name."
              print(self.error)
        else:
          # Error thrown for if the user's input is not at least three words long.
            self.error = Fore.RED + "Syntax Error: '=' Expected after variable name."
            print(self.error)

    # INTEGERS

    def do_integer(self):
      # Ensure that the user's input is at least 3 words. If not, an error will be thrown.
      if len(self.user_input) > 2:
        # Make sure there is an equals sign after the variable name or error is thrown.
        if self.user_input[2] == '=':
          self.variables_add = [] # Reset variables_add list
          # Put integer into variable value.
          self.variable_value = int(self.user_input[3])
          # Add variable name and string to the variables list.
          self.variables_add += [self.user_input[1], self.variable_value]

          if any(self.user_input[1] in x for x in self.variables_list):
                  # Find user input variable with for loop
                  for d in self.variables_list:
                    # Keep variable name
                    if d[0] == self.user_input[1]:
                      # Changes the value, not the variable name.
                      d[1] = self.variable_value

          # Append to variable list.
          self.variables_list.append(self.variables_add)
          # Print variables_add for confirmation
          print(self.variables_add[0], '=', self.variables_add[1]) 
        else:
          # Error is thrown if there is no equals sign after the variable name.
          self.error = Fore.RED + "Syntax Error: '=' Expected after variable name."
          print(self.error)
      else:
        # Error thrown for if the user's input is not at least three words long.
          self.error = Fore.RED + "Syntax Error: '=' Expected after variable name."
          print(self.error)

    # Booleans

    def do_boolean(self):
      # Ensure that the user's input is at least 3 words. If not, an error will be thrown.
      if len(self.user_input) > 2:
        if self.user_input[2] == '=':
          self.variables_add = [] # Reset variables_add list

          if any(self.user_input[1] in x for x in self.variables_list):
                  # Find user input variable with for loop
                  for d in self.variables_list:
                    # Keep variable name
                    if d[0] == self.user_input[1]:
                      # Changes the value, not the variable name.
                      if self.user_input[3] == 'true' or self.user_input[3] == 't' or self.user_input[3] == '1':
                        self.variable_value = 'b_true'
                        d[1] = self.variable_value
                        # Add variable name and string to the variables list.
                        self.variables_add += [self.user_input[1], self.variable_value]
                        print(self.variables_add[0], '=', self.variables_add[1]) 
                        break
                      elif self.user_input[3] == 'false' or self.user_input[3] == 'f' or self.user_input[3] == '0':
                        self.variable_value = 'b_false'
                        d[1] = self.variable_value
                        # Add variable name and string to the variables list.
                        self.variables_add += [self.user_input[1], self.variable_value]
                        print(self.variables_add[0], '=', self.variables_add[1]) 
                        break
                      else:
                        # Error thrown for if the user's input is not at least three words long.
                        self.error = Fore.RED + "Variable Error: Expected a Boolean Type."
                        print(self.error)
                    else:
                      # This error should not be thrown.
                      self.error = Fore.RED + "Program Error: Please Restart."
                      print(self.error)
          # Append to variable list if it is not already within the variables list.
          else:
            # Put bool type into variable value.
            if self.user_input[3] == 'true' or self.user_input[3] == 't' or self.user_input[3] == '1':
              self.variable_value = 'b_true'
              # Add variable name and string to the variables list.
              self.variables_add += [self.user_input[1], self.variable_value]
              self.variables_list.append(self.variables_add)
              print(self.variables_add[0], '=', self.variables_add[1]) 
            elif self.user_input[3] == 'false' or self.user_input[3] == 'f' or self.user_input[3] == '0':
              self.variable_value = 'b_false'
              # Add variable name and string to the variables list.
              self.variables_add += [self.user_input[1], self.variable_value]
              self.variables_list.append(self.variables_add)
              print(self.variables_add[0], '=', self.variables_add[1]) 
            else:
              self.error = Fore.RED + "Variable Error: Expected a Boolean Type."
              print(self.error)
          
      else:
        # Error thrown for if the user's input is not at least three words long.
          self.error = Fore.RED + "Syntax Error: '=' Expected after variable name."
          print(self.error)




#############################
#       CLASS CONFIGS       #
#############################

# Set Variables class to var.
var = Variables()
var.error = ""
var.user_input = ""
var.variables_list = []
var.variable_value = ""
var.variables_add = []
var.variable_location = []

# Set Terminal class to ter.
ter = Terminal()
ter.user_input = []

#############################
#       WHILE RUNNING       #
#############################

# Output version upon startup of program.
print(Fore.WHITE + 'nocap v0.1')
print(Fore.WHITE + 'type help for assistance.')

# While program is running
while 1:
    # Output shell >
    ter.user_input = input(Fore.WHITE + 'nocap.cmd > ')
    # Put user's input into a list separating each word within the terminal class.
    ter.split_terminal()
    var.user_input = ter.user_input

    # Check user's input to see what their first word is
    # If it is any of these, then it calls the corresponding class.
    # If string
    if ter.user_input[0] == 'str':
      var.do_string()
    # If int
    elif ter.user_input[0] == 'int':
      var.do_integer()
    # If boolean
    elif ter.user_input[0] == 'bool':
      var.do_boolean()
    # If math
    elif ter.user_input[0] == 'math':
        print('math is not working yet')
    # print variables list if user types 'var' command.
    elif ter.user_input[0] == 'var':
        print(var.variables_list)
    # If user types the help command.
    elif ter.user_input[0] == 'help':
        ter.help_command()
    elif ter.user_input[0] == "exit" or ter.user_input[0] == "bye":
      print("closing interface...")
      sys.exit()
    else:
        pass


# To be added: loops, string concatenation, math, delete var command, etc.