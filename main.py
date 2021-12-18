####################################################
#             CODE UNDER CONSTRUCTION              #
####################################################

########################
#       IMPORTS        #
########################
import sys
import colorama
from colorama import Fore  # For changing text
from colorama import Back as bg  # For background colors in themes
import pathlib  # For opening / saving files

# For networking commands
import socket  

###############################
#       TERMINAL CLASS        #
###############################
class Terminal:
    # Split the terminal text into a list.
    def split_terminal(self):
      self.user_input = self.user_input.split()
      

    # Show command options when user types help in terminal.
    def help_command(self):

      # Variable help
      print('\nvariables: ')
      print(Fore.CYAN + 'str ____ = ____', Fore.WHITE, ': create strings')
      print(Fore.CYAN + 'int ____ = ____', Fore.WHITE, ': create integers')
      print(Fore.CYAN + 'bool ____ = ____', Fore.WHITE, ': create booleans')
      print(Fore.CYAN + 'math ____ + ____', Fore.WHITE, ': do math - can use +, -, *, /, ^')
      print(Fore.WHITE + '1. you can type the variable name to output the variable result.')
      print(Fore.WHITE + '2. string concatenation is done by adding a dollar sign in front of the variable name within the string. Example: \nstr name = Brandon\nstr message = My name is $name\noutput: My name is Brandon')

      # Commands help
      print('\ncommands: ')
      print(Fore.CYAN + 'var' + Fore.WHITE + ': view variables list.')
      print(Fore.CYAN + 'hist' + Fore.WHITE + ' or ' + Fore.CYAN +  'history' + Fore.WHITE + ': view command history.')
      print(Fore.CYAN + 'cls' + Fore.WHITE + ' or ' + Fore.CYAN +  'clear' + Fore.WHITE + ': clear current terminal window.')
      print(Fore.CYAN + 'exit' + Fore.WHITE + ' or ' + Fore.CYAN +  'bye' + Fore.WHITE + ': close interface.')
      print(Fore.CYAN + 'theme ___' + Fore.WHITE + ': change terminal theme (beta). current themes: hacker, ocean, lite, inverted.')

      # Networking help
      print('\nnetworking: ')
      print(Fore.CYAN + 'ip' + Fore.WHITE + ': beginning of networking commands. must be followed by a sub command such as:')
      print('1. local: get local ip address.\n2. ping www.website_name.com: ping web address.\n3. bind 12345: bind to socket. replace 12345 with own numbers.')
      print('ip commands can usually be saved to a string. for example, str ip_address = %ip local. ensure that you use a % before ip to reference a networking command in your string. another example: str google = %ip ping www.google.com has an output relative to 216.239.38.120.')
    # THEMES

    def change_theme(self):
      # Hacker Theme
      if self.user_input[1] == 'hacker':
        self.theme_name = 'hacker'
        colorama.init()
        print(bg.BLACK)
        print(Fore.GREEN)
        print(colorama.ansi.clear_screen())
      # Lite Theme
      elif self.user_input[1] == 'lite':
        self.theme_name = 'lite'
        colorama.init()
        print(bg.WHITE)
        print(Fore.BLACK)
        print(colorama.ansi.clear_screen())
      # Ocean theme
      elif self.user_input[1] == 'ocean':
        self.theme_name = 'ocean'
        colorama.init()
        print(bg.BLUE)
        print(Fore.CYAN)
        print(colorama.ansi.clear_screen())
      elif self.user_input[1] == 'inverted':
        self.theme_name = 'inverted'
        colorama.init()
        print(bg.WHITE)
        print(Fore.WHITE)
        print(colorama.ansi.clear_screen())
      # Revert to regular theme. - NOT WORKING
      elif self.user_input[1] == 'reg' or self.user_input[1] == 'regular':
        self.theme_name = 'regular'
        colorama.init()
        print(bg.RESET_ALL)
        print(Fore.RESET_ALL)
        print(colorama.ansi.clear_screen())
      # Throw error if the user input an invalid theme name.
      else:
        print(Fore.RED + "Error: There is no theme: '" + self.user_input[1] + "'")
      
      # Print warning message
      print("warning: themes are not fully functional yet, you may experience glitches.")

    # Networking commands

    def networking(self):
      # If missing anything commands past ip
      if ter.user_input[1] is None or ter.user_input[1] == '':
        # Throw error if command is incorrect syntax.
        print(Fore.RED + 'error in networking command. recheck syntax. null command detected.')
      else:
        # View current local IP Address
        if ter.user_input[1] == 'local':
          self.result = socket.gethostbyname(socket.gethostname())
          print(self.result)
        elif ter.user_input[1] == 'ping':
          self.result = socket.gethostbyname(ter.user_input[2])
          print(self.result)
        elif ter.user_input[1] == 'bind':
          # Create a socket object
          s = socket.socket()        
          print ("Socket successfully created")
          
          # reserve a port on your computer in our
          # case it is 12345 but it can be anything
          port = int(ter.user_input[2])     
          
          # Next bind to the port
          # we have not typed any ip in the ip field
          # instead we have inputted an empty string
          # this makes the server listen to requests
          # coming from other computers on the network
          s.bind(('', port))        
          print ("socket binded to %s" %(port))
          
          # put the socket into listening mode
          s.listen(5)    
          print ("socket is listening")           
          
          # a forever loop until we interrupt it or
          # an error occurs
          while True:
          
          # Establish connection with client.
            c, addr = s.accept()    
            print ('Got connection from', addr )
          
            # send a thank you message to the client. encoding to send byte type.
            c.send('Thank you for connecting'.encode())
          
            # Close the connection with the client
            c.close()
        # All of SSH
        elif ter.user_input[1] == 'ssh':
          if ter.user_input[2] == 'view':
            # Subprocess
            print('SSH not currently working on nocap terminal.')
        else:
          # Throw error if command is incorrect syntax.
          print(Fore.RED + 'error in networking command. recheck syntax.')
    def file(self):
      if ter.user_input[1] == 'save':
        if ter.user_input[2] == 'as':
          file = pathlib.Path(ter.user_input[3] + '.nc')
          if file.exists ():
              self.user_answer = input("file exists by that name '" + ter.user_input[3] + "'. overwrite? (y/n)")
              if self.user_answer == 'y':
                print(Fore.RED + 'unable to overwrite file.')
              else:
                print(Fore.RED + 'process cancelled.')
          else:
            # Save file and create it using history
            with open(ter.user_input[3] + ".nc", 'x') as f:

              for xs in history:
                f.write(" ".join(map(str, xs)) + "\n")

              #f.write('Create a new text file!')
            print("file '" + ter.user_input[3] + "'.nc created.")

        else:
          pass
      if ter.user_input[1] == 'open':
        print('open command is not functional yet.')
        f = open("demofile2.txt", "a")
        f.write("Now the file has more content!")
        f.close()

        #open and read the file after the appending:
        f = open("demofile2.txt", "r")
        print(f.read())



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
                # 
                if self.user_input[3] == '$hist' or self.user_input[3] == '$history':
                  self.variables_add.append(self.user_input[1])
                  if len(self.user_input) > 3:
                    joined = " ".join(history[-2][3:])
                    self.variables_add.append(joined)
                  else:
                    print("There's an error, mate.")

                  # If there is already a variable by that name, then overwrite it.
                  if any(self.user_input[1] in x for x in self.variables_list):
                    # Find user input variable with for loop
                    for d in self.variables_list:
                      # Keep variable name
                      if d[0] == self.user_input[1]:
                        # Changes the value, not the variable name.
                        d[1] = self.variable_value
                  else:

                    self.variables_list.append(self.variables_add)

                  # Print variables_add for confirmation
                  print(self.variables_add[0], '=', self.variables_add[1]) 

                # Else run program as normal
                else:
                  # Combine string text and set to string value.
                  self.variable_value = " ".join(str(item) for item in self.user_input[3:])

                  # Find a dollar sign in variable value. This notifies the script that it is looking for a variable to concatenate.
                # Split variable value to look through each list item
                  split_var = self.variable_value.split()
                  # for loop to work through the split variables
                  for string in split_var:
                    # If the first letter in the string is a dollar sign
                    if string[0] == '$':
                      # Find index of split variable string
                      location = split_var.index(string)
                      # Update loc takes eveything after the dollar sign from the string
                      updated_loc = string[1:]
                      # If the updated_loc is within the variables list
                      if any(updated_loc in x for x in self.variables_list):
                        # Find user input variable with for loop
                        for d in self.variables_list:
                          # Place variable values in place of variable names.
                          if d[0] == updated_loc:
                            split_var[location] = d[1]
                            self.variable_value = self.variable_value.replace(string, str(d[1]))    
                    # This begins the ability to save a networking command output to a string.
                    elif string[0] == '%':
                      previous_text = []
                      previous_text = self.user_input
                      self.user_input[0] = 'ip'
                      if len(self.user_input) == 5:
                        self.user_input[1] = self.user_input[4]
                      elif len(self.user_input) == 6:
                        self.user_input[1] = self.user_input[4]
                        self.user_input[2] = self.user_input[5]

                      ter.networking()

                      self.user_input[1] = previous_text[1]
                      self.variable_value = ter.result


                  # If there is a plus symbol (concatenation) in code.
                  if '+' in self.variable_value:
                    # Split variable value by plus symbol, then combine into variable value
                    updated_var = self.variable_value.split(' + ')
                    self.variable_value = ' '.join(updated_var)

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
              self.error = Fore.RED + "syntax error: '=' expected after variable name."
              print(self.error)
        else:
          # Error thrown for if the user's input is not at least three words long.
          self.error = Fore.RED + "syntax error: '=' expected after variable name."
          print(self.error)

    # INTEGERS

    def do_integer(self):
      # Ensure that the user's input is at least 3 words. If not, an error will be thrown.
      if len(self.user_input) > 2:
        # Make sure there is an equals sign after the variable name or error is thrown.
        if self.user_input[2] == '=':
          # Error checking to ensure user inputs an integer.
          if self.user_input[3].isnumeric():
            
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
          # If user input is not a digit, then throw error
          else:
            self.error = Fore.RED + "variable error: expected integer."
            print(self.error)
        else:
          # Error is thrown if there is no equals sign after the variable name.
          self.error = Fore.RED + "syntax error: '=' expected after variable name."
          print(self.error)
      else:
        # Error thrown for if the user's input is not at least three words long.
          self.error = Fore.RED + "syntax error: '=' expected after variable name."
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
                        self.error = Fore.RED + "variable error: expected a boolean type."
                        print(self.error)
                    else:
                      # This error should not be thrown.
                      self.error = Fore.RED + "program error: please restart."
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
              self.error = Fore.RED + "variable error: expected a boolean type."
              print(self.error)
          
      else:
        # Error thrown for if the user's input is not at least three words long.
          self.error = Fore.RED + "syntax error: '=' expected after variable name."
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
ter.theme_name = ""

