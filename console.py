#!/usr/bin/python3
"""console command controller for airbnb clone"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """implementing command line functionality"""
    prompt = "(hbnb) "
    def do_quit(self, arg):
        """beans"""
        return True

    def do_EOF(self, arg):
        """foo"""
        return True

    def emptyline(self):
        """handles empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
