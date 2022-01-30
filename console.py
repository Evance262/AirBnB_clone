#!/usr/bin/python3
import cmd
import string, sys
import os

class HbnbConsole(cmd.Cmd):
    intro = "-------------------------------------\n|\
    Welcome to the HBnB console    |\n|\
    for help, input 'help'         |\n|\
    for quit, input 'quit'         |\n-------------------------------------\n"


    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb)'

    # my_class = {"BaseModel": BaseModel, "Amenity": Amenity,
    #             "City": City, "Place": Place, "Review": Review,
    #             "User": User, "State": State}
    
    file = None
    last_output = ''

    
    def do_create(self, arg):
        """Created an object parsed from the console: create"""
        if arg == "":
            print("** class name missing **")
            return
        try:
            new_instance = {}
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doen't exist **")
            return

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        list_arg = arg.split()
        obj_dict = storage.all()

        if len(list_arg) == 0:
            print("** class name missing **")
            return False
        if list_arg[0] not in HbnbConsole.my_class:
            print("** class doesn't exist **")
            return False
        if len(list_arg) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(list_arg[0], list_arg[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(list_arg) == 2:
            print("** attribute name missing **")
            return False
        if len(list_arg) == 3:
            try:
                type(eval(list_arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(list_arg) == 4:
            obj = obj_dict["{}.{}".format(list_arg[0], list_arg[1])]
            if list_arg[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[list_arg[2]])
                obj.__dict__[list_arg[2]] = valtype(list_arg[3])
            else:
                obj.__dict__[list_arg[2]] = list_arg[3]
        elif type(eval(list_arg[2])) == dict:
            obj = obj_dict["{}.{}".format(list_arg[0], list_arg[1])]
            for k, v in eval(list_arg[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_destroy(self, arg):
        """Destroys an object of a given uuid"""
        list_arg = arg.split()
        obj_dict = storage.all()
        if len(list_arg) == 0:
            print("** class name missing **")
        elif list_arg[0] not in HbnbConsole.my_class:
            print("** Invalid class **")
        elif len(list_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(list_arg[0], list_arg[1] not in obj_dict.keys()):
            print("** instance not found **")
        else:
            del obj_dict["{}.{}".format(list_arg[0], list_arg[1])]
            storage.save()
        
    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if arg == "":
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            list_arg = eval(arg_list[0])()
        except Exception:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        instance = 0
        for key, value in storage.all().items():
            if key == "{}.{}".format(arg_list[0], arg_list[1]):
                print(value)
                instance = 1
        if instance == 0:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Delete a class instance of a given id."""
        list_arg = arg.split()
        obj_dict = storage.all()
        if len(list_arg) == 0:
            print("** class name missing **")
        elif list_arg[0] not in HbnbConsole.my_class:
            print("** class doesn't exist **")
        elif len(list_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(list_arg[0], list_arg[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(list_arg[0], list_arg[1])]
            storage.save()

    def do_shell(self, line):
        "Runs shell commands"
        output = os.popen(line).read()
        print(output)
        self.last_output = output
    
    def do_EOF(self, line):
        """Processes the end of file: EOF"""
        sys.exit(1)

    def do_quit(self, arg):
        """Stops the console and closes the terminal window, and exit: quit"""
        print("Process terimnated")
        self.exit(1)



if __name__=='__main__':
    HbnbConsole().cmdloop()