#############################
#         FUNCTIONS         #
#############################

def delete_var():
  # Find out if the input variable is within the variables list.
  if ter.user_input[1] == 'all':
    if var.variables_list == []:
      print(Fore.RED + 'error: no variables to delete in the variables list.')
    else:
      var.variables_list.pop()
      print('successfully deleted all variables.')
  elif any(ter.user_input[1] in x for x in var.variables_list):
          for d in var.variables_list:
            # If the variable name equals the first value within the variables list, then delete the second value.
            if d[0] == ter.user_input[1]:
              var_index = var.variables_list.index(d)
              var.variables_list.pop(var_index)
              # Print confirmation that the variable was deleted.
              print("successfully deleted variable: '" + d[0] + "'.")
  else:
    # Print error if the del variable is not within the variables list.
    error = Fore.RED + "error: '" + ter.user_input[1] + "' is not within the variables list."
    # Print error and tell the user how to check for variables list.
    print(error)
    print(Fore.WHITE + "type 'var' to see current variables list.")

#############################
#       WHILE RUNNING       #
#############################

# Output version upon startup of program.
print(Fore.WHITE + 'nocap v0.15')
print(Fore.WHITE + 'type help for assistance.')

# Set the history list
history = []

# While program is running
while 1:
  # Themes are still in early development.
    if ter.theme_name == 'hacker':
      # Hacker theme has green fore text.
      ter.user_input = input(Fore.GREEN + 'nocap.cmd > ')
    elif ter.theme_name == 'lite':
      # Lite theme has black fore text.
      ter.user_input = input(Fore.BLACK + 'nocap.cmd > ')
    elif ter.theme_name == 'ocean':
      # Ocean theme has cyan fore text.
      ter.user_input = input(Fore.CYAN + 'nocap.cmd > ')
    elif ter.theme_name == 'regular':
      # Revert back to regular theme.
      ter.user_input = input(Fore.WHITE + 'nocap.cmd > ')
    elif ter.theme_name == 'inverted':
      ter.user_input = input(Fore.WHITE + bg.BLACK + 'nocap.cmd > ')
    else:
      # Output shell >
      ter.user_input = input(Fore.WHITE + 'nocap.cmd > ')

    # Put user's input into a list separating each word within the terminal class.
    ter.split_terminal()
    var.user_input = ter.user_input

    # Add user input to history list.
    history.append(ter.user_input)

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
    # Allow user to delete a variable with the del command.
    elif ter.user_input[0] == 'del':
      # Call delete variables function.
        delete_var()
    # If user types variable name, then output result
    elif any(ter.user_input[0] in x for x in var.variables_list):
      for d in var.variables_list:
        # If the variable name equals the first value within the variables list, then print the second value.
        if d[0] == ter.user_input[0]:
          print(d[1])
    # Change the theme of the terminal window.
    elif ter.user_input[0] == 'theme':
      ter.change_theme()
    # Command to find IP address
    elif ter.user_input[0] == 'ip':
      ter.networking()
    # File commands
    elif ter.user_input[0] == 'file':
      ter.file()
    # View history of commands for current session.
    elif ter.user_input[0] == 'history' or ter.user_input[0] == 'hist':
      for xs in history:
        print(" ".join(map(str, xs)))
    # Clear terminal screen.
    elif ter.user_input[0] == 'clear' or ter.user_input[0] == 'cls':
      print('\033[H\033[J', end='')
    # Exit command to close program.
    elif ter.user_input[0] == "exit" or ter.user_input[0] == "bye":
      print("closing interface...")
      sys.exit()
    else:
        pass


# To be added: loops, math, lists, conditional statements, more networking commands, etc.
# Please let me know if there are any additional suggestions!