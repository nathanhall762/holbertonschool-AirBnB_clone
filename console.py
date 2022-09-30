#!/usr/bin/python3
"""console command controller for airbnb clone"""
import cmd


class HBNBCommand(cmd.Cmd):
    """implementing command line functionality"""
    def do_EOF(self):
        """foo"""

    def do_help(self):
        """bar"""

if __name__ == '__main__':
    HBNBCommand().cmdloop("(hbnb)")
