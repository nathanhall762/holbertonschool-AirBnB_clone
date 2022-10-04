#!/usr/bin/python3
"""console command controller for airbnb clone"""
import cmd
import sys
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User
from models import storage

school = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}
errors = {
    "1": "** class name missing **",
    "2": "** instance id missing **",
    "3": "** attribute name missing **",
    "4": "** value missing **",
    "5": "** class doesn't exist **",
    "6": "** no instance found"
}  # i would like to more elegantly handle the print() calls
bank = storage.all()


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
        if len(arg) == 0:
            print(errors["1"])
        elif arg in school.keys():
            command = school[arg]()
            command.save()
            print(command.id)
        else:
            print(errors["5"])
        # this command keeps feeding back the same object id
        # and i cant figure out if its making new ones or not

    def do_show(self, arg):
        """
        Prints the string representation
        of an instance based on the class name and id.

        """
        args = arg.split()
        if len(args) == 0:
            print(errors["1"])
        elif args[0] in school.keys():
            if len(args) > 1:
                found = f"{args[0]}.{args[1]}"
                print(bank[found] if found in bank
                      else errors["6"])
            else:
                print(errors["2"])
        else:
            print(errors["5"])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class
        name and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = arg.split()
        if len(args) == 0:
            print(errors["1"])
        elif args[0] in school.keys():
            if len(args) > 1:
                found = f"{args[0]}.{args[1]}"
                if found in bank:
                    del bank[found]
                    models.storage.save()
                else:
                    print(errors["6"])
        else:
            print(errors["5"])

    def do_all(self, arg):
        """
        Prints all string representation
        of all instances based or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        args = arg.split()
        if len(arg) > 0:
            print(school[args[1]] if args[1] in school.keys()
                  else errors["5"])
        else:
            print(bank)
        # using this shows a list index out of range :(

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = arg.split()
        commands = len(args)
        if commands < 4:
            print(errors[commands])
        elif args[0] not in school.keys():
            print(errors["5"])
        else:
            found = f"{args[0]}.{args[1]}"
            if found in bank:
                bank[found].update({
                    args[2]: args[3].strip("'\"")
                })
            else:
                print(errors["6"])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
