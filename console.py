#!/usr/bin/python3
import cmd
import string, sys
import os
import uuid

class HbnbConsole(cmd.Cmd):
    intro = "-------------------------------------\n|\
    Welcome to the HBnB console    |\n|\
    for help, input 'help'         |\n|\
    for quit, input 'quit'         |\n-------------------------------------\n"


    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb)'
    file = None
    last_output = ''

    
    def do_create(self, arg):
        """Created an object parsed from the console: create"""
        pass
    
    def do_shell(self, line):
        "Runs shell commands"
        output = os.popen(line).read()
        print(output)
        self.last_output = output
    
    def do_EOF(self, line):
        """Processes the end of file: EOF"""
        return True

    def do_quit(self, arg):
        """Stops the console and closes the terminal window, and exit: quit"""
        print("Process terimnated")
        self.exit(1)



if __name__=='__main__':
    HbnbConsole().cmdloop()