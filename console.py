#!/usr/bin/python3
"""console command controller for airbnb clone"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """implementing command line functionality"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """quits the current shell"""
        return True

    def do_EOF(self, arg):
        """quits the current shell"""
        return True

    def emptyline(self):
        """handles empty line"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        pass

    def do_show(self, arg):
        """
        Prints the string representation
        of an instance based on the class name and id.
        """
        pass

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class
        name and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        pass

    def do_all(self, arg):
        """
        Prints all string representation
        of all instances based or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        pass

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
